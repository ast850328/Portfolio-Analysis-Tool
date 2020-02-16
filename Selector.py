import pandas as pd
class Selector:
    def __init__(self, number, target):
        self.number = number
        self.target = target
        if target == 'MDD':
            self.biggest = False
        else:
            self.biggest = True

    def select(self, df):
        df_result = self._cal_performance(df)
        if self.biggest:
            df_selected = df_result.nlargest(self.number, self.target)
        else:
            df_selected = df_result.nsmallest(self.number, self.target)
        selected_columns = df_selected.index.tolist()
        return selected_columns, df_selected

    def _cal_performance(self, df):
        # Equity, MDD, Equity/MDD, [MAR, CAGR]
        columns = df.columns.tolist()
        columns.remove('Date')
        data = {}

        for col in columns:
            df_col = df.loc[:, [col]]
            buy_price = df_col.iloc[0].values[0]
            sell_price = df_col.iloc[-1].values[0]
            equity = sell_price - buy_price
            MDD = 0
            peak = buy_price
            for index, row in df_col.iterrows():
                price = row[col]
                if price >= peak:
                    peak = price
                DD = price - peak
                if DD <= MDD:
                    MDD = DD
            MDD = 0 - MDD
            equity_to_MDD = equity / MDD

            data[col] = [equity, MDD, equity_to_MDD]
        df_result = pd.DataFrame(data=data, index=['Equity', 'MDD', 'Equity / MDD'])
        return df_result.T
