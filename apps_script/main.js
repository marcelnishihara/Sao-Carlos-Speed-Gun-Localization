CLOUD_FUNCTION = {
  "url" : "https://us-central1-marcelnishihara.cloudfunctions.net/sao-carlos-speed-gun-position",
  "version" : "py_1.2"
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
  let date = todayIs()
  
  writeData(sheetByName, lastRow, SPREADSHEET.colDate, date)
  
  for (let speedGun in JsonPositions) {
    writeData(sheetByName, lastRow, column, JsonPositions[speedGun]["localization"])
    writeData(sheetByName, lastRow, column + 1, JsonPositions[speedGun]["speed_limit"])
    column += 2
  }
  
  writeData(sheetByName, lastRow, SPREADSHEET.colVersion, CLOUD_FUNCTION.version)
  
}


function todayIs() {
  let today = new Date()
  let day = addLeadingZero(today.getDate())
  let month = addLeadingZero(today.getMonth())
  let year = today.getYear() + 1900
  return `${day}\/${month}\/${year}`   
}

function addLeadingZero(int) {
  if (int < 10) {
    return "0" + int.toString()
  } else {
    return int.toString()
  }
}


function writeData(sheet, row, column, str) {
  sheet.getRange(row, column).setValue(str)
}
