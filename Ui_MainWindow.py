# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.save_config_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_config_button.sizePolicy().hasHeightForWidth())
        self.save_config_button.setSizePolicy(sizePolicy)
        self.save_config_button.setObjectName("save_config_button")
        self.gridLayout_4.addWidget(self.save_config_button, 2, 1, 1, 1)
        self.investments_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.investments_table.sizePolicy().hasHeightForWidth())
        self.investments_table.setSizePolicy(sizePolicy)
        self.investments_table.setObjectName("investments_table")
        self.investments_table.setColumnCount(4)
        self.investments_table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.investments_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.investments_table.setItem(0, 1, item)
        self.gridLayout_4.addWidget(self.investments_table, 0, 0, 3, 1)
        self.result_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_textBrowser.sizePolicy().hasHeightForWidth())
        self.result_textBrowser.setSizePolicy(sizePolicy)
        self.result_textBrowser.setMinimumSize(QtCore.QSize(760, 192))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.result_textBrowser.setFont(font)
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.gridLayout_4.addWidget(self.result_textBrowser, 1, 1, 1, 2)
        self.plot_result_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_result_button.sizePolicy().hasHeightForWidth())
        self.plot_result_button.setSizePolicy(sizePolicy)
        self.plot_result_button.setObjectName("plot_result_button")
        self.gridLayout_4.addWidget(self.plot_result_button, 2, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.assets_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_label.sizePolicy().hasHeightForWidth())
        self.assets_label.setSizePolicy(sizePolicy)
        self.assets_label.setObjectName("assets_label")
        self.gridLayout.addWidget(self.assets_label, 1, 0, 1, 1)
        self.starttime_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.starttime_label.sizePolicy().hasHeightForWidth())
        self.starttime_label.setSizePolicy(sizePolicy)
        self.starttime_label.setObjectName("starttime_label")
        self.gridLayout.addWidget(self.starttime_label, 1, 3, 1, 1)
        self.start_year_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_year_text.sizePolicy().hasHeightForWidth())
        self.start_year_text.setSizePolicy(sizePolicy)
        self.start_year_text.setText("")
        self.start_year_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_year_text.setReadOnly(False)
        self.start_year_text.setObjectName("start_year_text")
        self.gridLayout.addWidget(self.start_year_text, 1, 4, 1, 1)
        self.start_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_month_text.sizePolicy().hasHeightForWidth())
        self.start_month_text.setSizePolicy(sizePolicy)
        self.start_month_text.setText("")
        self.start_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_month_text.setReadOnly(False)
        self.start_month_text.setObjectName("start_month_text")
        self.gridLayout.addWidget(self.start_month_text, 1, 5, 1, 1)
        self.ignore_month_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_month_label.sizePolicy().hasHeightForWidth())
        self.ignore_month_label.setSizePolicy(sizePolicy)
        self.ignore_month_label.setObjectName("ignore_month_label")
        self.gridLayout.addWidget(self.ignore_month_label, 2, 0, 1, 1)
        self.ignore_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_month_text.sizePolicy().hasHeightForWidth())
        self.ignore_month_text.setSizePolicy(sizePolicy)
        self.ignore_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ignore_month_text.setReadOnly(False)
        self.ignore_month_text.setObjectName("ignore_month_text")
        self.gridLayout.addWidget(self.ignore_month_text, 2, 1, 1, 1)
        self.ignore_months_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_months_label.sizePolicy().hasHeightForWidth())
        self.ignore_months_label.setSizePolicy(sizePolicy)
        self.ignore_months_label.setObjectName("ignore_months_label")
        self.gridLayout.addWidget(self.ignore_months_label, 2, 2, 1, 1)
        self.endtime_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endtime_label.sizePolicy().hasHeightForWidth())
        self.endtime_label.setSizePolicy(sizePolicy)
        self.endtime_label.setObjectName("endtime_label")
        self.gridLayout.addWidget(self.endtime_label, 2, 3, 1, 1)
        self.end_year_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_year_text.sizePolicy().hasHeightForWidth())
        self.end_year_text.setSizePolicy(sizePolicy)
        self.end_year_text.setText("")
        self.end_year_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_year_text.setReadOnly(False)
        self.end_year_text.setObjectName("end_year_text")
        self.gridLayout.addWidget(self.end_year_text, 2, 4, 1, 1)
        self.end_month_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_month_text.sizePolicy().hasHeightForWidth())
        self.end_month_text.setSizePolicy(sizePolicy)
        self.end_month_text.setText("")
        self.end_month_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_month_text.setReadOnly(False)
        self.end_month_text.setObjectName("end_month_text")
        self.gridLayout.addWidget(self.end_month_text, 2, 5, 1, 1)
        self.assets_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_text.sizePolicy().hasHeightForWidth())
        self.assets_text.setSizePolicy(sizePolicy)
        self.assets_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.assets_text.setObjectName("assets_text")
        self.gridLayout.addWidget(self.assets_text, 1, 1, 1, 2)
        self.portfolio_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portfolio_label.sizePolicy().hasHeightForWidth())
        self.portfolio_label.setSizePolicy(sizePolicy)
        self.portfolio_label.setObjectName("portfolio_label")
        self.gridLayout.addWidget(self.portfolio_label, 0, 0, 1, 6)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.selection_layout = QtWidgets.QGridLayout()
        self.selection_layout.setObjectName("selection_layout")
        self.basis_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis_label.sizePolicy().hasHeightForWidth())
        self.basis_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.basis_label.setFont(font)
        self.basis_label.setObjectName("basis_label")
        self.selection_layout.addWidget(self.basis_label, 2, 0, 1, 1)
        self.selection_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection_label.sizePolicy().hasHeightForWidth())
        self.selection_label.setSizePolicy(sizePolicy)
        self.selection_label.setObjectName("selection_label")
        self.selection_layout.addWidget(self.selection_label, 0, 0, 1, 2)
        self.basis_box = QtWidgets.QComboBox(self.centralwidget)
        self.basis_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis_box.sizePolicy().hasHeightForWidth())
        self.basis_box.setSizePolicy(sizePolicy)
        self.basis_box.setAcceptDrops(False)
        self.basis_box.setDuplicatesEnabled(False)
        self.basis_box.setObjectName("basis_box")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.basis_box.addItem("")
        self.selection_layout.addWidget(self.basis_box, 2, 1, 1, 1)
        self.ranking_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranking_label.sizePolicy().hasHeightForWidth())
        self.ranking_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.ranking_label.setFont(font)
        self.ranking_label.setObjectName("ranking_label")
        self.selection_layout.addWidget(self.ranking_label, 1, 0, 1, 1)
        self.ranking_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranking_box.sizePolicy().hasHeightForWidth())
        self.ranking_box.setSizePolicy(sizePolicy)
        self.ranking_box.setObjectName("ranking_box")
        self.ranking_box.addItem("")
        self.selection_layout.addWidget(self.ranking_box, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.selection_layout, 0, 1, 1, 1)
        self.model_layout = QtWidgets.QGridLayout()
        self.model_layout.setObjectName("model_layout")
        self.model_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label.sizePolicy().hasHeightForWidth())
        self.model_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.model_label.setFont(font)
        self.model_label.setObjectName("model_label")
        self.model_layout.addWidget(self.model_label, 1, 0, 1, 1)
        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_button.sizePolicy().hasHeightForWidth())
        self.config_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.config_button.setFont(font)
        self.config_button.setAutoDefault(True)
        self.config_button.setDefault(False)
        self.config_button.setFlat(False)
        self.config_button.setObjectName("config_button")
        self.model_layout.addWidget(self.config_button, 2, 0, 1, 2)
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
        self.model_layout.addWidget(self.model_box, 1, 1, 1, 1)
        self.weighting_model_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weighting_model_label.sizePolicy().hasHeightForWidth())
        self.weighting_model_label.setSizePolicy(sizePolicy)
        self.weighting_model_label.setObjectName("weighting_model_label")
        self.model_layout.addWidget(self.weighting_model_label, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.model_layout, 0, 2, 1, 1)
        self.window_layout = QtWidgets.QGridLayout()
        self.window_layout.setObjectName("window_layout")
        self.t2_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_label.sizePolicy().hasHeightForWidth())
        self.t2_end_label.setSizePolicy(sizePolicy)
        self.t2_end_label.setObjectName("t2_end_label")
        self.window_layout.addWidget(self.t2_end_label, 2, 2, 1, 1)
        self.t1_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_label.sizePolicy().hasHeightForWidth())
        self.t1_start_label.setSizePolicy(sizePolicy)
        self.t1_start_label.setObjectName("t1_start_label")
        self.window_layout.addWidget(self.t1_start_label, 1, 0, 1, 1)
        self.t1_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_text.sizePolicy().hasHeightForWidth())
        self.t1_end_text.setSizePolicy(sizePolicy)
        self.t1_end_text.setText("")
        self.t1_end_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1_end_text.setObjectName("t1_end_text")
        self.window_layout.addWidget(self.t1_end_text, 1, 3, 1, 1)
        self.t2_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_text.sizePolicy().hasHeightForWidth())
        self.t2_start_text.setSizePolicy(sizePolicy)
        self.t2_start_text.setText("")
        self.t2_start_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t2_start_text.setObjectName("t2_start_text")
        self.window_layout.addWidget(self.t2_start_text, 2, 1, 1, 1)
        self.t2_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_label.sizePolicy().hasHeightForWidth())
        self.t2_start_label.setSizePolicy(sizePolicy)
        self.t2_start_label.setObjectName("t2_start_label")
        self.window_layout.addWidget(self.t2_start_label, 2, 0, 1, 1)
        self.t1_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_label.sizePolicy().hasHeightForWidth())
        self.t1_end_label.setSizePolicy(sizePolicy)
        self.t1_end_label.setObjectName("t1_end_label")
        self.window_layout.addWidget(self.t1_end_label, 1, 2, 1, 1)
        self.t1_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_text.sizePolicy().hasHeightForWidth())
        self.t1_start_text.setSizePolicy(sizePolicy)
        self.t1_start_text.setText("")
        self.t1_start_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1_start_text.setObjectName("t1_start_text")
        self.window_layout.addWidget(self.t1_start_text, 1, 1, 1, 1)
        self.t2_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_text.sizePolicy().hasHeightForWidth())
        self.t2_end_text.setSizePolicy(sizePolicy)
        self.t2_end_text.setText("")
        self.t2_end_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t2_end_text.setObjectName("t2_end_text")
        self.window_layout.addWidget(self.t2_end_text, 2, 3, 1, 1)
        self.window_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_label.sizePolicy().hasHeightForWidth())
        self.window_label.setSizePolicy(sizePolicy)
        self.window_label.setObjectName("window_label")
        self.window_layout.addWidget(self.window_label, 0, 0, 1, 4)
        self.gridLayout_3.addLayout(self.window_layout, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.import_investments_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_investments_button.sizePolicy().hasHeightForWidth())
        self.import_investments_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.import_investments_button.setFont(font)
        self.import_investments_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.import_investments_button.setAutoRepeat(False)
        self.import_investments_button.setObjectName("import_investments_button")
        self.gridLayout_2.addWidget(self.import_investments_button, 0, 0, 1, 1)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.play_button.setFont(font)
        self.play_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.play_button.setAutoRepeat(False)
        self.play_button.setObjectName("play_button")
        self.gridLayout_2.addWidget(self.play_button, 1, 0, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.clear_button.setFont(font)
        self.clear_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear_button.setAutoRepeat(False)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout_2.addWidget(self.clear_button, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 3)
        self.result_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_table.sizePolicy().hasHeightForWidth())
        self.result_table.setSizePolicy(sizePolicy)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(7)
        self.result_table.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(12, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(3, 1, item)
        self.gridLayout_4.addWidget(self.result_table, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Portfolio Analysis Tool"))
        self.save_config_button.setText(_translate("MainWindow", "Save Config"))
        item = self.investments_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.investments_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.investments_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.investments_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "5"))
        item = self.investments_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Investment"))
        item = self.investments_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.investments_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ticker Symbol"))
        item = self.investments_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit"))
        __sortingEnabled = self.investments_table.isSortingEnabled()
        self.investments_table.setSortingEnabled(False)
        item = self.investments_table.item(0, 0)
        item.setText(_translate("MainWindow", "SP500"))
        self.investments_table.setSortingEnabled(__sortingEnabled)
        self.result_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Running...(example)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Done.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best Profit(t1, t2): (5, 35)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best Profit / MDD(t1, t2): (5, 30)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best AR(t1, t2): (5, 35)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best MAR(t1, t2): (6, 30)</span></p></body></html>"))
        self.plot_result_button.setText(_translate("MainWindow", "Plot Result"))
        self.assets_label.setText(_translate("MainWindow", "Assets:"))
        self.starttime_label.setText(_translate("MainWindow", "Start Time:"))
        self.start_year_text.setPlaceholderText(_translate("MainWindow", "year"))
        self.start_month_text.setPlaceholderText(_translate("MainWindow", "month"))
        self.ignore_month_label.setText(_translate("MainWindow", "Ignore:"))
        self.ignore_month_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.ignore_months_label.setText(_translate("MainWindow", "months"))
        self.endtime_label.setText(_translate("MainWindow", "End Time:"))
        self.end_year_text.setPlaceholderText(_translate("MainWindow", "year"))
        self.end_month_text.setPlaceholderText(_translate("MainWindow", "month"))
        self.assets_text.setPlaceholderText(_translate("MainWindow", "100,000,000"))
        self.portfolio_label.setText(_translate("MainWindow", "Portfolio"))
        self.basis_label.setText(_translate("MainWindow", "Basis:"))
        self.selection_label.setText(_translate("MainWindow", "Selection"))
        self.basis_box.setItemText(0, _translate("MainWindow", "Profit"))
        self.basis_box.setItemText(1, _translate("MainWindow", "Profit / MDD"))
        self.basis_box.setItemText(2, _translate("MainWindow", "AR"))
        self.basis_box.setItemText(3, _translate("MainWindow", "MAR"))
        self.ranking_label.setText(_translate("MainWindow", "Ranking:"))
        self.ranking_box.setItemText(0, _translate("MainWindow", "All"))
        self.model_label.setText(_translate("MainWindow", "Model:"))
        self.config_button.setText(_translate("MainWindow", "Congfig"))
        self.model_box.setItemText(0, _translate("MainWindow", "CLA"))
        self.model_box.setItemText(1, _translate("MainWindow", "HRP"))
        self.model_box.setItemText(2, _translate("MainWindow", "Optimal F"))
        self.model_box.setItemText(3, _translate("MainWindow", "Equal Weight"))
        self.model_box.setItemText(4, _translate("MainWindow", "Equal Risk"))
        self.weighting_model_label.setText(_translate("MainWindow", "Weighting Model"))
        self.t2_end_label.setText(_translate("MainWindow", "T2 End:"))
        self.t1_start_label.setText(_translate("MainWindow", "T1 Start:"))
        self.t1_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_start_label.setText(_translate("MainWindow", "T2 Start:"))
        self.t1_end_label.setText(_translate("MainWindow", "T1 End:"))
        self.t1_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.window_label.setText(_translate("MainWindow", "Window"))
        self.import_investments_button.setText(_translate("MainWindow", "Import Investments"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        item = self.result_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.result_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.result_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.result_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.result_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.result_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.result_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.result_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.result_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "10"))
        item = self.result_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "11"))
        item = self.result_table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "12"))
        item = self.result_table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "13"))
        item = self.result_table.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "14"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t1"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "t2"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Profit"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MDD"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Profit / MDD"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "AR"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "MAR"))
        __sortingEnabled = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        item = self.result_table.item(0, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.result_table.item(0, 1)
        item.setText(_translate("MainWindow", "30"))
        item = self.result_table.item(0, 2)
        item.setText(_translate("MainWindow", "9,000,000"))
        item = self.result_table.item(0, 3)
        item.setText(_translate("MainWindow", "15,000"))
        item = self.result_table.item(1, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.result_table.item(1, 1)
        item.setText(_translate("MainWindow", "35"))
        item = self.result_table.item(2, 0)
        item.setText(_translate("MainWindow", "6"))
        item = self.result_table.item(2, 1)
        item.setText(_translate("MainWindow", "30"))
        item = self.result_table.item(3, 0)
        item.setText(_translate("MainWindow", "6"))
        item = self.result_table.item(3, 1)
        item.setText(_translate("MainWindow", "35"))
        self.result_table.setSortingEnabled(__sortingEnabled)
