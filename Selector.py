import math
import pandas as pd
import numpy as np
class Selector:

    def __init__(self, number, basis):
        self.number = number
        self.basis = basis

    def select(self, data, commodity, assets, t1_start_datetime, t1_end_datetime):
        # print(t1_start_datetime)
        if self.number == 'All':
            selected_investments = list(data.keys())
        else:
            days = (t1_end_datetime - t1_start_datetime).astype('timedelta64[D]') / np.timedelta64(1, 'D')
            df_result = self._cal_window_performance(data, commodity, assets, days)
            df_result = df_result.nlargest(self.number, self.basis)
            selected_names = df_result.index.tolist()
            selected_investments = {}
            for name in selected_names:
                selected_investments[name] = data[name]
        return selected_investments

    def _cal_window_performance(self, data, commodity, assets, days):
        # Equity, Equity/MDD, MAR, AR
        result_data = {}
        for key in data:
            symbol = data[key]['symbol']
            df_dailyProfit = data[key]['dailyProfit']
            commodity_type = commodity[symbol]['type']
            price_per_point = commodity[symbol]['pricePerPoint']
            df_price = commodity[symbol]['priceData']
            buy_date = df_dailyProfit.iloc[0].date
            lastest_K = self._get_lastest_K(buy_date, df_price)

            if commodity_type == 'Future':
                # (資金 * 風險比率) / (ATR * 大點金額)
                # risk 0.7%
                volatility = df_dailyProfit.iloc[0].volatility
                units = math.floor((assets * 0.007) / (volatility * price_per_point))
            else:
                buy_price = lastest_K.Open
                units = math.floor(assets / buy_price)

            profit = df_dailyProfit['return'].sum() * units

            MDD = 0
            peak = df_dailyProfit.iloc[0]['return']
            for index, row in df_dailyProfit.iterrows():
                if row['return'] >= peak:
                    peak = row['return']
                DD = peak - row['return']
                if DD >= MDD:
                    MDD = DD
            MDD = MDD * units

            profit_to_MDD = profit / MDD

            original_assets = assets
            final_assets = profit + original_assets
            years = days / 365.0

            AR = pow(final_assets/original_assets, 1.0/years) - 1
            MDD = MDD / original_assets
            MAR = AR / MDD

            result_data[key] = [profit, profit_to_MDD, AR, MAR]
        df_result = pd.DataFrame(data=result_data, index=['Profit', 'Profit / MDD', 'AR', 'MAR']).T
        return df_result

    def _get_lastest_K(self, date, df):
        row = df[df['Date'] <= date].tail(1)
        return row
