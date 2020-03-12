import sys
import pandas as pd
from CLA import CLA
from HRP import HRP
from Optimal_F import Optimal_F
from Selector import Selector
from functools import reduce
from template import Ui_MainWindow
from SlidingWindow import SlidingWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QTableWidgetItem

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.df_stocks = None
        self.setupUi(self)
        self.clear_ui()
        self.bind_init_event()
        # self.result_table.horizontalHeader().setSectionResizeMode(3)

    def clear_ui(self):
        self.investments_table.clear()
        self.investments_table.setRowCount(0)
        self.result_table.clear()
        self.result_table.setRowCount(0)
        self.result_textBrowser.clear()
        self.assets_text.clear()
        self.rolling_month_text.clear()
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
        # self.stocks_listView.installEventFilter(self)
        # self.select_box.currentTextChanged.connect(self.set_target_box)
        # self.config_button
        # self.clear_button
        # self.play_button.clicked.connect(self.play)

    def eventFilter(self, obj, event):
        # print(type(obj))
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
        elif obj == self.stocks_listView:
            if event.type() == QtCore.QEvent.Timer:
                number = len(self.get_checked_items())
                self.set_select_box(number)
            return False
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
        pass

    def import_investments(self):
        files_path = self.get_files_path()
        # get file
        # self.read_files(self, files_path)
        filenames = [path[path.rfind('/')+1: -4] for path in files_path]
        self.set_investments_table(filenames)
        pass

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
        self.investments_table.clear()
        self.investments_table.setRowCount(0)
        for name in filenames:
            self.insert_investment_row(name)

    def insert_investment_row(self, name):
        _translate = QtCore.QCoreApplication.translate
        row_position = self.investments_table.rowCount()
        self.investments_table.insertRow(row_position)

        self.investments_table.setItem(row_position, 0, QTableWidgetItem(name))

        type_combo_box = QtWidgets.QComboBox()
        type_combo_box_options = ['ETF', 'Stock', 'Futures']
        for t in type_combo_box_options:
                type_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 1, type_combo_box)

        price_per_point_text = QtWidgets.QLineEdit()
        price_per_point_text.setPlaceholderText('1')
        price_per_point_text.setAlignment(QtCore.Qt.AlignRight)
        self.investments_table.setCellWidget(row_position, 2, price_per_point_text)

        unit_combo_box = QtWidgets.QComboBox()
        unit_combo_box_options = ['share', 'lot']
        for t in unit_combo_box_options:
                unit_combo_box.addItem(t)
        self.investments_table.setCellWidget(row_position, 3, unit_combo_box)

        import_price_button = QtWidgets.QPushButton()
        import_price_button.setText(_translate("MainWindow", "Import Price"))
        self.investments_table.setCellWidget(row_position, 4, import_price_button)

    def set_target_box(self):
        select = self.select_box.currentText()
        if select == 'All':
            self.target_box.setEnabled(False)
        else:
            self.target_box.setEnabled(True)

    def get_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)

        if dlg.exec_():
            filenames = dlg.selectedFiles()

            stocks_names = []
            stocks_data = []

            self.set_stocks(stocks_names)
            self.set_select_box(len(stocks_names))

    def set_stocks(self, stocks_names):
        self.stocks_listView.clear()
        for name in stocks_names:
            item = QtWidgets.QListWidgetItem()
            item.setText(name)
            item.setCheckState(QtCore.Qt.Checked)
            self.stocks_listView.addItem(item)

    def set_select_box(self, number):
        self.select_box.clear()
        items = [str(x) for x in range(1, number)]
        items.insert(0, 'All')
        self.select_box.addItems(items)

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

    def play(self):
        self.result_table.setRowCount(0)
        self.result_textBrowser.append('')
        self.result_textBrowser.append('Running...')

        data = self.get_input_data()
        selector = self.generate_selector(data['number'], data['target'])
        model = self.generate_model(data['model_name'], data['config'])
        t1_start = int(data['t1_start'])
        t1_end = int(data['t1_end'])
        t2_start = int(data['t2_start'])
        t2_end = int(data['t2_end'])
        assets = int(data['assets'])
        stocks_name = data['stocks_name']
        df = self.df_stocks[['Date'] + stocks_name]
        sliding_window = SlidingWindow(df, assets, selector, model)
        for i in range(t1_start, t1_end+1, 1):
            for j in range(t2_start, t2_end+1, 1):
                total_equity, max_MDD, CAGR, MAR, data = sliding_window.play(i, j)
                print(total_equity, max_MDD, CAGR, MAR)
                row_position = self.result_table.rowCount()
                self.result_table.insertRow(row_position)
                self.result_table.setItem(row_position , 0, QTableWidgetItem(str(i)))
                self.result_table.setItem(row_position , 1, QTableWidgetItem(str(j)))
                self.result_table.setItem(row_position , 2, QTableWidgetItem(str(total_equity)))
                self.result_table.setItem(row_position , 3, QTableWidgetItem(str(max_MDD)))
                self.result_table.setItem(row_position , 4, QTableWidgetItem(str(total_equity/max_MDD)))
                self.result_table.setItem(row_position , 5, QTableWidgetItem(str(CAGR)))
                self.result_table.setItem(row_position , 6, QTableWidgetItem(str(MAR)))
                self.result_table.scrollToBottom()
                print('==============================')
        self.result_textBrowser.append('Done.')

    def get_checked_items(self):
        checked_items = []
        for index in range(self.stocks_listView.count()):
            if self.stocks_listView.item(index).checkState() == QtCore.Qt.Checked:
                checked_items.append(self.stocks_listView.item(index).text())
        return checked_items

    def get_input_data(self):
        data = {}

        data['stocks_name'] = self.get_checked_items()
        data['t1_start'] = self.t1_start_text.text()
        data['t1_end'] = self.t1_end_text.text()
        data['t2_start'] = self.t2_start_text.text()
        data['t2_end'] = self.t2_end_text.text()
        data['assets'] = self.assets_text.text().replace(',', '')

        data['number'] = self.select_box.currentText()
        data['target'] = self.target_box.currentText()

        data['model_name'] = self.model_box.currentText()
        data['config'] = None ## Todo

        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
