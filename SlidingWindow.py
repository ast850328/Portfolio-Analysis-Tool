from Window import Window
class SlidingWindow:
    def __init__(self, t1, t2, df, assets, selector, model):
        self.t1 = t1
        self.t2 = t2
        self.df = df
        self.assets = assets
        self.selector = selector
        self.model = model

    def _cal_performance(self, data, start, end):
        dates = data.keys()
        total_equity = 0
        max_MDD = -1
        for date in dates:
            df = data[date]
            total_equity += df['Equity'].sum()
            MDD = df['MDD'].max()
            if MDD > max_MDD:
                max_MDD = MDD
        original_assets = self.assets
        final_assets = total_equity + original_assets
        years = (end - start) / 365.0

        CAGR = pow(final_assets/original_assets, 1.0/years) - 1
        MDD = max_MDD / original_assets
        MAR = CAGR / max_MDD
        return total_equity, max_MDD, CAGR, MAR

    def play(self):
        # 20 days a month
        t1_start = 0
        length = len(self.df.index)
        start = t1_start + self.t1 * 20
        end = 0
        data = {}

        while t1_start < length:

            t1_end = t1_start + self.t1 * 20
            t2_start = t1_end
            t2_end = t2_start + self.t2 * 20
            # print(t1_start, t1_end)
            # print(t2_start, t2_end)
            if t2_end >= length:
                break
            df_t1 = self.df.iloc[t1_start: t1_end]
            df_t2 = self.df.iloc[t2_start: t2_end]
            window = Window(df_t1, df_t2, self.selector, self.model, self.assets)
            df_result, date = window.play()
            # print(date)
            # print(df_result)
            data[date] = df_result
            end = t2_end
            t1_start = t1_start + self.t2 * 20
        total_equity, max_MDD, CAGR, MAR = self._cal_performance(data, start, end)
        return total_equity, max_MDD, CAGR, MAR, data
