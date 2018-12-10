self.client_transactions = {

            'client-{}-portfolios'.format(self.client_1_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()) : {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['WPP_LondonStockEx_WPP']['identifiers']['LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 265600,
                        'transaction_price': 8.9100,
                        'transaction_currency': 'GBP',
                    }
                },
                'client-{}-strategy-tech'.format(self.client_1_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['MicroFocus_LondonStockEx_MCRO']['identifiers']['LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=5)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 15074,
                        'transaction_price': 13.2867,
                        'transaction_currency': 'GBP',
                    }
                }
            },

            'client-{}-portfolios'.format(self.client_2_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_2_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['Kingfisher_LondonStockEx_KGF']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=6)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 325000,
                        'transaction_price': 2.3450,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['UKGiltTreasury_4.5_2034']['identifiers']['LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 10501,
                        'transaction_price': 140.572,
                        'transaction_currency': 'GBP',
                    }
                },

                'client-{}-strategy-fixedincome'.format(self.client_2_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Buy',
                        'instrument_uid': self.instrument_universe['UKGiltTreasury_3.75_2021']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=3)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 24000,
                        'transaction_price': 109.126,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['USTreasury_2.00_2021']['identifiers']['LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=2)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 57000,
                        'transaction_price': 97.80,
                        'transaction_currency': 'USD',
                    }
                },
            },

            'client-{}-portfolios'.format(self.client_3_portfolio_group_id): {

                'client-{}-strategy-balanced'.format(self.client_3_portfolio_group_id): {
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['Whitebread_LondonStockEx_WTB']['identifiers'][
                            'LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=5)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 70000,
                        'transaction_price': 47.03,
                        'transaction_currency': 'GBP',
                    },
                    'tid_{}'.format(uuid.uuid4()): {
                        'type': 'Sell',
                        'instrument_uid': self.instrument_universe['TESCO_LondonStockEx_TSCO']['identifiers']['LUID'],
                        'transaction_date': (datetime.today() - timedelta(days=1) + timedelta(hours=9)).isoformat(),
                        'settlement_date': (datetime.today() - timedelta(days=1) + timedelta(days=2)).isoformat(),
                        'units': 342000,
                        'transaction_price': 1.8865,
                        'transaction_currency': 'GBP',
                    }
                },
            }
        }