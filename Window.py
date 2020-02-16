import math
import pandas as pd
class Window:

    def __init__(self, df_t1, df_t2, selector, model, assets):
        self.df_t1 = df_t1
        self.df_t2 = df_t2
        self.selector = selector
        self.model = model
        self.assets = assets

    def _cal_performance(self, df, weight_dict):

        stocks = weight_dict.keys()
        data = {}
        for stock in stocks:
            df_stock = df.loc[:, [stock]]

            weight = weight_dict[stock]
            assets = self.assets * weight
            buy_price = df_stock.iloc[0].values[0]
            sell_price = df_stock.iloc[-1].values[0]
            shares = math.floor(assets / buy_price)
            equity_change = sell_price - buy_price
            equity = equity_change * shares
            MDD = 0
            peak = buy_price
            for index, row in df_stock.iterrows():
                price = row[stock]
                if price >= peak:
                    peak = price
                DD = price - peak
                if DD <= MDD:
                    MDD = DD
            MDD = 0 - MDD
            MDD = MDD * shares
            equity_to_MDD = equity / MDD
            data[stock] = [assets, weight, shares, equity_change, equity, MDD, equity_to_MDD]

        df_result = pd.DataFrame(data=data, index=['Assets', 'Weight', 'Shares', 'Equity Change', 'Equity', 'MDD', 'Equity / MDD'])
        date = df['Date'].iloc[-1]

        return df_result.T, date

    def play(self):
        selected_stocks, df_selected = self.selector.select(self.df_t1)
        df_t1 = self.df_t1.loc[:, selected_stocks]
        weight_dict = self.model.get_weight(df_t1)
        selected_stocks.append('Date')
        cols = selected_stocks
        df_t2 = self.df_t2.loc[:, cols]
        df_result, date = self._cal_performance(df_t2, weight_dict)
        return df_result, date
