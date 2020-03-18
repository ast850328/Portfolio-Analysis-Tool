from Ui_ConfigWindow import Ui_ConfigWindow
from PyQt5 import QtCore, QtWidgets

class ConfigWindow(QtWidgets.QMainWindow, Ui_ConfigWindow):
    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__(parent)
        self.setupUi(self)
