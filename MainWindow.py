import sys
import numpy as np
import pandas as pd
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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.df_stocks = None
        self.setupUi(self)
        self.clear_ui()
        self.bind_init_event()
        self.investments_file_path = None
        self.model_config = None

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

    def bind_init_event(self):
        self.assets_text.installEventFilter(self)
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
        else:
            return QWidget.eventFilter(self, obj, event)

    def format_dollar(self, text):
        text = text.replace(',', '')
        dollarText = '{:,}'.format(int(text))
        return dollarText

    def import_investments(self):
        files_path = self.get_files_path()
        self.investments_file_path = files_path
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

    def set_investments_table(self, filenames):
        self.investments_table.setRowCount(0)
        for name in filenames:
            self.insert_investment_row(name)

    def insert_investment_row(self, name):
        _translate = QtCore.QCoreApplication.translate
        row_position = self.investments_table.rowCount()
        self.investments_table.insertRow(row_position)
        name_item = QTableWidgetItem(name)
        name_item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.investments_table.setItem(row_position, 0, name_item)

        type_combo_box = QtWidgets.QComboBox()
        type_combo_box_options = ['Stock', 'ETF', 'Future']
        for t in type_combo_box_options:
            type_combo_box.addItem(t)
        # type_combo_box.installEventFilter(self)
        type_combo_box.currentTextChanged.connect(self.set_symbols)
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

    def set_symbols(self, text):
        sender = self.sender()
        point = sender.pos()
        row = int(point.y() / 30)
        ticker_symbol_combo_box = QtWidgets.QComboBox()
        ticker_symbol_combo_box_options = self.get_ticker_symbols(text)
        for t in ticker_symbol_combo_box_options:
            ticker_symbol_combo_box.addItem(t)
        self.investments_table.setCellWidget(row, 2, ticker_symbol_combo_box)

    def get_ticker_symbols(self, type):
        path = './symbols/' + str(type)
        files = [f[:-4] for f in listdir(path) if isfile(join(path, f)) and f[-3:] == 'csv']
        return files

    def set_ranking_box(self, number):
        self.ranking_box.clear()
        items = [str(x) for x in range(1, number)]
        items.insert(0, 'All')
        self.ranking_box.addItems(items)

    def set_basis_box(self):
        ranking = self.ranking_box.currentText()
        if ranking == 'All':
            self.basis_box.setEnabled(False)
        else:
            self.basis_box.setEnabled(True)

    def set_config(self):
        model_name = self.model_box.currentText()

        dialog = QtWidgets.QDialog()
        ui = Ui_ConfigDialog()
        ui.setupUi(dialog)
        ui.set_model_label(model_name)
        ui.limit_column(model_name)
        res = dialog.exec_()
        if res == QtWidgets.QDialog.Accepted:
            print('accept')
            self.model_config = ui.get_model_config()
        else:
            print('cancel')

    def play(self):
        all_commodity = self.read_all_commodity()
        investments, commodity = self.get_investments(all_commodity)

        data = self.get_input_data()
        start_datetime = np.datetime64(data['start_year'] + '-' + data['start_month'])
        end_datetime = np.datetime64(data['end_year'] + '-' + data['end_month'])
        config_portfolio = {
            'assets': data['assets'],
            'start_datetime': start_datetime,
            'end_datetime': end_datetime,
            'ignore_month': data['ignore_month'],
            'commodity': commodity
        }

        selector = self.generate_selector(data['ranking'], data['basis'])

        model_config = self.model_config
        model = self.generate_model(data['model_name'], model_config)

        print(investments)
        print(commodity)
        print(config_portfolio)

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
        #         total_equity, max_MDD, AR, MAR, data = sliding_window.play(i, j)
        #         print(total_equity, max_MDD, AR, MAR)
        #         row_position = self.result_table.rowCount()
        #         self.result_table.insertRow(row_position)
        #         self.result_table.setItem(row_position , 0, QTableWidgetItem(str(i)))
        #         self.result_table.setItem(row_position , 1, QTableWidgetItem(str(j)))
        #         self.result_table.setItem(row_position , 2, QTableWidgetItem(str(total_equity)))
        #         self.result_table.setItem(row_position , 3, QTableWidgetItem(str(max_MDD)))
        #         self.result_table.setItem(row_position , 4, QTableWidgetItem(str(total_equity/max_MDD)))
        #         self.result_table.setItem(row_position , 5, QTableWidgetItem(str(AR)))
        #         self.result_table.setItem(row_position , 6, QTableWidgetItem(str(MAR)))
        #         self.result_table.scrollToBottom()
        #         print('==============================')
        # self.result_textBrowser.append('Done.')

    def get_input_data(self):
        data = {}

        data['assets'] = int(self.assets_text.text().replace(',', ''))
        data['ignore_month'] = self.ignore_month_text.text()
        data['start_year'] = self.start_year_text.text()
        data['start_month'] = self.start_month_text.text()
        data['end_year'] = self.end_year_text.text()
        data['end_month'] = self.end_month_text.text()

        data['ranking'] = self.ranking_box.currentText()
        data['basis'] = self.basis_box.currentText()

        data['model_name'] = self.model_box.currentText()

        data['t1_start'] = self.t1_start_text.text()
        data['t1_end'] = self.t1_end_text.text()
        data['t2_start'] = self.t2_start_text.text()
        data['t2_end'] = self.t2_end_text.text()

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

