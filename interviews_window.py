from PyQt5.QtWidgets import QMainWindow
from ui.Ui_interviews import Ui_MainWindow

class InterviewsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
