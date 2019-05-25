function localizacaoRadar() {
     
  var infoSCA = saoCarlosAgora(URL_SCA);
  var infoSCO = saoCarlosOficial(URL_SCO);
  
  writeToSheet(infoSCA, SHEET_NAME_SCA);
  writeToSheet(infoSCO, SHEET_NAME_SCO);

}
