import sqlite3
import pandas as pd
import streamlit as st

# SQLite-Datenbank aus einem GitHub-Repo laden
db_url = "https://raw.githubusercontent.com/AdminL3/Jugend-Forscht/main/Database/Wordcount/Guardian.db"
conn = sqlite3.connect("database.db")

# Beispielabfrage
query = "SELECT * FROM politics"
df = pd.read_sql_query(query, conn)
st.dataframe(df)
