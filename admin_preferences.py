from PyQt5.QtWidgets import QMainWindow
from ui.Ui_admin_pref import Ui_MainWindow

# Gerekli pencereleri import et
from admin_menu import AdminMenu
from applications_window import ApplicationsWindow
from mentor_interview_window import MentorInterviewWindow
from interviews_window import InterviewsWindow

class AdminPreferences(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buton bağlantıları
        self.ui.applications_button.clicked.connect(self.open_applications)
        self.ui.mentor_interview_button.clicked.connect(self.open_mentor_interview)
        self.ui.interviews_button.clicked.connect(self.open_interviews)
        self.ui.admin_menu_button.clicked.connect(self.open_admin_menu)
        self.ui.exit_button.clicked.connect(self.return_to_login)

    def open_applications(self):
        self.applications_window = ApplicationsWindow()
        self.applications_window.show()
        self.close()

    def open_mentor_interview(self):
        self.mentor_window = MentorInterviewWindow()
        self.mentor_window.show()
        self.close()

    def open_interviews(self):
        self.interviews_window = InterviewsWindow()
        self.interviews_window.show()
        self.close()

    def open_admin_menu(self):
        self.admin_menu = AdminMenu()
        self.admin_menu.show()
        self.close()

    def return_to_login(self):
        """Exit butonuna basıldığında login ekranına geri dön."""
        from login_window import LoginWindow  
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()