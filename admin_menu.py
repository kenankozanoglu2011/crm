import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.Ui_admin_pref import Ui_MainWindow
#from backend.google_sheets import get_events_from_sheet 
from PyQt5 import QtWidgets 
from backend.drive_activity import get_drive_changes
#from admin_preferences import AdminPreferences

from ui.Ui_admin_menu import Ui_MainWindow  # Arayüz dosyanı import et
#from backend.google_calendar import get_events  # Etkinlikleri çekeceğimiz backend
#from backend.send_email import send_event_emails  # Mail gönderme backend

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_eventRegistration.clicked.connect(self.load_drive_activity)
        self.ui.btn_sendmail.clicked.connect(self.send_emails)
        self.ui.btn_preferences.clicked.connect(self.go_to_preferences)  # Tercihler ekranına dön
        self.ui.btn_exit.clicked.connect(self.close)  # Çıkış

    def load_drive_activity(self):
        from backend.drive_activity import get_drive_changes
        try:
            changes = get_drive_changes()
            self.populate_table(changes)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
    
    def populate_table(self, events):
        # events, örneğin: [{'Event Title': 'Mentor Meeting', 'Date': '2025‑10‑03', …}, …]
        if not events:
            return
        # Satır sayısı = kaç kayıt varsa o kadar
        self.ui.tableWidget.setRowCount(len(events))
        # Kolon sayısı = dict’te kaç anahtar varsa
        self.ui.tableWidget.setColumnCount(len(events[0]))
        # Kolon başlıklarını ayarla
        header_labels = list(events[0].keys())
        self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)

        # Verileri doldur
        for row_idx, record in enumerate(events):
            for col_idx, key in enumerate(header_labels):
                value = record.get(key, "")
                item = QtWidgets.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_idx, col_idx, item)


    def go_to_preferences(self):
        from admin_preferences import AdminPreferences  # Import burada yapılacak
        self.pref_window = AdminPreferences()
        self.pref_window.show()
        self.close()


    def load_activity_history(self):
        try:
            changes, next_token = get_drive_changes()
            self.populate_activity_table(changes)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def populate_activity_table(self, changes):
        if not changes:
            return
        # Değişiklikler bir dict listesi, anahtarlar aynı olmalı
        keys = list(changes[0].keys())
        self.ui.tableWidget.setRowCount(len(changes))
        self.ui.tableWidget.setColumnCount(len(keys))
        self.ui.tableWidget.setHorizontalHeaderLabels(keys)

        for i, rec in enumerate(changes):
            for j, key in enumerate(keys):
                item = QtWidgets.QTableWidgetItem(str(rec.get(key, "")))
                self.ui.tableWidget.setItem(i, j, item)

    def send_emails(self):
        try:
            # Önce etkinlikleri çek
            from backend.google_sheets import get_activity_records
            events = get_activity_records()

            from backend.send_email import send_event_emails
            send_event_emails(events)

            QtWidgets.QMessageBox.information(self, "Success", "Emails sent successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to send emails:\n{str(e)}")



    