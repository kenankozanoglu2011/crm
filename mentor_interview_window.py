# mentor_interview_window.py

import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.Ui_mentor_interview import Ui_MainWindow

class MentorInterviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Excel dosyasını oku
        try:
            self.mentor_data = pd.read_excel("Mentor.xlsx")  # aynı klasörde olmalı
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Mentor.xlsx okunamadı:\n{str(e)}")
            self.mentor_data = pd.DataFrame()

        # Bağlantılar
        self.ui.btn_preferences.clicked.connect(self.show_all_records)
        self.ui.btn_search.clicked.connect(self.search_by_name)
        self.ui.btn_p_submitted.clicked.connect(self.go_to_user_preferences)
        self.ui.btn_exit.clicked.connect(self.close)

    def populate_table(self, dataframe):
        self.ui.tableWidget.clear()

        if dataframe.empty:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)
            return

        self.ui.tableWidget.setRowCount(len(dataframe))
        self.ui.tableWidget.setColumnCount(len(dataframe.columns))
        self.ui.tableWidget.setHorizontalHeaderLabels(dataframe.columns)

        for i in range(len(dataframe)):
            for j in range(len(dataframe.columns)):
                item = QTableWidgetItem(str(dataframe.iat[i, j]))
                self.ui.tableWidget.setItem(i, j, item)

    def show_all_records(self):
        self.populate_table(self.mentor_data)

    def search_by_name(self):
        keyword = self.ui.ln_input_search.text().strip().lower()
        if not keyword:
            QMessageBox.warning(self, "Uyarı", "Lütfen aramak için bir isim girin.")
            return

        filtered_df = self.mentor_data[
            self.mentor_data["Ad Soyad"].str.lower().str.contains(keyword, na=False)
        ]
        if filtered_df.empty:
            QMessageBox.information(self, "Sonuç", "Eşleşen kayıt bulunamadı.")
        self.populate_table(filtered_df)

    def filter_by_preference(self):
        selected_option = self.ui.comboBox.currentText()
        filtered_df = self.mentor_data[
            self.mentor_data["Tercih"].fillna("").str.contains(selected_option, na=False)
        ]
        self.populate_table(filtered_df)

    def go_to_user_preferences(self):
        from user_preferences import UserPreferences  # import sadece burada
        self.user_pref_window = UserPreferences()
        self.user_pref_window.show()
        self.close()

