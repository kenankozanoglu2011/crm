# backend/drive_activity.py

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.changes.readonly"
]

# Bir global değişken ya da dosyada saklanan token
_last_page_token = None

def get_drive_changes():
    global _last_page_token

    creds = service_account.Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    service = build("drive", "v3", credentials=creds)

    # Eğer _last_page_token None ise, ilk defa çağırıyoruz
    if _last_page_token is None:
        token_response = service.changes().getStartPageToken().execute()
        _last_page_token = token_response.get("startPageToken")

    # Şimdi değişiklikleri alıyoruz
    response = service.changes().list(
        pageToken=_last_page_token,
        fields="nextPageToken, newStartPageToken, changes(fileId, time, removed, file(name, mimeType))"
    ).execute()

    changes = response.get("changes", [])
    next_token = response.get("nextPageToken")
    new_start_token = response.get("newStartPageToken")

    # Eğer yeni start token varsa, sakla
    if new_start_token:
        _last_page_token = new_start_token

    results = []
    for change in changes:
        info = {
            "fileId": change.get("fileId"),
            "fileName": change.get("file", {}).get("name"),
            "mimeType": change.get("file", {}).get("mimeType"),
            "time": change.get("time"),
            "removed": change.get("removed", False),
        }
        results.append(info)

    return results
