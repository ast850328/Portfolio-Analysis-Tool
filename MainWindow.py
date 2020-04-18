import pandas as pd
from functools import reduce
from os import listdir
from os.path import isfile, join

from CLA import CLA
from HRP import HRP
from Optimal_F import Optimal_F
from Selector import Selector
from SlidingWindow import SlidingWindow

from Ui_MainWindow import Ui_MainWindow
from ConfigWindow import ConfigWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget, QTableWidgetItem

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.df_stocks = None
        self.setupUi(self)
        self.clear_ui()
        self.bind_init_event()
        # self.result_table.horizontalHeader().setSectionResizeMode(3)

    def clear_ui(self):
        self.investments_table.setRowCount(0)
        self.result_table.setRowCount(0)
        self.result_textBrowser.clear()
        self.assets_text.clear()
        self.rolling_month_text.clear()
        self.ranking_box.clear()
        self.ranking_box.addItems(['All'])
        self.t1_start_text.clear()
        self.t1_end_text.clear()
        self.t2_start_text.clear()
        self.t2_end_text.clear()

    def bind_init_event(self):
        # import data button
        # self.import_data_button.clicked.connect(self.get_file)
        self.assets_text.installEventFilter(self)
        self.rolling_checkBox.stateChanged.connect(self.set_rolling_months)
        self.import_investments_button.clicked.connect(self.import_investments)
        self.ranking_box.currentTextChanged.connect(self.set_basis_box)
        self.config_button.clicked.connect(self.set_config)
        self.clear_button.clicked.connect(self.clear_ui)
        self.play_button.clicked.connect(self.play)

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
        # elif obj == self.stocks_listView:
        #     if event.type() == QtCore.QEvent.Timer:
        #         number = len(self.get_checked_items())
        #         self.set_select_box(number)
        #     return False
        else:
            return QWidget.eventFilter(self, obj, event)

    def format_dollar(self, text):
        text = text.replace(',', '')
        dollarText = '{:,}'.format(int(text))
        return dollarText

    def set_rolling_months(self):
        if self.rolling_checkBox.checkState() == QtCore.Qt.Checked:
            self.rolling_month_text.setReadOnly(False)
        else:
            self.rolling_month_text.setReadOnly(True)

    def import_investments(self):
        files_path = self.get_files_path()
        # get file
        # self.read_files(self, files_path)
        if files_path != None:
            filenames = [path[path.rfind('/')+1: -4] for path in files_path]
            self.set_investments_table(filenames)
            self.set_ranking_box(len(filenames))
        else:
            return False

    def get_files_path(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)

        if dlg.exec_():
            files_path = dlg.selectedFiles()
            return files_path

    def read_files(self, files_path):
        for path in files_path:
            stock = path[path.rfind('/')+1: -4]

            df = pd.read_csv(path)
            if df.size >= 33000:
                stocks_names.append(stock)
                df = df.rename(columns={'Adj Close': stock})
                stocks_data.append(df[['Date', stock]])


        self.df_stocks = reduce(lambda left,right: pd.merge(left, right, on='Date'), stocks_data)
        pass

    def set_investments_table(self, filenames):
        self.investments_table.setRowCount(0)
        for name in filenames:
            self.insert_investment_row(name)

    def insert_investment_row(self, name):
        _translate = QtCore.QCoreApplication.translate
        row_position = self.investments_table.rowCount()
        self.investments_table.insertRow(row_position)

        self.investments_table.setItem(row_position, 0, QTableWidgetItem(name))

        type_combo_box = QtWidgets.QComboBox()
        type_combo_box_options = ['Stock', 'ETF', 'Future']
        for t in type_combo_box_options:
            type_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 1, type_combo_box)

        ticker_symbol_combo_box = QtWidgets.QComboBox()
        ticker_symbol_combo_box_options = self.get_ticker_symbols(type_combo_box_options[0])
        for t in ticker_symbol_combo_box_options:
            ticker_symbol_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 2, ticker_symbol_combo_box)

        unit_combo_box = QtWidgets.QComboBox()
        unit_combo_box_options = ['share', 'lot']
        for t in unit_combo_box_options:
            unit_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 3, unit_combo_box)

    def get_ticker_symbols(self, type):
        path = './symbols/' + str(type)
        files = [f[:-4] for f in listdir(path) if isfile(join(path, f)) and f[-3:] == 'csv']
        return files

    def set_ranking_box(self, number):
        self.ranking_box.clear()
        items = [str(x) for x in range(1, number)]
        items.insert(0, 'All')
        self.ranking_box.addItems(items)

    def import_price(self):
        sender = self.sender()
        files_path = self.get_files_path()
        if files_path != None:
            sender.setText('Done')
            filenames = [path[path.rfind('/')+1: -4] for path in files_path]
            # save price data
        else:
            return False

    def set_basis_box(self):
        ranking = self.ranking_box.currentText()
        if ranking == 'All':
            self.basis_box.setEnabled(False)
        else:
            self.basis_box.setEnabled(True)

    def set_config(self):
        print('config')
        model_name = self.model_box.currentText()
        # config_columns = self.get_model_columns()
        config_dialog = ConfigWindow(self)
        config_dialog.show()
        # if config_dialog.exec_():
        #     # files_path = dlg.selectedFiles()
        #     pass
        pass

    def get_model_columns(self, model_name):
        columns = []
        if model_name == 'CLA':
            pass
        elif model_name == 'HRP':
            pass
        elif model_name == 'Optimal F':
            pass
        elif model_name == 'Equal Weight':
            pass
        elif model_name == 'Equal Weight':
            pass
        elif model_name == 'Custom':
            pass
        pass

    def play(self):
        data = self.get_input_data()
        print(data)
        # selector = self.generate_selector(data['number'], data['target'])
        # model = self.generate_model(data['model_name'], data['config'])
        # self.result_table.setRowCount(0)
        # self.result_textBrowser.append('')
        # self.result_textBrowser.append('Running...')
        # t1_start = int(data['t1_start'])
        # t1_end = int(data['t1_end'])
        # t2_start = int(data['t2_start'])
        # t2_end = int(data['t2_end'])
        # assets = int(data['assets'])
        # stocks_name = data['stocks_name']
        # df = self.df_stocks[['Date'] + stocks_name]

        # sliding_window = SlidingWindow(df, assets, selector, model)
        # for i in range(t1_start, t1_end+1, 1):
        #     for j in range(t2_start, t2_end+1, 1):
        #         total_equity, max_MDD, CAGR, MAR, data = sliding_window.play(i, j)
        #         print(total_equity, max_MDD, CAGR, MAR)
        #         row_position = self.result_table.rowCount()
        #         self.result_table.insertRow(row_position)
        #         self.result_table.setItem(row_position , 0, QTableWidgetItem(str(i)))
        #         self.result_table.setItem(row_position , 1, QTableWidgetItem(str(j)))
        #         self.result_table.setItem(row_position , 2, QTableWidgetItem(str(total_equity)))
        #         self.result_table.setItem(row_position , 3, QTableWidgetItem(str(max_MDD)))
        #         self.result_table.setItem(row_position , 4, QTableWidgetItem(str(total_equity/max_MDD)))
        #         self.result_table.setItem(row_position , 5, QTableWidgetItem(str(CAGR)))
        #         self.result_table.setItem(row_position , 6, QTableWidgetItem(str(MAR)))
        #         self.result_table.scrollToBottom()
        #         print('==============================')
        # self.result_textBrowser.append('Done.')

    def get_input_data(self):
        data = {}

        data['assets'] = int(self.assets_text.text().replace(',', ''))
        data['rolling'] = self.rolling_checkBox.isChecked()
        data['rolling_month'] = self.rolling_month_text.text()

        data['ranking'] = self.ranking_box.currentText()
        data['basis'] = self.basis_box.currentText()

        data['model_name'] = self.model_box.currentText()
        data['config'] = None ## Todo

        data['t1_start'] = self.t1_start_text.text()
        data['t1_end'] = self.t1_end_text.text()
        data['t2_start'] = self.t2_start_text.text()
        data['t2_end'] = self.t2_end_text.text()

        return data

    def generate_model(self, model_name, config=None):
        model = None
        if model_name == 'HRP':
            model = HRP(config)
        elif model_name == 'CLA':
            model = CLA()
        elif model_name == 'Optimal F':
            model = Optimal_F()
        elif model_name == 'Equal':
            pass
        return model

    def generate_selector(self, number, target):
        selector = Selector(number, target)
        return selector
