# TODO: ccxt precisions (manually or deduce from tickers)
# Note: some markets are disabled for non-resident countries

from uxs.base.socket import ExchangeSocket

import fons.log
from uxs.fintls.l3 import create_l3_orderbook, get_full_l3_loc_by_id,\
    get_l3_loc_by_id

logger,logger2,tlogger,tloggers,tlogger0 = fons.log.get_standard_5(__name__)


class luno(ExchangeSocket):
    exchange = 'luno'
    url_components = {
        'ws': 'wss://ws.luno.com/api/1/stream',
    }
    auth_defaults = {
        'takes_input': False,
        'each_time': True,
        'send_separately': False,
    }
    channel_defaults = {
        'url': '<$ws>/<symbol>',
        'is_private': True,
        'cnx_params_converter_config': {
            'lower': {'symbol': False}
        },
        'drop_unused_connection': True,
    }
    channels = {
        'account': {
            'required': ['symbol'],
            'identifying': (),
        },
    }
    connection_defaults = {
        'ping_interval': 30,
        'connect_timeout': 5,
        'reconnect_try_interval': 5, # initial connect often fails
    }
    has = {   
        'l3': True,
        'trades': {'emulated': 'l3'},
        'account': {
            'order': {'emulated': 'l3'},
            'fill': {'emulated': 'l3'}
        },
        'fetch_balance': {'free': True, 'used': True, 'total': True},
        'fetch_my_trades': {'symbolRequired': True},
        'fetch_tickers': {
                'last': True, 'bid': True, 'ask': True, 'bidVolume': False, 'askVolume': False,
                'high': False, 'low': False, 'open': False, 'close': True, 'previousClose': False,
                'change': False, 'percentage': False, 'average': False, 'vwap': False,
                'baseVolume': True, 'quoteVolume': False, 'active': False},  
    }
    has['fetch_ticker'] = has['fetch_tickers'].copy()
    ob = {
        'force_create': None,
        'uses_nonce': False,
    }
    l3 = {
        'force_create': None,
        'receives_snapshot': True,
        # 'default_limit': 10,
        # 'limits': [10],
    }
    order = {
        'update_filled_on_fill': True,
        'update_payout_on_fill': True,
        'update_remaining_on_fill': True,
    }
    trade = {
        'sort_by': lambda x: (x['timestamp'], x['price'], x['amount']),
    }
    
    def handle(self, R):
        if R.data:
            self.on_l3(R)
    
    
    def on_l3(self, R):
        """
        Snapshot:
        {
          'sequence': '6583315',
          'asks': [{'id': 'BXGQ2UUH4MBJ9UM', 'price': '0.03019', 'volume': '9.69'}],
          'bids': [...],
          'timestamp': 1595868645960,
          'status': 'ACTIVE'
        }
        Updates:
        {
          'sequence': '6583316',
          'trade_updates': None,
          'create_update': {'order_id': 'BXFHNGY5DFJFUWZ', 'type': 'BID', 'price': '0.030101', 'volume': '0.11'},
          'delete_update': {'order_id': 'BXJ47SQ44MC5S3Q'},
          'status_update': None,
          'timestamp': 1595868647503
        }
        Trade updates must be subtracted from open orders (no `create` / `delete` update is sent for the trade,
        unless the taker order has a remaining amount, in which case `create` update is sent for the new order)
        {
          'sequence': '6583332',
          'trade_updates':
            [
              {
                'base': '0.11',                        // base amount
                'counter': '0.00331111',               // quote amount
                'maker_order_id': 'BXFHNGY5DFJFUWZ',
                'taker_order_id': 'BXNXSZBCWMJ6XHW',
                'order_id': 'BXFHNGY5DFJFUWZ'          // always maker order id
              },
              ...
            ], 
          'create_update': None,
          'delete_update': None,
          'status_update': None,
          'timestamp': 1595868668344
        }
        """
        cnx = self.cm.connections[R.id]
        s = next((s for s in self.subscriptions if s.cnx is cnx and s.channel=='l3'), None)
        if s is None:
            return
        symbol = s.params['symbol']
        r = R.data
        is_snap = 'status' in r
        ob_0 = dict(symbol=symbol, timestamp=r['timestamp'], nonce=int(r['sequence']))
        trades = []
        if is_snap:
            ob = self.parse_l3_snapshot(dict(r, **ob_0))
            self.l3_maintainer.send_orderbook(ob)
        elif symbol in self.l3_books:
            ob = dict(ob_0, bids=[], asks=[])
            updates = []
            if r.get('trade_updates'):
                _updates, trades = self.parse_l3_trade_updates(r['trade_updates'], symbol, ob_0['timestamp'])
                updates += _updates
            if r.get('create_update'):
                updates += [self.parse_l3_create_update(r['create_update'])]
            if r.get('delete_update'):
                updates += [self.parse_l3_delete_update(r['delete_update'], symbol)]
            for u in updates:
                for side in ('bids','asks'):
                    ob[side] += u.get(side, [])
            self.l3_maintainer.send_update(ob)
        
        is_active = s.state
        subbed_to_account = self.is_subscribed_to(('account',))
        subbed_to_trades = self.is_subscribed_to(('trades',symbol))
        
        if is_active:
            if subbed_to_account:
                self.change_subscription_state(('account',), 1)
            if subbed_to_trades:
                self.change_subscription_state(('trades',symbol), 1)
        
        if subbed_to_trades:
            self.update_trades([{'symbol': symbol, 'trades': trades}], enable_sub=is_active)
        
        for t in trades:
            taker_id = t['info']['taker_order_id']
            maker_id = t['info']['maker_order_id']
            for tOM, id in [('taker', taker_id),('maker', maker_id)]:
                if id in self.orders:
                    f = dict(t, order=id, takerOrMaker=tOM)
                    self.add_fill_from_dict(f, enable_sub=is_active)
    
    
    def parse_l3_snapshot(self, ob):
        return create_l3_orderbook(ob, ob['timestamp'], 'bids', 'asks', 'price', 'volume', 'id')
    
    
    def parse_l3_trade_updates(self, trades, symbol, timestamp=None):
        l3 = self.l3_books[symbol]
        updates = []
        parsed_trades = []
        maker_side = None
        for t in trades:
            maker_id = t['maker_order_id']
            taker_id = t['taker_order_id']
            amount = float(t['base'])
            cost = float(t['counter'])
            if maker_side is None:
                maker_side, maker_loc = get_full_l3_loc_by_id(l3, maker_id)
            else:
                maker_loc = get_l3_loc_by_id(l3[maker_side], maker_id)
            maker_item = l3[maker_side][maker_loc]
            price = maker_item[0]
            new_item = [price, maker_item[1]-amount, maker_item[2]]
            updates.append({maker_side: [new_item]})
            parsed_trades.append(
                self.api.trade_entry(symbol=symbol, amount=amount, price=price, cost=cost,
                                     takerOrMaker='taker', order=taker_id, timestamp=timestamp, info=t))
        return updates, parsed_trades
    
    
    def parse_l3_create_update(self, u):
        side = 'bids' if u['type']=='BID' else 'asks'
        item = [float(u['price']), float(u['volume']), u['order_id']]
        return {side: [item]}
    
    
    def parse_l3_delete_update(self, u, symbol):
        l3 = self.l3_books[symbol]
        id = u['order_id']
        side, loc = get_full_l3_loc_by_id(l3, id)
        if side is None:
            return {}
        item = l3[side][loc]
        return {side: [[item[0], .0, id]]}
    
    
    def encode(self, req, sub=None):
        if not sub:
            return None
        return {}
    
    
    def sign(self, *args):
        return {
          'api_key_id': self.apiKey,
          'api_key_secret': self.secret
        }
