# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.hitbtc import hitbtc


class changellypro(hitbtc):

    def describe(self):
        return self.deep_extend(super(changellypro, self).describe(), {
            'id': 'changellypro',
            'name': 'changelly pro',
            'countries': ['KN'],
            'urls': {
                'logo': '',
                'api': {
                    'public': 'https://api.pro.changelly.com',
                    'private': 'https://api.pro.changelly.com',
                },
                'www': 'https://pro.changelly.com',
                'doc': 'https://api.pro.changelly.com',
                'fees': 'https://changelly.com/blog/changelly-pro-fee-structure/',
            },
            'fees': {
                'trading': {
                    'maker': 0.1 / 100,
                    'taker': 0.1 / 100,
                },
            },
        })