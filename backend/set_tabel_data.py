from backend.list_files import list_files
from backend.download_file import download_file 
from backend.read_xlsx import read_xlsx
from PyQt5 import QtWidgets 

def set_tabel_data(window, file_name):
    drive_files = list_files()

    file_id = None

    for file in drive_files:
        if file['name'] == file_name:
            file_id = file['id']
            download_file(file_id)
            break

    rows = read_xlsx(file_name)
    headers = [header for header in rows[0] if header is not None]
    window.tableWidget.clear()
    window.tableWidget.setColumnCount(len(headers))
    window.tableWidget.setRowCount(len(rows) - 1)

    for i, header in enumerate(headers):
        if header == 'None' or header is None:
            continue

        item = QtWidgets.QTableWidgetItem()
        item.setText(header)
        window.tableWidget.setHorizontalHeaderItem(i, item)

    for i in range(1, len(rows)):
        for j in range(len(headers)):
            if rows[i][j] is None:
                continue

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(rows[i][j]))
            window.tableWidget.setItem(i - 1, j, item)

