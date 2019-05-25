function saoCarlosAgora(URL) {
  var localizacaoRadarSCA = new Array();
  
  try {
    
    var fetchUrl = UrlFetchApp.fetch(URL);
    var contentText = fetchUrl.getContentText();
    
    var regexData = /Radar \|(.*)<\/h2>/gm;
    var dataLocalizacao = regexData.exec(contentText);
    localizacaoRadarSCA.push(dataLocalizacao[1].replace(/(\s)/,''));
    
    var regexSectionRadar = /<section class="radar">(.*)<\/section>/;
    var sectionRadar = regexSectionRadar.exec(contentText);
    
    var regexRadares = /<\/big><div><h4>(.*?)<\/h4>/gm;
    
    while (regexRadares.exec(sectionRadar) != null) {
      var radares = regexRadares.exec(sectionRadar);
      localizacaoRadarSCA.push(radares[1].replace(/(\s)/,''));
    }
    
  } catch(errSCA) {
    var errMsgSCA = "São Carlos Agora\n" + errSCA;
    GmailApp.sendEmail("marcelnishihara@gmail.com", "[ERRO] Sao-Carlos-Speed-Gun-Localization", errMsgSCA);
    
  }
  
  return localizacaoRadarSCA;
  
}



function saoCarlosOficial(URL) {
  var localizacaoRadarSCO = new Array();
  
  try {
    
  var fetchUrl = UrlFetchApp.fetch(URL);
  var contentText = fetchUrl.getContentText();
  
  var regexData = /<font face="Verdana" size="3"><b>(..\/..) -.*<\/b><br><\/font>/;
  var regexRadarUm = /Radar 1 - (.*)<br>/;
  var regexRadarDois = /Radar 2 - (.*)<br>/;
  var regexRadarTres = /Radar 3 - (.*)<br>/;
  
  localizacaoRadarSCO[0] = regexData.exec(contentText)[1];
  localizacaoRadarSCO[1] = regexRadarUm.exec(contentText)[1];
  localizacaoRadarSCO[2] = regexRadarDois.exec(contentText)[1];
  localizacaoRadarSCO[3] = regexRadarTres.exec(contentText)[1];
  
  } catch (errSCO) {
    var errMsgSCO = "São Carlos Oficial\n" + errSCO;
    GmailApp.sendEmail("marcelnishihara@gmail.com", "[ERRO] Sao-Carlos-Speed-Gun-Localization", errMsgSCO);
    
  }
       
  return localizacaoRadarSCO;
}



function writeToSheet(infoToWrite, sheet) {
  var number = 1;
  
  var openSpreadsheet = SpreadsheetApp.openById(ID_SPREADSHEET);
  var sheetByName = openSpreadsheet.getSheetByName(sheet);
  var header = ['Data', 'Radar 1', 'Radar 2', 'Radar 3'];
  var lastRow = sheetByName.getLastRow() + number;

  sheetByName.getRange(1, 1, 1, header.length).setValues([header]);  
  sheetByName.getRange(lastRow, 1, 1, 4).setValues([infoToWrite]);
  sheetByName.autoResizeColumns(1, infoToWrite.length);

}
