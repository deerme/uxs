# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import BadRequest
from ccxt.base.errors import BadSymbol
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import NotSupported
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import InvalidNonce


class coinbene(Exchange):

    def describe(self):
        return self.deep_extend(super(coinbene, self).describe(), {
            'id': 'coinbene',
            'name': 'CoinBene',
            'countries': ['CN', 'US'],
            'version': 'v2',
            'rateLimit': 1500,
            'has': {
                'cancelOrders': True,
                'fetchClosedOrders': True,
                'fetchMyTrades': False,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchTickers': True,
            },
            'timeframes': {
                '1m': '1',
                '3m': '3',
                '5m': '5',
                '15m': '15',
                '30m': '30',
                '1h': '60',
                '2h': '120',
                '4h': '240',
                '6h': '360',
                '12h': '720',
                '1d': 'D',
                '1w': 'W',
                '1M': 'M',
            },
            'urls': {
                'logo': 'https://res.coinbene.mobi/coinbene-article/9f524eb71731f51e.png',
                'api': 'https://openapi-exchange.coinbene.com',
                'www': 'http://www.coinbene.com',
                'prefixPath': '/api/exchange/v2/',
                'referral': 'http://www.coinbene.com',
                'doc': [
                    'https://github.com/Coinbene/API-SPOT-v2-Documents',
                ],
            },
            'api': {
                'public': {
                    'get': [
                        'market/tradePair/list',
                        'market/tradePair/one',
                        'market/ticker/list',
                        'market/ticker/one',
                        'market/orderBook',
                        'market/trades',
                        'market/instruments/candles',
                        'market/rate/list',
                    ],
                },
                'private': {
                    'get': [
                        'account/list',
                        'account/one',
                        'order/info',
                        'order/openOrders',
                        'order/closedOrders',
                        'order/trade/fills',
                    ],
                    'post': [
                        'order/place',
                        'order/cancel',
                        'order/batchCancel',
                        'order/batchPlaceOrder',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'taker': 0.001,
                    'maker': 0.001,
                },
            },
            'exceptions': {
                '429': DDoSProtection,	        # Requests are too frequent
                '430': ExchangeError,	        # API user transactions are not supported at self time
                '10001': BadRequest,	        # "ACCESS_KEY" cannot be empty
                '10002': BadRequest,	        # "ACCESS_SIGN" cannot be empty
                '10003': BadRequest,	        # "ACCESS_TIMESTAMP" cannot be empty
                '10005': InvalidNonce,	        # Invalid ACCESS_TIMESTAMP
                '10006': AuthenticationError,	# Invalid ACCESS_KEY
                '10007': BadRequest,	        # Invalid Content_Type, please use "application / json" format
                '10008': InvalidNonce,	        # Request timestamp expired
                '10009': ExchangeNotAvailable,	# System Error
                '10010': AuthenticationError,	# API authentication failed
                '11000': BadRequest,        	# Required parameter cannot be empty
                '11001': BadRequest,        	# Incorrect parameter value
                '11002': InvalidOrder,     	    # Parameter value exceeds maximum limit
                '11003': ExchangeError,      	# No data returned by third-party interface
                '11004': InvalidOrder,         	# Order price accuracy does not match
                '11005': InvalidOrder,      	# The currency pair has not yet opened leverage
                '11007': ExchangeError,      	# Currency pair does not match asset
                '51800': ExchangeError,     	# The transaction has been traded, failure
                '51801': OrderNotFound,     	# The order does not exist, the cancellation of failure
                '51802': BadSymbol,         	# TradePair Wrong
                '51803': InvalidOrder,      	# Buy Price must not be more than current price {0}%
                '51804': InvalidOrder,      	# Sell price must not be less than current price {0}%
                '51805': InvalidOrder,      	# Order price Most decimal point {0}
                '51806': InvalidOrder,      	# Order quantity Most decimal point {0}
                '51807': InvalidOrder,      	# Buy at least {0}
                '51808': InvalidOrder,      	# Sell at least {0}
                '51809': InsufficientFunds,	    # Insufficient balance or account is frozen
                '51810': ExchangeError,	        # selling not supported
                '51811': PermissionDenied,  	# Sorry, you do not have the authority to trade.
                '51812': InvalidOrder,      	# The buy price exceeds the limit of {1} within current {0}-hour cycle. Please adjust the price.
                '51813': InvalidOrder,      	# The sell price exceeds the limit of {1} within current {0}-hour cycle. Please adjust the price.
                '51814': InvalidOrder,      	# Schedule Order can only be cancelled before triggering
                '51815': InvalidOrder,      	# Order Type Error
                '51816': BadRequest,      	    # Account Type Error
                '51817': BadSymbol,         	# Trade Pair Error
                '51818': InvalidOrder,        	# Trade Orientation Error
                '51819': InvalidOrder,        	# Order Interface Error
                '51820': InvalidOrder,        	# Trigger Price Error
                '51821': InvalidOrder,      	# Trigger price Most decimal point {0}
                '51822': InvalidOrder,      	# Purchase price shall not be higher than trigger price {0}%
                '51823': InvalidOrder,      	# Selling Price shall not be under Trigger Price{0}%
                '51824': InvalidOrder,      	# Order Price Error
                '51825': InvalidOrder,      	# Order Amount Error
                '51826': InvalidOrder,      	# Order amount Most decimal point {0}
                '51827': InvalidOrder,      	# Order Quantity Error
                '51828': InvalidOrder,      	# Quantity of senior open order can not exceed {0}
                '51829': InvalidOrder,      	# Trigger price shall be higher than the latest filled price
                '51830': InvalidOrder,      	# Trigger price shall be lower than the latest filled price
                '51831': InvalidOrder,      	# Limited Price Error
                '51832': InvalidOrder,      	# Limited price Most decimal point {0}
                '51833': InvalidOrder,      	# Limited price shall be higher than the latest filled price
                '51834': InvalidOrder,      	# Limited price shall be lower than the latest filled price
                '51835': ExchangeError,     	# Account not found
                '51836': OrderNotFound,     	# Order does not exist
                '51837': InvalidOrder,      	# Order Number Error
                '51838': InvalidOrder,      	# Quantity of batch ordering can not exceed {0}
                '51839': ExchangeError,     	# Account freezing failed
                '51840': ExchangeError,     	# Account checking failed
                '51841': InvalidOrder,      	# Trade pair have no settings of price limit
                '51842': InvalidOrder,      	# Showing Quantity of Iceberg Order shall be greater than 0
                '51843': InvalidOrder,      	# Price limit checking failed
                '51844': BadRequest,        	# Start time error
                '51845': BadRequest,      	    # End time error
                '51846': BadRequest,      	    # Start time should be earlier than end time
                '51847': BadRequest,      	    # Maximum download time period is {0} days
                '51848': InvalidOrder,      	# Purchase Price shall not be under Trigger Price {0}%
                '51849': InvalidOrder,      	# Selling price can not be higher than trigger price {0}%
                '51850': ExchangeError,     	# The maximum number of download tasks is {0}
                '51851': BadRequest,     	    # Start time: Only a specific time of the past 3 months is available
            },
            'options': {
                'currencyNames': None,
                'orderTypes': {
                    'limit': '1',
                    'market': '2',
                },
                'direction': {
                    'buy': '1',
                    'sell': '2',
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetMarketTradePairList(params)
        result = []
        for i in range(0, len(response['data'])):
            market = response['data'][i]
            slashedId = self.safe_string(market, 'symbol').upper()
            base = None
            quote = None
            baseId = None
            quoteId = None
            if slashedId.find('/') >= 0:
                parts = slashedId.split('/')
                base = self.safe_currency_code(parts[0])
                baseId = parts[0].lower()
                quote = self.safe_currency_code(parts[1])
                quoteId = parts[1].lower()
            symbol = base + '/' + quote
            id = (baseId + quoteId).upper()
            precision = {
                'price': self.safe_integer(market, 'pricePrecision'),
                'amount': self.safe_integer(market, 'amountPrecision'),
            }
            priceFluctuation = self.safe_float(market, 'priceFluctuation')
            limits = {
                'amount': {
                    'min': self.safe_float(market, 'minAmount'),
                    'max': None,
                },
                'price': {
                    'min': None,  # 1 - priceFluctuation,
                    'max': None,  # 1 + priceFluctuation,
                },
            }
            limits['cost'] = {
                'min': None,  # limits['amount']['min'] * limits['price']['min'],
                'max': None,
            }
            result.append({
                'id': id,                # BTCUSDT
                'slashedId': slashedId,  # BTC/USDT
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    def parse_slashed_id(self, slashedId):
        # convert slashedId to id
        if slashedId is None:
            return None
        elif slashedId.find('/') < 0:
            return slashedId.upper()
        else:
            split = slashedId.split('/')
            return(split[0] + split[1]).upper()

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        if limit is None:
            limit = 10  # 5, 10, 50, 100. Default value 10
        request = {
            'symbol': market['slashedId'],
            'depth': limit,
        }
        response = self.publicGetMarketOrderBook( self.extend(request, params))
        orderBook = response['data']
        timestamp = self.parse8601(self.safe_string(orderBook, 'timestamp'))
        return self.parse_order_book(orderBook, timestamp)
        return orderBook

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['slashedId'],
        }
        response = self.publicGetMarketTickerOne(self.extend(request, params))
        return self.parse_ticker(response['data'], market)

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetMarketTickerList(params)
        return self.parse_tickers(response['data'], symbols)

    def parse_ticker(self, ticker, market=None):
        if market is None:
            marketId = self.parse_slashed_id(self.safe_string(ticker, 'symbol'))
            market = self.safe_value(self.markets_by_id, marketId)
        last = self.safe_float(ticker, 'latestPrice')
        percentage = None
        open = None
        average = None
        change = None
        chg24h = self.safe_string(ticker, 'chg24h')
        if chg24h is not None and chg24h.find('%') >= 0:
            loc = chg24h.find('%')
            percentage = float(chg24h[0:loc]) / 100
            if last is not None:
                open = last / (1 + percentage)
                average = (open + last) / 2
                change = last - open
        return {
            'symbol': self.safe_string(market, 'symbol'),
            'info': ticker,
            'timestamp': None,
            'datetime': None,
            'high': self.safe_float(ticker, 'high24h'),
            'low': self.safe_float(ticker, 'low24h'),
            'bid': self.safe_float(ticker, 'bestBid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'bestAsk'),
            'askVolume': None,
            'vwap': None,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': average,
            'percentage': percentage,
            'average': average,
            'baseVolume': None,
            'quoteVolume': self.safe_float(ticker, 'volume24h'),
        }

    def parse_tickers(self, rawTickers, symbols=None):
        tickers = []
        for i in range(0, len(rawTickers)):
            tickers.append(self.parse_ticker(rawTickers[i]))
        return self.filter_by_array(tickers, 'symbol', symbols)

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['slashedId'],
            'period': self.timeframes[timeframe],
        }
        if since is not None:
            request['start'] = int(since / 1000)
        response = self.publicGetMarketInstrumentsCandles(self.extend(request, params))
        return self.parse_ohlcvs(response['data'], market, timeframe, since, limit)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        return [
            self.parse8601(self.safe_string(ohlcv, 0)),
            self.safe_float(ohlcv, 1),
            self.safe_float(ohlcv, 2),
            self.safe_float(ohlcv, 3),
            self.safe_float(ohlcv, 4),
            self.safe_float(ohlcv, 5),
        ]

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['slashedId'],
        }
        response = self.publicGetMarketTrades(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    def parse_trade(self, trade, market=None):
        symbol = None
        if market is None:
            marketId = self.safe_string(trade, 0)
            market = self.safe_value(self.markets_by_id, marketId)
        if market is not None:
            symbol = market['symbol']
        price = self.safe_float_2(trade, 1, 'price')
        # quantity = fill['quantity']
        amount = self.safe_float_2(trade, 2, 'amount')
        side = self.safe_string_2(trade, 3, 'direction')
        timestamp = self.parse8601(self.safe_string_2(trade, 4, 'tradeTime'))
        cost = None
        if price is not None and amount is not None:
            cost = price * amount
        fee = None
        feeAmount = self.safe_float(trade, 'fee')
        # feeByConi = fill['feeByConi']
        if feeAmount is not None:
            fee = {
                'cost': feeAmount,
                'currency': self.safe_string(market, 'quote'),
                'rate': None,
            }
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'id': None,
            'order': None,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetAccountList(params)
        result = {'info': response}
        for i in range(0, len(response['data'])):
            balance = response['data'][i]
            currencyId = self.safe_string(balance, 'asset')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_float(balance, 'available')
            account['used'] = self.safe_float(balance, 'frozenBalance')
            account['total'] = self.safe_float(balance, 'totalBalance')
            result[code] = account
        return self.parse_balance(result)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        if not (type in self.options['orderTypes']):
            raise InvalidOrder(self.id + ' - invalid order type')
        request = {
            'symbol': market['slashedId'],
            'direction': self.options['direction'][side],
            'price': price,
            'quantity': amount,
            'orderType': self.options['orderTypes'][type],
            'notional': None,
        }
        response = self.privatePostOrderPlace(self.extend(request, params))
        result = {}
        result['id'] = response['data']['orderId']
        result['info'] = response['data']
        return result

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        response = self.privateGetOrderInfo(self.extend(request, params))
        return self.parse_order(response['data'])

    def cancel_order(self, id, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        response = self.privatePostOrderCancel(self.extend(request, params))
        return {
            'id' : id,
            'result': True,
        }

    def cancel_orders(self, ids, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderIds': ids,
        }
        response = self.privatePostOrderBatchCancel(self.extend(request, params))
        #  {
        #      "code":200,
        #      "data":[
        #          {
        #              "orderId":"1980983481458700288",
        #              "code":"200",
        #              "message":""
        #          },
        #          {
        #              "orderId":"1980983581337661440",
        #              "code":"200",
        #              "message":""
        #          },
        #          {
        #              "orderId":"1924511943331438592",
        #              "code":"3004",
        #              "message":"The order does not exist, the cancellation of failure"
        #          }
        #      ]
        #  }

    def parse_order_status(self, status):
        statuses = {
            'Open': 'open',
            'Filled': 'closed',
            'Cancelled': 'canceled',
            'Partially cancelled': 'canceled',  # partially filled and canceled
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'orderId')
        symbol = None
        base = self.safe_currency_code(self.safe_string(order, 'baseAsset'))
        quote = self.safe_currency_code(self.safe_string(order, 'quoteAsset'))
        marketId = self.safe_string(order, 'symbol')
        if base is not None and quote is not None:
            symbol = base + '/' + quote
            if symbol in self.markets:
                market = self.markets[symbol]
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
        if market is not None:
            symbol = market['symbol']
        type = self.safe_string(order, 'orderType')
        side = self.safe_string(order, 'orderDirection')
        filled = self.safe_float(order, 'filledQuantity')
        amount = self.safe_float(order, 'quantity')            # '0' for market order
        if type == 'market' and amount == 0:
            amount = filled
        remaining = None
        cost = self.safe_float(order, 'filledAmount')
        takerFee = self.safe_float(order, 'takerFeeRate')
        makerFee = self.safe_float(order, 'makerFeeRate')
        average = self.safe_float(order, 'avgPrice')         # '' always?
        price = self.safe_float(order, 'orderPrice')           # '0' for market order
        if not price:
           price = None
        if filled is not None:
            if cost is not None and average is None and filled > 0:
                average = cost / filled
            if cost is None:
                if average is not None:
                    cost = average * filled
                elif price is not None:
                    cost = price * filled
            if amount is not None:
                remaining = amount - filled
        status = self.parse_order_status(self.safe_string(order, 'orderStatus'))
        timestamp = self.parse8601(self.safe_string(order, 'orderTime'))
        fee = None
        feeAmount = self.safe_float_2(order, 'fee', 'totalFee')
        if feeAmount is not None:
            fee = {
                'cost': feeAmount,
                'currency': self.safe_string(market, 'quote'),
                'rate': None,
            }
        return {
            'info': order,
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': None,
        }

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['slashedId']
        if limit is not None:
            request['limit'] = limit
        response = self.privateGetOrderOpenorders(self.extend(request, params))
        orders = self.safe_value(response, 'data')
        if orders is None:
            return []
        return self.parse_orders(orders, market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['slashedId']
        if limit is not None:
            request['limit'] = limit
        response = self.privateGetOrderClosedorders(self.extend(request, params))
        orders = self.safe_value(response, 'data')
        if orders is None:
            return []
        return self.parse_orders(orders, market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        raise NotSupported(self.id + ' - fetchMyTrades is not supported yet')
        # params required: 'orderId'
        # self.load_markets()
        # response = self.privateGetOrderTradeFills(params)
        # code = response['code']
        # if code != 200:
        #     return response
        # }
        # trades = self.safe_value(response, 'data')
        # if trades is None:
        #     return []
        # }
       #  return self.parse_trades(trades, market, since, limit)

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        path = self.urls['prefixPath'] + path
        isArray = isinstance(params, list)
        # request = '/api/' + api + '/' + self.version + '/'
        request = path if isArray else self.implode_params(path, params)
        query = params if isArray else self.omit(params, self.extract_params(path))
        url = self.urls['api'] + request
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        if api == 'private':
            self.check_required_credentials()
            timestamp = self.iso8601(self.milliseconds())
            headers = {
                'ACCESS-KEY': self.apiKey,
                'ACCESS-TIMESTAMP': timestamp,
            }
            auth = timestamp + method + request
            if method == 'GET':
                if query: 
                    urlencodedQuery = '?' + self.urlencode(query)
                    url += urlencodedQuery
                    auth += urlencodedQuery
            else:
                if isArray or query:
                    body = self.json(query)
                    auth += body
                headers['Content-Type'] = 'application/json'
            signature = self.hmac(self.encode(auth), self.encode(self.secret))
            headers['ACCESS-SIGN'] = signature
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return
        if body[0] == '{':
            feedback = self.id + ' ' + body
            code2 = self.safe_string(response, 'code', '200')
            # message = self.safe_string_2(response, 'message', 'error')
            if code2 != '200':
                self.throw_exactly_matched_exception(self.exceptions, code2, feedback)
                raise ExchangeError(feedback)
            if code >= 400:
                raise ExchangeError(feedback)  # unknown message
