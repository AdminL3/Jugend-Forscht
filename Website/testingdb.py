import sqlite3
import pandas as pd
import streamlit as st
import requests

# SQLite-Datenbank aus GitHub herunterladen
db_url = "https://raw.githubusercontent.com/AdminL3/Jugend-Forscht/main/Database/Wordcount/Guardian.db"
db_path = "Guardian.db"

# Datei herunterladen
response = requests.get(db_url)
with open(db_path, "wb") as file:
    file.write(response.content)

# Verbindung zur heruntergeladenen SQLite-Datenbank herstellen
conn = sqlite3.connect(db_path)

# Beispielabfrage
query = "SELECT * FROM politics"
try:
    df = pd.read_sql_query(query, conn)
    st.dataframe(df)
except Exception as e:
    st.error(f"Fehler bei der Abfrage: {e}")
finally:
    conn.close()
