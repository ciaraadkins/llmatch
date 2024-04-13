import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Function to authenticate and fetch data from Google Sheets
def fetch_sheet_data():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("YourSpreadsheetName").sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Main app
def main():
    st.title("LLMatch.ai")
    st.subheader("A Customizable LLM Leaderboard")
    
    # Fetch data
    df = fetch_sheet_data()
    
    # Display data
    st.table(df)

if __name__ == "__main__":
    main()
