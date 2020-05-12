# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(268, 228)
        ConfigDialog.setAutoFillBackground(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(ConfigDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.risk_label = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.risk_label.sizePolicy().hasHeightForWidth())
        self.risk_label.setSizePolicy(sizePolicy)
        self.risk_label.setObjectName("risk_label")
        self.gridLayout.addWidget(self.risk_label, 1, 0, 1, 1)
        self.risk_text = QtWidgets.QLineEdit(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.risk_text.sizePolicy().hasHeightForWidth())
        self.risk_text.setSizePolicy(sizePolicy)
        self.risk_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.risk_text.setObjectName("risk_text")
        self.gridLayout.addWidget(self.risk_text, 1, 1, 1, 1)
        self.cluster_method_label = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cluster_method_label.sizePolicy().hasHeightForWidth())
        self.cluster_method_label.setSizePolicy(sizePolicy)
        self.cluster_method_label.setObjectName("cluster_method_label")
        self.gridLayout.addWidget(self.cluster_method_label, 2, 0, 1, 1)
        self.cluster_method_box = QtWidgets.QComboBox(ConfigDialog)
        self.cluster_method_box.setObjectName("cluster_method_box")
        self.cluster_method_box.addItem("")
        self.cluster_method_box.addItem("")
        self.cluster_method_box.addItem("")
        self.cluster_method_box.addItem("")
        self.gridLayout.addWidget(self.cluster_method_box, 2, 1, 1, 1)
        self.order_method_label = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_method_label.sizePolicy().hasHeightForWidth())
        self.order_method_label.setSizePolicy(sizePolicy)
        self.order_method_label.setObjectName("order_method_label")
        self.gridLayout.addWidget(self.order_method_label, 3, 0, 1, 1)
        self.order_method_box = QtWidgets.QComboBox(ConfigDialog)
        self.order_method_box.setObjectName("order_method_box")
        self.order_method_box.addItem("")
        self.order_method_box.addItem("")
        self.gridLayout.addWidget(self.order_method_box, 3, 1, 1, 1)
        self.weight_method_label = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight_method_label.sizePolicy().hasHeightForWidth())
        self.weight_method_label.setSizePolicy(sizePolicy)
        self.weight_method_label.setObjectName("weight_method_label")
        self.gridLayout.addWidget(self.weight_method_label, 4, 0, 1, 1)
        self.weight_method_box = QtWidgets.QComboBox(ConfigDialog)
        self.weight_method_box.setObjectName("weight_method_box")
        self.weight_method_box.addItem("")
        self.weight_method_box.addItem("")
        self.gridLayout.addWidget(self.weight_method_box, 4, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.model_label = QtWidgets.QLabel(ConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_label.sizePolicy().hasHeightForWidth())
        self.model_label.setSizePolicy(sizePolicy)
        self.model_label.setObjectName("model_label")
        self.gridLayout.addWidget(self.model_label, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ConfigDialog)
        self.buttonBox.accepted.connect(ConfigDialog.accept)
        self.buttonBox.rejected.connect(ConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Dialog"))
        self.risk_label.setText(_translate("ConfigDialog", "Risk(%):"))
        self.risk_text.setPlaceholderText(_translate("ConfigDialog", "0"))
        self.cluster_method_label.setText(_translate("ConfigDialog", "Cluster Method:"))
        self.cluster_method_box.setItemText(0, _translate("ConfigDialog", "single"))
        self.cluster_method_box.setItemText(1, _translate("ConfigDialog", "complete"))
        self.cluster_method_box.setItemText(2, _translate("ConfigDialog", "average"))
        self.cluster_method_box.setItemText(3, _translate("ConfigDialog", "ward"))
        self.order_method_label.setText(_translate("ConfigDialog", "Order Method:"))
        self.order_method_box.setItemText(0, _translate("ConfigDialog", "top-down"))
        self.order_method_box.setItemText(1, _translate("ConfigDialog", "bisection"))
        self.weight_method_label.setText(_translate("ConfigDialog", "Weight Method:"))
        self.weight_method_box.setItemText(0, _translate("ConfigDialog", "var"))
        self.weight_method_box.setItemText(1, _translate("ConfigDialog", "equal"))
        self.model_label.setText(_translate("ConfigDialog", "CLA model"))

    def set_model_label(self, model_name):
        self.model_label.setText(model_name + ' model')

    def limit_column(self, model_name):
        if model_name == 'HRP':
            pass
        else:
            self.cluster_method_box.setEnabled(False)
            self.order_method_box.setEnabled(False)
            self.weight_method_box.setEnabled(False)

    def get_model_config(self):
        config_model = {
            'cluster_method': self.cluster_method_box.currentText(),
            'order_method': self.order_method_box.currentText(),
            'weight_method': self.weight_method_box.currentText(),
            'risk': float(self.risk_text.text()) / 100.0
        }
        return config_model
