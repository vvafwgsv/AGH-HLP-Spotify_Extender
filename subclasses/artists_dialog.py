from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from py_source.custom_dialog import Ui_Dialog

class artists_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.exit_dialog.clicked.connect(self.close())

        self.show()
