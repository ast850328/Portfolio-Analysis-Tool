import math
import pandas as pd
import numpy as np
class Window:

    def __init__(self, config, selector, model):
        self.config = config
        self.selector = selector
        self.model = model
        self.weight_dict = {}

    def _get_lastest_K(self, date, df):
        row = df[df['Date'] <= date].tail(1)
        return row

    def _cal_window_performance(self, data, t2_start_datetime, t2_end_datetime):
        commodity = self.config['commodity']

        result_data = {}
        # 計算每個投資的績效
        for key in data:
            assets = self.config['assets'] * self.weight_dict[key]
            symbol = data[key]['symbol']
            commodity_type = commodity[symbol]['type']
            price_per_point = commodity[symbol]['pricePerPoint']
            df_dailyProfit = data[key]['dailyProfit']
            df_price = commodity[symbol]['priceData']
            buy_date = df_dailyProfit.iloc[0].date
            lastest_K = self._get_lastest_K(buy_date, df_price)

            # 若投資商品為期貨或是使用 Equal Risk 權重配置模型
            # 則使用風險平價公式計算部位 (資金 * 風險比率) / (ATR * 大點金額)
            if commodity_type == 'Future' or self.model.model_name == 'EqualRisk':
                volatility = df_dailyProfit.iloc[0].volatility
                units = math.floor((assets * self.model.config['risk']) / (volatility * price_per_point))
            # 其餘情況則使用一般股票方式買入商品
            else:
                buy_price = lastest_K.Open
                units = math.floor(assets / buy_price)

            # 獲利為該區間的每日賺賠績效總和 乘上 購買單位
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

            result_data[key] = [t2_start_datetime, t2_end_datetime, profit, MDD, profit_to_MDD, self.weight_dict[key], symbol]
        df_result = pd.DataFrame(data=result_data, index=['Start Date', 'End Date', 'Profit', 'MDD', 'Profit / MDD', 'Weight', 'Symbol']).T
        return df_result

    def t1_play(self, t1_data, t1_start_datetime, t1_end_datetime):
        # 經由績效排名指標，選取出前幾名的投資作為投資組合成份
        selected_investments = self.selector.select(t1_data, self.config['commodity'], self.config['assets'], t1_start_datetime, t1_end_datetime)

        # 統一每個投資的每日賺賠天數
        t1_end_datetime = t1_end_datetime - np.timedelta64(1, 'D')
        idx = pd.bdate_range(start=t1_start_datetime, end=t1_end_datetime)
        data = []
        for name in selected_investments.keys():
            investment = selected_investments[name]
            symbol = investment['symbol']
            pricePerPoint =  float(self.config['commodity'][symbol]['pricePerPoint'])
            df = investment['dailyProfit']
            df.index = df.date
            df = df.drop(columns=['volatility', 'date'])
            df = df.reindex(idx, fill_value=0)
            df['return'] = df['return'] / pricePerPoint
            df = df.rename(columns={'return': name})
            data.append(df)
        data = pd.concat(data, axis=1)

        # 將整理好的投資組合成份，丟入權重配置模型分配權重，並記錄下來
        self.weight_dict = self.model.get_weight(data)

        return selected_investments

    def t2_play(self, t2_data, t2_start_datetime, t2_end_datetime):
        # 計算 t2 窗格的績效
        df_result = self._cal_window_performance(t2_data, t2_start_datetime, t2_end_datetime)
        return df_result
