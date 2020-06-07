import sys
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.axes
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from datetime import datetime
from Selector import Selector
from model.CLA import CLA
from model.HRP import HRP
from model.OptimalF import OptimalF
from model.EqualRisk import EqualRisk
from model.EqualWeight import EqualWeight
from SlidingWindow import SlidingWindow
from Ui_MainWindow import Ui_MainWindow
from Ui_ConfigDialog import Ui_ConfigDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget, QTableWidgetItem

class WindowThread(QtCore.QThread):

    def __init__(self, sliding_window, t1_start, t1_end, t2_start, t2_end):
        QtCore.QThread.__init__(self)
        self.sliding_window = sliding_window
        self.t1_start = t1_start
        self.t1_end = t1_end
        self.t2_start = t2_start
        self.t2_end = t2_end
    # 設定 signal 的變數
    save_df_result_signal = QtCore.pyqtSignal(pd.DataFrame)
    result_table_signal = QtCore.pyqtSignal(dict)
    result_testBrowser_signal = QtCore.pyqtSignal(str)
    destroy_signal = QtCore.pyqtSignal()
    progressBar_signal = QtCore.pyqtSignal(int)

    def run(self):
        self.result_testBrowser_signal.emit('Start running sliding window...')
        self.progressBar_signal.emit(0)
        df_result = pd.DataFrame(columns=["t1", "t2", "profit", "profit_to_MDD", "MDD", "AR", "MAR"])
        t1_start = self.t1_start
        t1_end = self.t1_end
        t2_start = self.t2_start
        t2_end = self.t2_end
        # 計算進度條的總長度
        total = (t1_end-t1_start+1) * (t2_end-t2_start+1)
        count = 0
        sliding_window = self.sliding_window
        for i in range(t1_start, t1_end+1):
            for j in range(t2_start, t2_end+1):
                self.result_testBrowser_signal.emit('({0}, {1})'.format(i, j))
                result, df_windows = sliding_window.play(i, j)
                print(result)
                data = {
                    "t1": i,
                    "t2": j,
                    "profit": result['profit'],
                    "profit_to_MDD": result['profit_to_MDD'],
                    "MDD": result['MDD'],
                    "AR": result['AR'],
                    "MAR": result['MAR'],
                }
                df_result = df_result.append(data, ignore_index=True)
                result_string = "Profit: {0}, MDD: {1}, Profit / MDD: {2}, AR: {3}, MAR: {4}".format(
                    result['profit'], result['MDD'], result['profit_to_MDD'], result['AR'], result['MAR']
                )
                # 藉由 signal 將資料傳去前台顯示出來
                self.result_testBrowser_signal.emit(result_string)
                self.result_testBrowser_signal.emit("====================================================")
                self.result_table_signal.emit(data)
                count += 1
                self.progressBar_signal.emit(int(count * (100 / total)))
        self.result_testBrowser_signal.emit('Done')
        self.progressBar_signal.emit(100)
        self.save_df_result_signal.emit(df_result)
        self.destroy_signal.emit()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 繪製 GUI 畫面
        self.setupUi(self)
        self.clear_ui()
        # 將物件 bind 事件
        self.bind_init_event()
        # 需要儲存的參數
        self.investments_file_path = None
        self.model_config = None
        self.windowThread = None
        self.df_result = None

    def clear_ui(self):
        self.investments_table.setRowCount(0)
        self.result_table.setRowCount(0)
        self.result_textBrowser.clear()
        self.assets_text.clear()
        self.start_year_text.clear()
        self.start_month_text.clear()
        self.end_year_text.clear()
        self.end_month_text.clear()
        self.ignore_month_text.clear()
        self.ranking_box.clear()
        self.ranking_box.addItems(['All'])
        self.t1_start_text.clear()
        self.t1_end_text.clear()
        self.t2_start_text.clear()
        self.t2_end_text.clear()
        self.progress_bar.setValue(0)

    def bind_init_event(self):
        self.assets_text.installEventFilter(self)
        self.action_import_investments.triggered.connect(self.import_investments)
        self.action_import_config.triggered.connect(self.import_config)
        self.action_import_result.triggered.connect(self.import_result)
        self.action_save_config.triggered.connect(self.save_config)
        self.action_save_result.triggered.connect(self.save_result)
        self.action_plot_result.triggered.connect(self.plot_result)
        # self.action_plot_window.triggered.connect(self.plot_test)
        self.ranking_box.currentTextChanged.connect(self.set_basis_box)
        self.config_button.clicked.connect(self.set_model_config)
        self.play_button.clicked.connect(self.play)
        self.clear_button.clicked.connect(self.clear_ui)

    def eventFilter(self, obj, event):
        if obj == self.assets_text:
            if event.type() == QtCore.QEvent.KeyRelease:
                text = self.assets_text.text()
                if text is '':
                    return False
                else:
                    dollarText = self.format_dollar(text)
                    self.assets_text.setText(dollarText)
                    return False
            else:
                return False
        else:
            return QWidget.eventFilter(self, obj, event)

    def format_dollar(self, text):
        # 金錢表示型態
        text = text.replace(',', '')
        dollarText = '{:,}'.format(int(text))
        return dollarText

    def import_investments(self):
        # 透過 get_files_path() 取得匯入資料的路徑
        files_path = self.get_files_path()
        if files_path != None:
            # 將路徑存下來
            self.investments_file_path = files_path
            filenames = [path[path.rfind('/')+1: -4] for path in files_path]
            # 更新投資列表
            self.set_investments_table(filenames)
            # 更新績效排名指標的選取數量
            self.set_ranking_box(len(filenames))
        else:
            return False

    def get_files_path(self):
        # 建立 PyQt 選取檔案的視窗
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)
        # 等視窗關閉
        if dlg.exec_():
            files_path = dlg.selectedFiles()
            return files_path

    def set_investments_table(self, filenames):
        # 清除所有 row
        self.investments_table.setRowCount(0)
        # 將每一個投資更新進去投資列表
        for name in filenames:
            self.insert_investment_row(name)

    def insert_investment_row(self, name):
        # 先取得目前可以 insert row 的 index
        row_position = self.investments_table.rowCount()
        self.investments_table.insertRow(row_position)
        # 設定每一條 row 的 items
        # 投資名稱
        name_item = QTableWidgetItem(name)
        name_item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.investments_table.setItem(row_position, 0, name_item)
        # 投資種類
        type_combo_box = QtWidgets.QComboBox()
        type_combo_box_options = ['Stock', 'ETF', 'Future']
        for t in type_combo_box_options:
            type_combo_box.addItem(t)
        # 更換種類時，要更換商品代碼(symbol)的列表
        type_combo_box.currentTextChanged.connect(self.set_symbols)
        self.investments_table.setCellWidget(row_position, 1, type_combo_box)
        # 商品代碼列表
        ticker_symbol_combo_box = QtWidgets.QComboBox()
        ticker_symbol_combo_box_options = self.get_ticker_symbols(type_combo_box_options[0])
        for t in ticker_symbol_combo_box_options:
            ticker_symbol_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 2, ticker_symbol_combo_box)
        # 投資績效檔案的最小單位
        unit_combo_box = QtWidgets.QComboBox()
        unit_combo_box_options = ['share', 'lot']
        for t in unit_combo_box_options:
            unit_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 3, unit_combo_box)

    def set_symbols(self, text):
        # 先取得是哪一列投資項目
        sender = self.sender()
        point = sender.pos()
        row = int(point.y() / 30)
        # 將該類投資的商品代碼更新
        ticker_symbol_combo_box = QtWidgets.QComboBox()
        ticker_symbol_combo_box_options = self.get_ticker_symbols(text)
        for t in ticker_symbol_combo_box_options:
            ticker_symbol_combo_box.addItem(t)
        self.investments_table.setCellWidget(row, 2, ticker_symbol_combo_box)

    def get_ticker_symbols(self, type):
        path = './symbols/' + str(type)
        files = [f[:-4] for f in listdir(path) if isfile(join(path, f)) and f[-3:] == 'csv']
        return files

    def import_config(self):
        self.set_result_textBrowser("Importing config file....")
        file_path = self.get_files_path()
        if file_path != None:
            # 只取一個檔案的路徑
            file_path = file_path[0]
            # 讀入 json 檔
            with open(file_path) as json_file:
                data = json.load(json_file)
                print(data)
                # 設定參數
                self.set_config(data)
            self.set_result_textBrowser("Done.")
        else:
            self.set_result_textBrowser("Canceled.")   

    def set_config(self, data):
        # 將每個參數欄位直接設定
        self.assets_text.setText(data['assets'])
        self.ignore_month_text.setText(data['ignore_month'])
        self.start_year_text.setText(data['start_year'])
        self.start_month_text.setText(data['start_month'])
        self.end_year_text.setText(data['end_year'])
        self.end_month_text.setText(data['end_month'])
        index = self.ranking_box.findText(data['ranking'], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ranking_box.setCurrentIndex(index)
        index = self.basis_box.findText(data['basis'], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.basis_box.setCurrentIndex(index)
        index = self.model_box.findText(data['model_name'], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.model_box.setCurrentIndex(index)
        self.model_config = data['model_config']
        self.t1_start_text.setText(data['t1_start'])
        self.t1_end_text.setText(data['t1_end'])
        self.t2_start_text.setText(data['t2_start'])
        self.t2_end_text.setText(data['t2_end'])

    def import_result(self):
        self.set_result_textBrowser("Importing result file....")
        file_path = self.get_files_path()
        if file_path != None:
            # 只取一個檔案路徑
            file_path = file_path[0]
            # 用 pandas 讀入窗格績效並儲存起來
            self.df_result = pd.read_csv(file_path)
            # 更新 result table
            self.set_result_table()
            # 輸出最佳窗格績效訊息
            self.print_result_info()
            self.set_result_textBrowser("Done.")
        else:
            self.set_result_textBrowser("Canceled.")

    def set_result_table(self):
        if self.df_result is not None:
            self.result_table.setRowCount(0)
            for index, row in self.df_result.iterrows():
                row_position = self.result_table.rowCount()
                self.result_table.insertRow(row_position)
                self.result_table.setItem(row_position , 0, QTableWidgetItem(str(int(row['t1']))))
                self.result_table.setItem(row_position , 1, QTableWidgetItem(str(int(row['t2']))))
                self.result_table.setItem(row_position , 2, QTableWidgetItem(str(row['profit'])))
                self.result_table.setItem(row_position , 3, QTableWidgetItem(str(row['MDD'])))
                self.result_table.setItem(row_position , 4, QTableWidgetItem(str(row['profit_to_MDD'])))
                self.result_table.setItem(row_position , 5, QTableWidgetItem(str(row['AR'])))
                self.result_table.setItem(row_position , 6, QTableWidgetItem(str(row['MAR'])))

    def save_config(self):
        self.set_result_textBrowser("Saving config file....")
        # 透過儲存視窗，獲得要儲存的位置及檔案名稱
        name = QFileDialog.getSaveFileName(self, 'Save Config File')[0]
        if name is not None:
            data = self.get_input_data()
            data["model_config"] = self.model_config
            with open(name, 'w') as file:
                file.write(json.dumps(data))
        else:
            self.set_result_textBrowser("Canceled.")

    def save_result(self):
        self.set_result_textBrowser("Saving result file....")
        # 透過儲存視窗，獲得要儲存的位置及檔案名稱
        name = QFileDialog.getSaveFileName(self, 'Save Result File')[0]
        if name is not None:
            self.df_result.to_csv(name, index=False)
        else:
            self.set_result_textBrowser("Canceled.")
    def plot_result(self):
        df = self.df_result
        # 先透過 df_result 取得 t1 t2 開始與結束
        t1_start = int(df.iloc[0]["t1"])
        t2_start = int(df.iloc[0]["t2"])
        t1_end = int(df.iloc[-1]["t1"])
        t2_end = int(df.iloc[-1]["t2"])
        titles = ['profit', 'profit_to_MDD', 'AR', 'MAR']
        # 建立符合窗格大小的績效 dataframe
        df_slidingWindow = pd.DataFrame(columns=range(t1_start, t1_end+1), index=range(t2_start, t2_end+1))
        for title in titles:
            for index, row in df.iterrows():
                df_slidingWindow.loc[int(row["t2"]), int(row["t1"])] = row[title]
            df_slidingWindow = df_slidingWindow.astype(float)
            fig, ax = plt.subplots(figsize=(15,10))
            fig.canvas.set_window_title(title)
            ax.set_title(title)
            ax = sns.heatmap(df_slidingWindow, xticklabels=True, yticklabels=True, cmap='gray_r')
            plt.xlabel('T1')
            plt.ylabel('T2')
            plt.show()

    def set_ranking_box(self, number):
        # 根據傳入的數量，設定排名可選取的數量
        self.ranking_box.clear()
        items = [str(x) for x in range(1, number)]
        items.insert(0, 'All')
        self.ranking_box.addItems(items)

    def set_basis_box(self):
        # 根據所選的排名數量，開放設定績效指標
        ranking = self.ranking_box.currentText()
        if ranking == 'All':
            self.basis_box.setEnabled(False)
        else:
            self.basis_box.setEnabled(True)

    def set_model_config(self):
        # 先拿到目前選定的 model 名稱
        model_name = self.model_box.currentText()
        # 根據 ConfigDialog 建立對話視窗
        dialog = QtWidgets.QDialog()
        ui = Ui_ConfigDialog()
        ui.setupUi(dialog)
        # 在 Ui_ConfigDialog.py 裡面
        ui.set_model_label(model_name)
        ui.limit_column(model_name)
        res = dialog.exec_()
        # 當點選確定，則發送 signal 到這裡的 slot 接應
        if res == QtWidgets.QDialog.Accepted:
            print('accept')
            self.model_config = ui.get_model_config()
        else:
            print('cancel')

    def play(self):
        # 先讀入所有商品的設定檔
        all_commodity = self.read_all_commodity()
        # 從投資列表取得所有匯入的投資以及其商品資料設定
        investments, commodity = self.get_investments(all_commodity)
        # 去拿所有設定欄位的 input 資料
        data = self.get_input_data()
        # 將資料做一些處理
        # 把金錢表示型態變成整數
        data['assets'] = int(self.assets_text.text().replace(',', ''))
        # 以時間格式儲存回測起訖時間
        start_datetime = np.datetime64(data['start_year'] + '-' + data['start_month'])
        end_datetime = np.datetime64(data['end_year'] + '-' + data['end_month'])
        # 包成 dict 的投資組合設定
        config_portfolio = {
            'assets': data['assets'],
            'start_datetime': start_datetime,
            'end_datetime': end_datetime,
            'ignore_month': data['ignore_month'],
            'commodity': commodity
        }
        # 建立績效排名指標的物件
        selector = self.generate_selector(data['ranking'], data['basis'])
        # 根據所選取的權重配置模型以及其模型參數，建立權重配置模型的物件
        model_config = self.model_config
        model = self.generate_model(data['model_name'], model_config)
        # 將窗格大小範圍轉成 int
        t1_start = int(data['t1_start'])
        t1_end = int(data['t1_end'])
        t2_start = int(data['t2_start'])
        t2_end = int(data['t2_end'])

        print(investments)
        print(config_portfolio)
        # 清除目前的 result table
        self.result_table.setRowCount(0)
        # 建立移動窗格物件
        sliding_window = SlidingWindow(config_portfolio, investments, selector, model)
        # 建立窗格運算的 Thread，並丟入移動窗格物件
        self.windowThread = WindowThread(sliding_window, t1_start, t1_end, t2_start, t2_end)
        # 將 QThread 的 signal 綁定 function
        self.windowThread.result_table_signal.connect(self.insert_result_table)
        self.windowThread.result_testBrowser_signal.connect(self.set_result_textBrowser)
        self.windowThread.destroy_signal.connect(self.destroy_windowThread)
        self.windowThread.progressBar_signal.connect(self.set_progressBar)
        self.windowThread.save_df_result_signal.connect(self.save_df_result)
        # 開始在後台進行移動窗格運算，跑 WindowThread 的 run
        self.windowThread.start()

    def get_input_data(self):
        data = {}

        data['assets'] = self.assets_text.text()
        data['ignore_month'] = self.ignore_month_text.text()
        data['start_year'] = self.start_year_text.text()
        data['start_month'] = self.start_month_text.text().zfill(2)
        data['end_year'] = self.end_year_text.text()
        data['end_month'] = self.end_month_text.text().zfill(2)

        data['ranking'] = self.ranking_box.currentText()
        data['basis'] = self.basis_box.currentText()

        data['model_name'] = self.model_box.currentText()

        data['t1_start'] = self.t1_start_text.text()
        data['t1_end'] = self.t1_end_text.text()
        data['t2_start'] = self.t2_start_text.text()
        data['t2_end'] = self.t2_end_text.text()
        print(data)

        return data

    def generate_model(self, model_name, config=None):
        model = None
        if model_name == 'CLA':
            model = CLA(config)
        elif model_name == 'HRP':
            model = HRP(config)
        elif model_name == 'Optimal F':
            model = OptimalF(config)
        elif model_name == 'Equal Weight':
            model = EqualWeight(config)
        elif model_name == 'Equal Risk':
            model = EqualRisk(config)
        return model

    def generate_selector(self, number, basis):
        selector = Selector(number, basis)
        return selector

    def read_all_commodity(self):
        all_commodity = pd.read_csv('./commodity.csv')
        all_commodity = all_commodity.set_index('symbol')
        all_commodity = all_commodity.to_dict('index')
        return all_commodity

    def get_investments(self, all_commodity):
        commodity = {}
        investments = {}
        rows = self.investments_table.rowCount()
        for row in range(0, rows):
            investment_name = self.investments_table.item(row, 0).text()
            investment_type = self.investments_table.cellWidget(row, 1).currentText()
            investment_symbol = self.investments_table.cellWidget(row, 2).currentText()
            investment_unit = self.investments_table.cellWidget(row, 3).currentText()

            if investment_symbol not in commodity:
                commodity[investment_symbol] = all_commodity[investment_symbol]
                df = pd.read_csv('./symbols/' + investment_type + '/' + investment_symbol + '.csv')
                df.Date = pd.to_datetime(df.Date, format='%Y/%m/%d')
                df.Open = df.Open * float(commodity[investment_symbol]['exchange'])
                commodity[investment_symbol]['priceData'] = df

            investment_path = self.investments_file_path[row]
            df = pd.read_csv(investment_path)
            df['date'] = pd.to_datetime(df.date, format='%Y/%m/%d')
            df['return'] = df['return'] * float(commodity[investment_symbol]['exchange'])
            df['volatility'] = df['volatility'] * float(commodity[investment_symbol]['exchange'])

            investments[investment_name] = {
                'type': investment_type,
                'symbol': investment_symbol,
                'unit': investment_unit,
                'dailyProfit': df
            }
        return investments, commodity

    @QtCore.pyqtSlot(dict)
    def insert_result_table(self, data):
        row_position = self.result_table.rowCount()
        self.result_table.insertRow(row_position)
        self.result_table.setItem(row_position , 0, QTableWidgetItem(str(data['t1'])))
        self.result_table.setItem(row_position , 1, QTableWidgetItem(str(data['t2'])))
        self.result_table.setItem(row_position , 2, QTableWidgetItem(str(data['profit'])))
        self.result_table.setItem(row_position , 3, QTableWidgetItem(str(data['MDD'])))
        self.result_table.setItem(row_position , 4, QTableWidgetItem(str(data['profit_to_MDD'])))
        self.result_table.setItem(row_position , 5, QTableWidgetItem(str(data['AR'])))
        self.result_table.setItem(row_position , 6, QTableWidgetItem(str(data['MAR'])))

    @QtCore.pyqtSlot(str)
    def set_result_textBrowser(self, text):
        # 將某一串文字新增進 textBrowser
        self.result_textBrowser.append(text)

    @QtCore.pyqtSlot()
    def destroy_windowThread(self):
        self.windowThread = None

    @QtCore.pyqtSlot(int)
    def set_progressBar(self, value):
        self.progress_bar.setValue(value)

    @QtCore.pyqtSlot(pd.DataFrame)
    def save_df_result(self, df):
        self.df_result = df
        self.print_result_info()
    
    def print_result_info(self):
        df_result = self.df_result
        # 五種績效指標
        titles = ['profit', 'profit_to_MDD', 'MDD', 'AR', 'MAR']
        for title in titles:
            # 找出最佳窗格的位置與其數值
            index = df_result[title].idxmax()
            text = "Best {0} ({1}, {2}): {3}".format(
                title, int(df_result.loc[index]['t1']), int(df_result.loc[index]['t2']),
                round(df_result.loc[index][title], 2))
            self.set_result_textBrowser(text)
            text = "Best {0} [Profit, Profit/MDD, AR, MAR]: {1}, {2}, {3}, {4}".format(
                    title,
                    round(df_result.loc[index]['profit'], 2),
                    round(df_result.loc[index]['profit_to_MDD'], 2), 
                    round(df_result.loc[index]['AR'], 2),
                    round(df_result.loc[index]['MAR'], 2))
            self.set_result_textBrowser(text)