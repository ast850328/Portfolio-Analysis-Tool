import numpy as np
import pandas as pd
from Window import Window
class SlidingWindow:

    def __init__(self, config, investments, selector, model):
        # config = {
        #     assets: 1000000000,
        #     commodity: {
        #         'commodity_name': { symbol, type, pricePerPoint, exchange },
        #     }
        # }
        self.config = config
        # investments = {
        #     'investment_name': {
        #         'symbol': 'TX',
        #         'dailyProfit': df_daily
        #     }
        # }
        self.investments = investments
        self.selector = selector
        self.model = model


    def _cal_slidingWindow_performance(self, df):
        df = df.groupby('Start Date').sum()
        profit = df['Profit'].sum()
        MDD = df['MDD'].max()
        profit_to_MDD = profit / MDD

        original_assets = self.config['assets']
        final_assets = profit + original_assets
        days = (self.config['end_datetime'] - self.config['start_datetime']).astype('timedelta64[D]') / np.timedelta64(1, 'D')
        years = days / 365.0

        CAGR = pow(final_assets/original_assets, 1.0/years) - 1
        MDD = MDD / original_assets
        MAR = CAGR / MDD
        print(df)
        result = {
            'profit': profit,
            'profit_to_MDD': profit_to_MDD,
            'MDD': MDD,
            'CAGR': CAGR,
            'MAR': MAR
        }

        return result

    def play(self, t1, t2):

        # current_datetime index
        # first month testing
        current_datetime = self.config['start_datetime'] + np.timedelta64(1, 'M')
        window = Window(self.config, self.selector, self.model)
        df_windows = pd.DataFrame(columns=['Start Date', 'End Date', 'Profit', 'MDD', 'Profit / MDD', 'Weight'])
        i = 0
        while True:
            # set t1, t2 datetime
            t1_start_datetime = current_datetime
            t2_start_datetime = t1_end_datetime = t1_start_datetime + np.timedelta64(t1, 'M')
            t2_end_datetime = t2_start_datetime + np.timedelta64(t2, 'M')
            if t2_end_datetime > self.config['end_datetime']:
                break

            # split t1_data
            t1_data = {}
            for name in self.investments:
                t1_data[name] = {
                    'symbol': self.investments[name]['symbol'],
                    'dailyProfit': None
                }
                df = self.investments[name]['dailyProfit']
                t1_data[name]['dailyProfit'] = df[(df.date >= t1_start_datetime) & (df.date < t1_end_datetime)]

            selected_investments = window.t1_play(t1_data, t1_start_datetime, t1_end_datetime)

            t2_data = {}
            for name in selected_investments:
                t2_data[name] = {
                    'symbol': self.investments[name]['symbol'],
                    'dailyProfit': None
                }
                df = self.investments[name]['dailyProfit']
                t2_data[name]['dailyProfit'] = df[(df.date >= t2_start_datetime) & (df.date < t2_end_datetime)]

            df_result = window.t2_play(t2_data, t2_start_datetime, t2_end_datetime)
            df_windows = df_windows.append(df_result, ignore_index=True)

            current_datetime = current_datetime + np.timedelta64(t2, 'M')

        print(df_windows)
        result = self._cal_slidingWindow_performance(df_windows)
        return result
