# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1282, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.investments_table_label = QtWidgets.QLabel(self.centralwidget)
        self.investments_table_label.setObjectName("investments_table_label")
        self.gridLayout_2.addWidget(self.investments_table_label, 0, 0, 1, 1)
        self.result_table_label = QtWidgets.QLabel(self.centralwidget)
        self.result_table_label.setObjectName("result_table_label")
        self.gridLayout_2.addWidget(self.result_table_label, 0, 1, 1, 1)
        self.result_textBrowser_label = QtWidgets.QLabel(self.centralwidget)
        self.result_textBrowser_label.setObjectName("result_textBrowser_label")
        self.gridLayout_2.addWidget(self.result_textBrowser_label, 2, 1, 1, 1)
        self.config_layout = QtWidgets.QGridLayout()
        self.config_layout.setObjectName("config_layout")
        self.performance_selection_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.performance_selection_label.sizePolicy().hasHeightForWidth())
        self.performance_selection_label.setSizePolicy(sizePolicy)
        self.performance_selection_label.setObjectName("performance_selection_label")
        self.config_layout.addWidget(self.performance_selection_label, 0, 6, 1, 2)
        self.weight_allocation_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight_allocation_label.sizePolicy().hasHeightForWidth())
        self.weight_allocation_label.setSizePolicy(sizePolicy)
        self.weight_allocation_label.setObjectName("weight_allocation_label")
        self.config_layout.addWidget(self.weight_allocation_label, 0, 8, 1, 2)
        self.assets_text_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_text_label.sizePolicy().hasHeightForWidth())
        self.assets_text_label.setSizePolicy(sizePolicy)
        self.assets_text_label.setObjectName("assets_text_label")
        self.config_layout.addWidget(self.assets_text_label, 1, 0, 1, 1)
        self.assets_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_text.sizePolicy().hasHeightForWidth())
        self.assets_text.setSizePolicy(sizePolicy)
        self.assets_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.assets_text.setObjectName("assets_text")
        self.config_layout.addWidget(self.assets_text, 1, 1, 1, 2)
        self.start_time_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_time_label.sizePolicy().hasHeightForWidth())
        self.start_time_label.setSizePolicy(sizePolicy)
        self.start_time_label.setObjectName("start_time_label")
        self.config_layout.addWidget(self.start_time_label, 1, 3, 1, 1)
        self.start_year_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_year_text.sizePolicy().hasHeightForWidth())
        self.start_year_text.setSizePolicy(sizePolicy)
        self.start_year_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_year_text.setObjectName("start_year_text")
        self.config_layout.addWidget(self.start_year_text, 1, 4, 1, 1)
        self.start_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_month_text.sizePolicy().hasHeightForWidth())
        self.start_month_text.setSizePolicy(sizePolicy)
        self.start_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_month_text.setObjectName("start_month_text")
        self.config_layout.addWidget(self.start_month_text, 1, 5, 1, 1)
        self.ranking_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranking_label.sizePolicy().hasHeightForWidth())
        self.ranking_label.setSizePolicy(sizePolicy)
        self.ranking_label.setObjectName("ranking_label")
        self.config_layout.addWidget(self.ranking_label, 1, 6, 1, 1)
        self.ranking_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranking_box.sizePolicy().hasHeightForWidth())
        self.ranking_box.setSizePolicy(sizePolicy)
        self.ranking_box.setObjectName("ranking_box")
        self.ranking_box.addItem("")
        self.config_layout.addWidget(self.ranking_box, 1, 7, 1, 1)
        self.model_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label.sizePolicy().hasHeightForWidth())
        self.model_label.setSizePolicy(sizePolicy)
        self.model_label.setObjectName("model_label")
        self.config_layout.addWidget(self.model_label, 1, 8, 1, 1)
        self.model_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_box.sizePolicy().hasHeightForWidth())
        self.model_box.setSizePolicy(sizePolicy)
        self.model_box.setObjectName("model_box")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.config_layout.addWidget(self.model_box, 1, 9, 1, 1)
        self.t1_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_label.sizePolicy().hasHeightForWidth())
        self.t1_start_label.setSizePolicy(sizePolicy)
        self.t1_start_label.setObjectName("t1_start_label")
        self.config_layout.addWidget(self.t1_start_label, 1, 10, 1, 1)
        self.t1_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_text.sizePolicy().hasHeightForWidth())
        self.t1_start_text.setSizePolicy(sizePolicy)
        self.t1_start_text.setText("")
        self.t1_start_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1_start_text.setObjectName("t1_start_text")
        self.config_layout.addWidget(self.t1_start_text, 1, 11, 1, 1)
        self.t1_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_label.sizePolicy().hasHeightForWidth())
        self.t1_end_label.setSizePolicy(sizePolicy)
        self.t1_end_label.setObjectName("t1_end_label")
        self.config_layout.addWidget(self.t1_end_label, 1, 12, 1, 1)
        self.t1_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_text.sizePolicy().hasHeightForWidth())
        self.t1_end_text.setSizePolicy(sizePolicy)
        self.t1_end_text.setText("")
        self.t1_end_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1_end_text.setObjectName("t1_end_text")
        self.config_layout.addWidget(self.t1_end_text, 1, 13, 1, 1)
        self.ignore_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_label.sizePolicy().hasHeightForWidth())
        self.ignore_label.setSizePolicy(sizePolicy)
        self.ignore_label.setObjectName("ignore_label")
        self.config_layout.addWidget(self.ignore_label, 2, 0, 1, 1)
        self.ignore_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_month_text.sizePolicy().hasHeightForWidth())
        self.ignore_month_text.setSizePolicy(sizePolicy)
        self.ignore_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ignore_month_text.setObjectName("ignore_month_text")
        self.config_layout.addWidget(self.ignore_month_text, 2, 1, 1, 1)
        self.months_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.months_label.sizePolicy().hasHeightForWidth())
        self.months_label.setSizePolicy(sizePolicy)
        self.months_label.setObjectName("months_label")
        self.config_layout.addWidget(self.months_label, 2, 2, 1, 1)
        self.end_time_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_time_label.sizePolicy().hasHeightForWidth())
        self.end_time_label.setSizePolicy(sizePolicy)
        self.end_time_label.setObjectName("end_time_label")
        self.config_layout.addWidget(self.end_time_label, 2, 3, 1, 1)
        self.end_year_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_year_text.sizePolicy().hasHeightForWidth())
        self.end_year_text.setSizePolicy(sizePolicy)
        self.end_year_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_year_text.setObjectName("end_year_text")
        self.config_layout.addWidget(self.end_year_text, 2, 4, 1, 1)
        self.end_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_month_text.sizePolicy().hasHeightForWidth())
        self.end_month_text.setSizePolicy(sizePolicy)
        self.end_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_month_text.setObjectName("end_month_text")
        self.config_layout.addWidget(self.end_month_text, 2, 5, 1, 1)
        self.basis_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis_label.sizePolicy().hasHeightForWidth())
        self.basis_label.setSizePolicy(sizePolicy)
        self.basis_label.setObjectName("basis_label")
        self.config_layout.addWidget(self.basis_label, 2, 6, 1, 1)
        self.basis_box = QtWidgets.QComboBox(self.centralwidget)
        self.basis_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis_box.sizePolicy().hasHeightForWidth())
        self.basis_box.setSizePolicy(sizePolicy)
        self.basis_box.setEditable(False)
        self.basis_box.setObjectName("basis_box")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.config_layout.addWidget(self.basis_box, 2, 7, 1, 1)
        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_button.sizePolicy().hasHeightForWidth())
        self.config_button.setSizePolicy(sizePolicy)
        self.config_button.setObjectName("config_button")
        self.config_layout.addWidget(self.config_button, 2, 8, 1, 2)
        self.t2_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_label.sizePolicy().hasHeightForWidth())
        self.t2_start_label.setSizePolicy(sizePolicy)
        self.t2_start_label.setObjectName("t2_start_label")
        self.config_layout.addWidget(self.t2_start_label, 2, 10, 1, 1)
        self.t2_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_text.sizePolicy().hasHeightForWidth())
        self.t2_start_text.setSizePolicy(sizePolicy)
        self.t2_start_text.setText("")
        self.t2_start_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t2_start_text.setObjectName("t2_start_text")
        self.config_layout.addWidget(self.t2_start_text, 2, 11, 1, 1)
        self.t2_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_label.sizePolicy().hasHeightForWidth())
        self.t2_end_label.setSizePolicy(sizePolicy)
        self.t2_end_label.setObjectName("t2_end_label")
        self.config_layout.addWidget(self.t2_end_label, 2, 12, 1, 1)
        self.t2_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_text.sizePolicy().hasHeightForWidth())
        self.t2_end_text.setSizePolicy(sizePolicy)
        self.t2_end_text.setText("")
        self.t2_end_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t2_end_text.setObjectName("t2_end_text")
        self.config_layout.addWidget(self.t2_end_text, 2, 13, 1, 1)
        self.window_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_label.sizePolicy().hasHeightForWidth())
        self.window_label.setSizePolicy(sizePolicy)
        self.window_label.setObjectName("window_label")
        self.config_layout.addWidget(self.window_label, 0, 10, 1, 4)
        self.portfolio_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portfolio_label.sizePolicy().hasHeightForWidth())
        self.portfolio_label.setSizePolicy(sizePolicy)
        self.portfolio_label.setObjectName("portfolio_label")
        self.config_layout.addWidget(self.portfolio_label, 0, 0, 1, 6)
        self.gridLayout_2.addLayout(self.config_layout, 5, 0, 1, 2)
        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout.setObjectName("button_layout")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setObjectName("play_button")
        self.button_layout.addWidget(self.play_button, 0, 0, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setObjectName("clear_button")
        self.button_layout.addWidget(self.clear_button, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.button_layout, 5, 2, 1, 1)
        self.investments_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.investments_table.sizePolicy().hasHeightForWidth())
        self.investments_table.setSizePolicy(sizePolicy)
        self.investments_table.setObjectName("investments_table")
        self.investments_table.setColumnCount(4)
        self.investments_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.investments_table, 1, 0, 4, 1)
        self.result_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_table.sizePolicy().hasHeightForWidth())
        self.result_table.setSizePolicy(sizePolicy)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(7)
        self.result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.result_table, 1, 1, 1, 2)
        self.result_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_textBrowser.sizePolicy().hasHeightForWidth())
        self.result_textBrowser.setSizePolicy(sizePolicy)
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.gridLayout_2.addWidget(self.result_textBrowser, 3, 1, 1, 2)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_2.addWidget(self.progress_bar, 4, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1282, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menuBar.setFont(font)
        self.menuBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menuBar.setAcceptDrops(True)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuImport = QtWidgets.QMenu(self.menuBar)
        self.menuImport.setObjectName("menuImport")
        self.menuSave = QtWidgets.QMenu(self.menuBar)
        self.menuSave.setObjectName("menuSave")
        self.menuPlot = QtWidgets.QMenu(self.menuBar)
        self.menuPlot.setObjectName("menuPlot")
        MainWindow.setMenuBar(self.menuBar)
        self.action_import_investments = QtWidgets.QAction(MainWindow)
        self.action_import_investments.setCheckable(False)
        self.action_import_investments.setObjectName("action_import_investments")
        self.action_import_config = QtWidgets.QAction(MainWindow)
        self.action_import_config.setObjectName("action_import_config")
        self.action_save_result = QtWidgets.QAction(MainWindow)
        self.action_save_result.setObjectName("action_save_result")
        self.action_save_config = QtWidgets.QAction(MainWindow)
        self.action_save_config.setObjectName("action_save_config")
        self.action_import_result = QtWidgets.QAction(MainWindow)
        self.action_import_result.setObjectName("action_import_result")
        self.action_plot_result = QtWidgets.QAction(MainWindow)
        self.action_plot_result.setObjectName("action_plot_result")
        self.action_plot_window = QtWidgets.QAction(MainWindow)
        self.action_plot_window.setObjectName("action_plot_window")
        self.menuImport.addAction(self.action_import_investments)
        self.menuImport.addAction(self.action_import_config)
        self.menuImport.addAction(self.action_import_result)
        self.menuSave.addAction(self.action_save_result)
        self.menuSave.addAction(self.action_save_config)
        self.menuPlot.addAction(self.action_plot_result)
        self.menuPlot.addAction(self.action_plot_window)
        self.menuBar.addAction(self.menuImport.menuAction())
        self.menuBar.addAction(self.menuSave.menuAction())
        self.menuBar.addAction(self.menuPlot.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Portfolio Analysis Tool"))
        self.investments_table_label.setText(_translate("MainWindow", "Investments Table"))
        self.result_table_label.setText(_translate("MainWindow", "Result Table"))
        self.result_textBrowser_label.setText(_translate("MainWindow", "Result Browser"))
        self.performance_selection_label.setText(_translate("MainWindow", "Performance Selection"))
        self.weight_allocation_label.setText(_translate("MainWindow", "Weight Allocation Model"))
        self.assets_text_label.setText(_translate("MainWindow", "Assets:"))
        self.assets_text.setPlaceholderText(_translate("MainWindow", "100,000,000"))
        self.start_time_label.setText(_translate("MainWindow", "Start Time:"))
        self.start_year_text.setPlaceholderText(_translate("MainWindow", "year"))
        self.start_month_text.setPlaceholderText(_translate("MainWindow", "month"))
        self.ranking_label.setText(_translate("MainWindow", "Ranking:"))
        self.ranking_box.setItemText(0, _translate("MainWindow", "All"))
        self.model_label.setText(_translate("MainWindow", "Model:"))
        self.model_box.setItemText(0, _translate("MainWindow", "CLA"))
        self.model_box.setItemText(1, _translate("MainWindow", "HRP"))
        self.model_box.setItemText(2, _translate("MainWindow", "Optimal F"))
        self.model_box.setItemText(3, _translate("MainWindow", "Equal Risk"))
        self.model_box.setItemText(4, _translate("MainWindow", "Equal Weight"))
        self.t1_start_label.setText(_translate("MainWindow", "T1 Start:"))
        self.t1_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t1_end_label.setText(_translate("MainWindow", "T1 End:"))
        self.t1_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.ignore_label.setText(_translate("MainWindow", "Ignore:"))
        self.ignore_month_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.months_label.setText(_translate("MainWindow", "months"))
        self.end_time_label.setText(_translate("MainWindow", "End Time:"))
        self.end_year_text.setPlaceholderText(_translate("MainWindow", "year"))
        self.end_month_text.setPlaceholderText(_translate("MainWindow", "month"))
        self.basis_label.setText(_translate("MainWindow", "Basis:"))
        self.basis_box.setItemText(0, _translate("MainWindow", "Profit"))
        self.basis_box.setItemText(1, _translate("MainWindow", "Profit / MDD"))
        self.basis_box.setItemText(2, _translate("MainWindow", "AR"))
        self.basis_box.setItemText(3, _translate("MainWindow", "MAR"))
        self.config_button.setText(_translate("MainWindow", "Config"))
        self.t2_start_label.setText(_translate("MainWindow", "T2 Start:"))
        self.t2_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_end_label.setText(_translate("MainWindow", "T2 End:"))
        self.t2_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.window_label.setText(_translate("MainWindow", "Window"))
        self.portfolio_label.setText(_translate("MainWindow", "Portfolio"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        item = self.investments_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Investment"))
        item = self.investments_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.investments_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ticker Symbol"))
        item = self.investments_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "T1"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "T2"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Profit"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Profit / MDD"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "MDD"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "MAR"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.action_import_investments.setText(_translate("MainWindow", "Import Investments"))
        self.action_import_config.setText(_translate("MainWindow", "Import Config"))
        self.action_save_result.setText(_translate("MainWindow", "Save Result"))
        self.action_save_config.setText(_translate("MainWindow", "Save Config"))
        self.action_import_result.setText(_translate("MainWindow", "Import Result"))
        self.action_plot_result.setText(_translate("MainWindow", "Plot Result"))
        self.action_plot_window.setText(_translate("MainWindow", "Plot Window"))
