import streamlit as st
import mysql.connector
import pandas as pd
import requests

st.title('📚 BookScape Explorer')
st.header('Clickhere')

def get_db_connection():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        port=int(st.secrets["DB_PORT"]), 
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"]
    )

def fetch_books_from_db():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books LIMIT 1000") 
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books


if st.button("Fetch Books Data"):
    books_data = fetch_books_from_db()
    
    if books_data:
        df = pd.DataFrame(books_data)
        st.success(f" Loaded {len(df)} books successfully!")
        st.dataframe(df) 
    else:
        st.warning("⚠ No books found in the database!")