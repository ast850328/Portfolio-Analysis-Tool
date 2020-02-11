class Window:

    def __init__(self, df, weight_dict, assets):
        self.assets = assets
        self.df = df
        self.weight_dict = weight_dict
        self.results = []

    def cal_performance(self, df, weight, stock):
        data = {}
        assets = self.assets * weight
        buy_price = df[stock].iloc[0]
        sell_price = df[stock].iloc[-1]
        shares = math.floor(assets / buy_price)
        equity_change = sell_price - buy_price
        equity = equity_change * shares

        MDD = 0
        peak = buy_price
        for index, row in df.iterrows():
            price = row[stock]
            if price >= peak:
                peak = price
            DD = price - peak
            if DD <= MDD:
                MDD = DD
        MDD = MDD * shares

        data['stock'] = stock
        data['assets'] = assets
        data['weight'] = weight
        data['shares'] = shares
        data['equity_change'] = equity_change
        data['equity'] = equity
        data['MDD'] = MDD
#         data['Date'] = df.loc[start_t2, 'Date'] + '~' + df.loc[end_t2-1, 'Date']
        data['Date'] = df['Date'].iloc[-1]

        return data

    def get_results(self):
        return self.results

    def play_window(self):
        for stock in self.weight_dict:
            weight = self.weight_dict[stock]
            df = self.df_origin.loc[:, ['Date', stock]]
            data = self.cal_performance(df, weight, stock)
            self.results.append(data)
