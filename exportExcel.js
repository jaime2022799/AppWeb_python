/*function exportTableToCsv(tblData,filename = ''){
    var csv = [];
    var rows = document.querySelectorAll("thead tr");
    
    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");
        
        for (var j = 0; j < cols.length; j++) 
            row.push(cols[j].innerText);
        
        csv.push(row.join(","));        
    }

    // Download CSV file
    downloadCSV(csv.join("n"), filename);
}
*/
const $exportar = document.querySelector("#exportar"),
$tabla = document.querySelector("#tabla");

$exportar.addEventListener("click", function() {
    let tableExport = new TableExport($tabla, {
        exportButtons: false,
        filename: "tabla de excel",
        sheetName: "tabla de excel",
    });
    let datos = tableExport.getExportData();
    let preferenciasDocumento = datos.tabla.xlsx;
    tableExport.export2file(preferenciasDocumento.data, preferenciasDocumento.mimeType, preferenciasDocumento.filename, preferenciasDocumento.fileExtension, preferenciasDocumento.merges, preferenciasDocumento.RTL, preferenciasDocumento.sheetname);
})