from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.Ui_Login import Ui_MainWindow
from backend.user_auth import check_user_credentials

from admin_preferences import AdminPreferences
from user_preferences import UserPreferences

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.login)
        self.ui.exit_button.clicked.connect(self.close)

    def login(self):
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        role = check_user_credentials(username, password)

        if role == "admin":
            self.pref_window = AdminPreferences()
            self.pref_window.show()
            self.close()

        elif role == "user":
            self.pref_window = UserPreferences()
            self.pref_window.show()
            self.close()

        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")
