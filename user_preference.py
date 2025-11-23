from PyQt5.QtWidgets import QMainWindow
from ui.Ui_user_pref import Ui_MainWindow  # UI dosyasının doğru yolunu kullan
from applications_window import ApplicationsWindow
from mentor_interview_window import MentorInterviewWindow
from interviews_window import InterviewsWindow

class UserPreferences(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buton sinyallerini fonksiyonlara bağla
        self.ui.applications_button.clicked.connect(self.open_applications)
        self.ui.mentor_interview_button.clicked.connect(self.open_mentor_interview)
        self.ui.interviews_button.clicked.connect(self.open_interviews)
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

    def return_to_login(self):
        """Exit butonuna basıldığında login ekranına geri dön."""
        from login_window import LoginWindow  
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()