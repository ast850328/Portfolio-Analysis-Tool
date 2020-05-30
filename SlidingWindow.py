import numpy as np
import pandas as pd
from Window import Window
class SlidingWindow:

    def __init__(self, config, investments, selector, model):
        self.config = config
        self.investments = investments
        self.selector = selector
        self.model = model
        self.df_windows = None


    def _cal_slidingWindow_performance(self, df):
        df = df.groupby('Start Date').sum()
        profit = df['Profit'].sum()
        MDD = df['MDD'].max()
        profit_to_MDD = profit / MDD

        original_assets = self.config['assets']
        final_assets = profit + original_assets
        days = (self.config['end_datetime'] - self.config['start_datetime']).astype('timedelta64[D]') / np.timedelta64(1, 'D')
        years = days / 365.0

        # 若有執行 reinvestment 就是 CAGR
        AR = pow(final_assets/original_assets, 1.0/years) - 1

        # MAR 單利公式 MAR = Profit / years / MDD
        MAR = profit / years / MDD

        MDD = MDD / original_assets
        # MAR 複利公式 MAR = CAGR / MDD
        # MAR = AR / MDD

        result = {
            'profit': profit,
            'profit_to_MDD': profit_to_MDD,
            'MDD': MDD,
            'AR': AR,
            'MAR': MAR
        }

        return result

    def play(self, t1, t2):
        # setting current_datetime index (ignore month testing)
        current_datetime = self.config['start_datetime'] + np.timedelta64(self.config['ignore_month'], 'M')
        # new 單一窗格
        window = Window(self.config, self.selector, self.model)
        # 窗格績效儲存欄位
        df_windows = pd.DataFrame(columns=['Start Date', 'End Date', 'Profit', 'MDD', 'Profit / MDD', 'Weight'])

        while True:
            # 設定 t1, t2 窗格的時間範圍
            t1_start_datetime = current_datetime
            t2_start_datetime = t1_end_datetime = t1_start_datetime + np.timedelta64(t1, 'M')
            t2_end_datetime = t2_start_datetime + np.timedelta64(t2, 'M')

            # 如果 t2 窗格結束時間已經超過回測時間，就結束窗格運算
            if t2_end_datetime > self.config['end_datetime']:
                break

            # 切割 t1 窗格資料
            t1_data = {}
            for name in self.investments:
                t1_data[name] = {
                    'symbol': self.investments[name]['symbol'],
                    'dailyProfit': None
                }
                df = self.investments[name]['dailyProfit']
                t1_data[name]['dailyProfit'] = df[(df.date >= t1_start_datetime) & (df.date < t1_end_datetime)]
                if t1_data[name]['dailyProfit'].empty:
                    del t1_data[name]

            # 將 t1 窗格資料丟入窗格進行 t1 窗格，找出投資組合成份及權重
            selected_investments = window.t1_play(t1_data, t1_start_datetime, t1_end_datetime)

            # 按照選取出來的投資成份，切割 t2 窗格資料
            t2_data = {}
            for name in selected_investments:
                t2_data[name] = {
                    'symbol': self.investments[name]['symbol'],
                    'dailyProfit': None
                }
                df = self.investments[name]['dailyProfit']
                t2_data[name]['dailyProfit'] = df[(df.date >= t2_start_datetime) & (df.date < t2_end_datetime)]

            # t2 窗格計算績效
            df_result = window.t2_play(t2_data, t2_start_datetime, t2_end_datetime)
            # 將此次窗個績效記錄下來
            df_windows = df_windows.append(df_result, ignore_index=True)
            # 移動至下一窗格
            current_datetime = current_datetime + np.timedelta64(t2, 'M')

        print(df_windows)
        self.df_windows = df_windows
        result = self._cal_slidingWindow_performance(df_windows)
        return result, df_windows
