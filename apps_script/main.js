CLOUD_FUNCTION = {
  "url" : "https://us-central1-marcelnishihara.cloudfunctions.net/sao-carlos-speed-gun-position",
  "version" : "py_1.3"
}


SPREADSHEET = {
  "id" : "1FBnlNFE2D0MTwgwkDqg4Qy9V6xAyBmXuuWRszKE8DrY",
  "dataBase" : "data_base",
  "colDate" : 1,
  "colVersion" : 8
}


function main() {
  let getAPIContent = UrlFetchApp.fetch(CLOUD_FUNCTION.url).getContentText()
  let JsonPositions = JSON.parse(getAPIContent)
  
  let spreadsheet = SpreadsheetApp.openById(SPREADSHEET.id)
  let sheetByName = spreadsheet.getSheetByName(SPREADSHEET.dataBase)
  let lastRow = sheetByName.getLastRow() + 1
  let column = 2
  let date = Object.keys(JsonPositions)
  
  writeData(sheetByName, lastRow, SPREADSHEET.colDate, date)
  
  for (let speedGun in JsonPositions[date]) {
    writeData(sheetByName, lastRow, column, JsonPositions[date][speedGun]["localization"])
    writeData(sheetByName, lastRow, column + 1, JsonPositions[date][speedGun]["speed_limit"])
    column += 2
  }
  
  writeData(sheetByName, lastRow, SPREADSHEET.colVersion, CLOUD_FUNCTION.version)
  
}


function writeData(sheet, row, column, str) {
  sheet.getRange(row, column).setValue(str)
}
