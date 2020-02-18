from Window import Window
class SlidingWindow:
    def __init__(self, df, assets, selector, model):
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

    def play(self, t1, t2):
        # 20 days a month
        t1_start = 0
        length = len(self.df.index)
        start = t1_start + t1 * 20
        end = 0
        data = {}
        window = Window(self.assets, self.selector, self.model)
        while t1_start < length:

            t1_end = t1_start + t1 * 20
            t2_start = t1_end
            t2_end = t2_start + t2 * 20
            if t2_end >= length:
                break
            df_t1 = self.df.iloc[t1_start: t1_end]
            df_t2 = self.df.iloc[t2_start: t2_end]
            df_result, date = window.play(df_t1, df_t2)
            data[date] = df_result
            end = t2_end
            t1_start = t1_start + t2 * 20
        total_equity, max_MDD, CAGR, MAR = self._cal_performance(data, start, end)
        return total_equity, max_MDD, CAGR, MAR, data
