import sys
import pandas as pd
# import CLA
# import HRP
from functools import reduce
from template import Ui_Window
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget


class MainWindow(QMainWindow, Ui_Window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.df_stocks = None

        self.setupUi(self)
        self.bind_init_event()

    def eventFilter(self, obj, event):
        # print(type(obj))
        if obj == self.assets_text:
            if event.type() == QtCore.QEvent.KeyRelease:
                text = self.assets_text.text()
                if text is '':
                    return False
                text = text.replace(',', '')
                text = '{:,}'.format(int(text))
                self.assets_text.setText(text)
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

    def bind_init_event(self):
        # import data button
        self.import_data_button.clicked.connect(self.get_file)
        self.assets_text.installEventFilter(self)
        self.stocks_listView.installEventFilter(self)
        self.select_box.currentTextChanged.connect(self.set_ranking_box)
        # self.config_button
        # self.clear_button
        self.play_button.clicked.connect(self.play_window)

    def set_ranking_box(self):
        select = self.select_box.currentText()
        if select == 'All':
            self.ranking_box.setEnabled(False)
        else:
            self.ranking_box.setEnabled(True)

    def get_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            stocks_names = []
            stocks_data = []
            for filename in filenames:
                stock = filename[filename.rfind('/')+1: -4]
                stocks_names.append(stock)

                df = pd.read_csv(filename)
                if df.size >= 33000:
                    df = df.rename(columns={'Adj Close': stock})
                    stocks_data.append(df[['Date', stock]])

            self.df_stocks = reduce(lambda left,right: pd.merge(left, right, on='Date'), stocks_data)
            # print(self.df_stocks)
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

    def generate_model(model_name, config):
        pass

    def generate_selector(number, target):
        pass

    def play_window(self):
        data = self.get_input_data()
        print(data)

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

        data['assets'] = self.assets_text.text()
        data['select'] = self.select_box.currentText()
        data['ranking'] = self.ranking_box.currentText()
        data['model'] = self.model_box.currentText()

        # data['config']

        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
