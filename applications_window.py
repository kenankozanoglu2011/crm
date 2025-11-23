from PyQt5.QtWidgets import QMainWindow
from ui.Ui_applications import Ui_MainWindow  # UI dosyanın adı

class ApplicationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
