# backend/google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_activity_records(sheet_name="Activity"):
    """
    Google Drive üzerindeki Google Sheet dosyasında, adı sheet_name olan dosyadan verileri çeker.
    Dönen değer: [{'Kolon1': değer1, ...}, ...]
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Spreadsheet adı “Activity” olmalı, Drive’da senin sheet bu adı taşımalı
    spreadsheet = client.open(sheet_name)
    sheet = spreadsheet.sheet1
    records = sheet.get_all_records()
    return records
