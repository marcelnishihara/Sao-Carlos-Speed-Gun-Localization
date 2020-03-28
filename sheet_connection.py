import gspread, re
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials
from globals import spreadsheet

def write_object_to_sheet(obj):
    data_base = get_sheet(spreadsheet["id"], spreadsheet["sheet_data_base"], "credentials.json")
    last_row = get_last_row(data_base) + 1
    today_is = date.today().strftime("%d/%m/%Y")

    for key in obj:
        reference = int(key)
        column_position, column_speed_limit = define_column_to_write(reference)
        data_base.update_cell(last_row, column_position, obj[key]["position"])
        data_base.update_cell(last_row, column_speed_limit, obj[key]["speed_limit"])

    data_base.update_cell(last_row, 1, today_is)
    data_base.update_cell(last_row, 8, "py_1.1")    


def get_sheet(ss_by_key, sheet_name, cred_file):
    client = google_sheets_authorization(cred_file)
    spreadsheet_by_key = client.open_by_key(ss_by_key)
    return get_sheet_by_name(spreadsheet_by_key, sheet_name)


def get_sheet_by_name(ss_by_key, sheet_name):
    return ss_by_key.worksheet(sheet_name)


def google_sheets_authorization(creds_file):
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    return gspread.authorize(creds)


def get_last_row(sheet):
    last_row = 0
    cols = sheet.range(1, 1, sheet.row_count, 999)

    for cell in cols:
        if cell.value != "":
            last_row = cell.row

    if last_row > 0:
        return last_row
    else:
        return last_row + 1


def define_column_to_write(addend):
    column_one = addend + addend
    column_two = column_one + 1
    return column_one, column_two
