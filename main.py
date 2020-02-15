import sys
import pandas as pd
# import CLA
# import HRP
from Selector import Selector
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
        self.select_box.currentTextChanged.connect(self.set_target_box)
        # self.config_button
        # self.clear_button
        self.play_button.clicked.connect(self.play)

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
            for filename in filenames:
                stock = filename[filename.rfind('/')+1: -4]

                df = pd.read_csv(filename)
                if df.size >= 33000:
                    stocks_names.append(stock)
                    df = df.rename(columns={'Adj Close': stock})
                    stocks_data.append(df[['Date', stock]])


            self.df_stocks = reduce(lambda left,right: pd.merge(left, right, on='Date'), stocks_data)
            # print(self.df_stocks)
            self.set_stocks(stocks_names)
            self.set_select_box(len(stocks_names))

            # start_date = ''
            # end_date = ''
            # stocks_names = []
            # tmp_data = []
            # data = []

            # for filename in filenames:
            #     name = filename[filename.rfind('/')+1: -4]
            #     stocks_names.append(name)

            #     df = pd.read_csv('./stocks/' + name + '.CSV', header=None, names=['Date', name])
            #     df['Date']= pd.to_datetime(df['Date'])
            #     df = df.groupby('Date').sum()
            #     start = df.first_valid_index()
            #     end = df.last_valid_index()
            #     if start_date == '' or start < start_date:
            #         start_date = start
            #     if end_date == '' or end > end_date:
            #         end_date = end
            #     tmp_data.append(df)

            # idx = pd.date_range(start_date, end_date)

            # for d in tmp_data:
            #     d = d.reindex(idx, fill_value=0)
            #     d['Date'] = d.index
            #     data.append(d)

            # df_final = reduce(lambda left,right: pd.merge(left, right, on='Date'), data)
            # cols = df_final.columns.tolist()
            # cols.remove('Date')
            # cols.insert(0, 'Date')
            # df_final = df_final[cols]

            # self.df_stocks = df_final
            # self.set_stocks(stocks_names)
            # self.set_select_box(len(stocks_names))

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
        pass

    def generate_selector(self, number, ranking):
        self.selector = Selector(number, ranking)

        pass

    def play(self):
        data = self.get_input_data()
        self.generate_selector(data['select'], data['target'])
        self.generate_model(data['model'])
        # print(self.selector)

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
        data['target'] = self.target_box.currentText()
        data['model'] = self.model_box.currentText()

        # data['config']

        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
