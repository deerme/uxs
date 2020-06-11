# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import base64
from ccxt.base.errors import AuthenticationError


class tradeogre(Exchange):

    def describe(self):
        return self.deep_extend(super(tradeogre, self).describe(), {
            'id': 'tradeogre',
            'name': 'Trade Ogre',
            'has': {
                'loadMarkets': True,
                'fetchMarkets': True,
                'fetchCurrencies': True,
                'fetchTicker': True,
                'fetchTickers': False,
                'fetchOrderBook': False,
                'fetchL2OrderBook': False,
                'fetchOHLCV': False,
                'fetchTrades': False,
                'fetchBalance': True,
                'createOrder': False,
                'cancelOrder': False,
                'fetchOrder': False,
                'fetchOrders': False,
                'fetchOpenOrders': False,
                'fetchClosedOrders': False,
                'fetchMyTrades': False,
                'deposit': False,
                'withdraw': False,
            },
            'urls': {
                'logo': 'https://tradeogre.com/img/logo.png',
                'api': {
                    'web': 'https://tradeogre.com',
                    'public': 'https://tradeogre.com/api/v1',
                    'private': 'https://tradeogre.com/api/v1',
                },
                'www': 'https://tradeogre.com',
                'doc': 'https://tradeogre.com/help/api',
                'fees': [
                    'https://tradeogre.com/help/fees',
                ],
            },
            'api': {
                'public': {
                    'get': [
                        'markets',
                        'orders',
                        'ticker',
                        'history',
                    ],
                },
                'private': {
                    'get': [
                        'account/order',
                        'account/balances',
                    ],
                    'post': [
                        'order/buy',
                        'order/sell',
                        'order/cancel',
                        'account/orders',
                        'account/balance',
                    ],
                },
            },
        })

    def fetch_markets(self, params={}):
        response = self.publicGetMarkets(params)
        result = []
        for i in range(0, len(response)):
            market = response[i]
            keys = list(market.keys())
            id = keys[0]
            quoteId, baseId = id.split('-')
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            entry = {
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'precision': {
                    'price': 8,
                    'amount': None,
                    'cost': None,
                },
                'limits': {
                    'amount': {
                        'min': None,
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
                'info': market,
            }
            result.append(entry)
        return result

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetAccountBalances(params)
        if not response['success'] and response['error'] == 'Must be authorized':
            raise AuthenticationError('fetchBalance could not be authorized')
        result = {'info': response}
        balances = response['balances']
        currencies = list(balances.keys())
        for i in range(0, len(currencies)):
            currency = currencies[i]
            balance = balances[currency]
            if currency in self.currencies_by_id:
                currency = self.currencies_by_id[currency]['code']
            account = {
                'free': None,
                'used': None,
                'total': balance,
            }
            result[currency] = account
        return self.parse_balance(result)

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        response = self.publicGetTicker(self.extend({
            'symbol': market['id'],
        }, params))
        response['symbol'] = symbol
        return self.parse_ticker(response, market)

    def parse_ticker(self, ticker, market=None):
        return {
            'symbol': ticker['symbol'],
            'timestamp': None,
            'datetime': None,
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': None,
            'last': None,
            'previousClose': self.safe_float(ticker, 'initialprice'),
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'volume'),
            'quoteVolume': None,
            'info': ticker,
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api]
        if api == 'private':
            self.check_required_credentials()
            auth = self.encode(self.apiKey + ':' + self.secret)
            auth = base64.b64encode(auth)
            headers = {'Authorization': 'Basic ' + self.decode(auth)}
        url += '/' + path
        if path == 'ticker' and method == 'GET':
            url += '/' + params['symbol']
        return {'url': url, 'method': method, 'body': body, 'headers': headers}