# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.plot_result_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_result_button.sizePolicy().hasHeightForWidth())
        self.plot_result_button.setSizePolicy(sizePolicy)
        self.plot_result_button.setObjectName("plot_result_button")
        self.gridLayout_7.addWidget(self.plot_result_button, 0, 1, 1, 1)
        self.save_config_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_config_button.sizePolicy().hasHeightForWidth())
        self.save_config_button.setSizePolicy(sizePolicy)
        self.save_config_button.setObjectName("save_config_button")
        self.gridLayout_7.addWidget(self.save_config_button, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 2, 0, 1, 1)
        self.result_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_textBrowser.sizePolicy().hasHeightForWidth())
        self.result_textBrowser.setSizePolicy(sizePolicy)
        self.result_textBrowser.setMinimumSize(QtCore.QSize(760, 192))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.result_textBrowser.setFont(font)
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.gridLayout_3.addWidget(self.result_textBrowser, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.result_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
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
        self.gridLayout_3.addWidget(self.result_table, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.t2_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_text.sizePolicy().hasHeightForWidth())
        self.t2_end_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t2_end_text.setFont(font)
        self.t2_end_text.setAcceptDrops(True)
        self.t2_end_text.setText("")
        self.t2_end_text.setObjectName("t2_end_text")
        self.gridLayout_2.addWidget(self.t2_end_text, 2, 3, 1, 1)
        self.t1_end_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_text.sizePolicy().hasHeightForWidth())
        self.t1_end_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t1_end_text.setFont(font)
        self.t1_end_text.setAcceptDrops(True)
        self.t1_end_text.setObjectName("t1_end_text")
        self.gridLayout_2.addWidget(self.t1_end_text, 1, 3, 1, 1)
        self.t2_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_label.sizePolicy().hasHeightForWidth())
        self.t2_start_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t2_start_label.setFont(font)
        self.t2_start_label.setObjectName("t2_start_label")
        self.gridLayout_2.addWidget(self.t2_start_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.t1_start_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_label.sizePolicy().hasHeightForWidth())
        self.t1_start_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t1_start_label.setFont(font)
        self.t1_start_label.setObjectName("t1_start_label")
        self.gridLayout_2.addWidget(self.t1_start_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.t2_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_start_text.sizePolicy().hasHeightForWidth())
        self.t2_start_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t2_start_text.setFont(font)
        self.t2_start_text.setAcceptDrops(True)
        self.t2_start_text.setText("")
        self.t2_start_text.setObjectName("t2_start_text")
        self.gridLayout_2.addWidget(self.t2_start_text, 2, 1, 1, 1)
        self.assets_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_text.sizePolicy().hasHeightForWidth())
        self.assets_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.assets_text.setFont(font)
        self.assets_text.setAcceptDrops(True)
        self.assets_text.setObjectName("assets_text")
        self.gridLayout_2.addWidget(self.assets_text, 0, 3, 1, 1)
        self.t1_start_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_start_text.sizePolicy().hasHeightForWidth())
        self.t1_start_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t1_start_text.setFont(font)
        self.t1_start_text.setAcceptDrops(True)
        self.t1_start_text.setText("")
        self.t1_start_text.setObjectName("t1_start_text")
        self.gridLayout_2.addWidget(self.t1_start_text, 1, 1, 1, 1)
        self.t2_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_end_label.sizePolicy().hasHeightForWidth())
        self.t2_end_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t2_end_label.setFont(font)
        self.t2_end_label.setObjectName("t2_end_label")
        self.gridLayout_2.addWidget(self.t2_end_label, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.t1_end_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_end_label.sizePolicy().hasHeightForWidth())
        self.t1_end_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.t1_end_label.setFont(font)
        self.t1_end_label.setObjectName("t1_end_label")
        self.gridLayout_2.addWidget(self.t1_end_label, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.assets_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_label.sizePolicy().hasHeightForWidth())
        self.assets_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.assets_label.setFont(font)
        self.assets_label.setObjectName("assets_label")
        self.gridLayout_2.addWidget(self.assets_label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.import_data_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_data_button.sizePolicy().hasHeightForWidth())
        self.import_data_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.import_data_button.setFont(font)
        self.import_data_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.import_data_button.setAutoRepeat(False)
        self.import_data_button.setObjectName("import_data_button")
        self.gridLayout_2.addWidget(self.import_data_button, 0, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setMinimumSize(QtCore.QSize(68, 0))
        self.play_button.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.gridLayout_6.addWidget(self.play_button, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(74, 0))
        self.clear_button.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.clear_button.setFont(font)
        self.clear_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear_button.setAutoRepeat(False)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout_6.addWidget(self.clear_button, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.select_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_label.sizePolicy().hasHeightForWidth())
        self.select_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.select_label.setFont(font)
        self.select_label.setObjectName("select_label")
        self.gridLayout_4.addWidget(self.select_label, 0, 0, 1, 1)
        self.model_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_box.sizePolicy().hasHeightForWidth())
        self.model_box.setSizePolicy(sizePolicy)
        self.model_box.setObjectName("model_box")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.model_box.addItem("")
        self.gridLayout_4.addWidget(self.model_box, 1, 1, 1, 2)
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
        self.gridLayout_4.addWidget(self.model_label, 1, 0, 1, 1)
        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayout_4.addWidget(self.config_button, 1, 3, 1, 1, QtCore.Qt.AlignVCenter)
        self.select_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_box.sizePolicy().hasHeightForWidth())
        self.select_box.setSizePolicy(sizePolicy)
        self.select_box.setObjectName("select_box")
        self.select_box.addItem("")
        self.gridLayout_4.addWidget(self.select_box, 0, 1, 1, 2)
        self.target_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_box.sizePolicy().hasHeightForWidth())
        self.target_box.setSizePolicy(sizePolicy)
        self.target_box.setObjectName("target_box")
        self.target_box.addItem("")
        self.target_box.addItem("")
        self.target_box.addItem("")
        self.target_box.addItem("")
        self.target_box.addItem("")
        self.gridLayout_4.addWidget(self.target_box, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.stocks_listView = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stocks_listView.sizePolicy().hasHeightForWidth())
        self.stocks_listView.setSizePolicy(sizePolicy)
        self.stocks_listView.setObjectName("stocks_listView")
        self.gridLayout_5.addWidget(self.stocks_listView, 0, 0, 2, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plot_result_button.setText(_translate("MainWindow", "Plot Result"))
        self.save_config_button.setText(_translate("MainWindow", "Save Config"))
        self.result_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Running...(example)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Done.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best Equity(t1, t2): (5, 35)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best MDD(t1, t2): (6, 30)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best Equity / MDD(t1, t2): (5, 30)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best CAGR(t1, t2): (5, 35)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Best MAR(t1, t2): (6, 30)</span></p></body></html>"))
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
        item.setText(_translate("MainWindow", "Equity"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MDD"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Equity / MDD"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CAGR"))
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
        self.t2_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t1_end_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_start_label.setText(_translate("MainWindow", "T2 Start:"))
        self.t1_start_label.setText(_translate("MainWindow", "T1 Start:"))
        self.t2_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.assets_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t1_start_text.setPlaceholderText(_translate("MainWindow", "0"))
        self.t2_end_label.setText(_translate("MainWindow", "T2 End:"))
        self.t1_end_label.setText(_translate("MainWindow", "T1 End:"))
        self.assets_label.setText(_translate("MainWindow", "Assets:"))
        self.import_data_button.setText(_translate("MainWindow", "Import Data"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.select_label.setText(_translate("MainWindow", "Select:"))
        self.model_box.setItemText(0, _translate("MainWindow", "HRP"))
        self.model_box.setItemText(1, _translate("MainWindow", "CLA"))
        self.model_box.setItemText(2, _translate("MainWindow", "Equal"))
        self.model_label.setText(_translate("MainWindow", "Model:"))
        self.config_button.setText(_translate("MainWindow", "Congfig"))
        self.select_box.setItemText(0, _translate("MainWindow", "All"))
        self.target_box.setItemText(0, _translate("MainWindow", "Equity"))
        self.target_box.setItemText(1, _translate("MainWindow", "MDD"))
        self.target_box.setItemText(2, _translate("MainWindow", "Equity / MDD"))
        self.target_box.setItemText(3, _translate("MainWindow", "CAGR"))
        self.target_box.setItemText(4, _translate("MainWindow", "MAR"))
