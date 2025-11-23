import pandas as pd

def check_user_credentials(username, password, filepath="Kullanicilar.xlsx"):
    df = pd.read_excel(filepath)
    
    for _, row in df.iterrows():
        if row['kullanici'] == username and row['parola'] == password:
            return row['yetki']  # "admin" veya "user"
    return None
