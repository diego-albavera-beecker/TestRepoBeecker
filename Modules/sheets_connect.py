import google.auth
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


# JSON File path
SERVICE_ACCOUNT_FILE = r"../Controllers/client_secret.json"

# XChecks for scopes in the spreadsheet
SCOPES_URL = ['https://www.googleapis.com/auth/spreadsheets']

credencial_user = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES_URL
    )
# Spreadsheet ID to use and modify
#SPREADSHEETS_ID = "1Y4y0HzIXyS2CYrO-hAW3vmAPeJBXJXzm0DHz7_U3IMM"
SPREADSHEETS_ID = "1olBnAl_A0LVuDrjYDoHWeMcqVKjo8bLooEpD089ZmtY"

# Selected range in the spreadsheet
RANGE_NAME = "Sheet1!A1:A2"

# Google sheets conection
service_account = build("sheets",'v4',credentials=credencial_user)
data_sheet = service_account.spreadsheets()