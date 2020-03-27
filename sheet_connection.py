import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1FBnlNFE2D0MTwgwkDqg4Qy9V6xAyBmXuuWRszKE8DrY").worksheet("LOCALIZACAO_RADAR_SCA")
data = sheet.get_all_values()

