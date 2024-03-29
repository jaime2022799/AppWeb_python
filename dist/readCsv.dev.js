"use strict";

var excel_file = document.getElementById('cargar'); //const reader = excel_file.reader;

excel_file.addEventListener('change', function (event) {
  var reader = new FileReader();
  reader.readAsArrayBuffer(event.target.files[0]);

  reader.onload = function (event) {
    var data = new Uint8Array(reader.result);
    var work_book = XLSX.read(data, {
      type: 'array'
    });
    var sheet_name = work_book.SheetNames;
    var sheet_data = XLSX.utils.sheet_to_json(work_book.Sheets[sheet_name[0]], {
      header: 1
    });

    if (sheet_data.length > 0) {
      var table_output = '<table class="table table-dark">';

      for (var row = 0; row < sheet_data.length; row++) {
        table_output += '<tr>';

        for (var cell = 0; cell < sheet_data[row].length; cell++) {
          table_output += '<td>' + sheet_data[row][cell] + '</td>';
        }

        table_output += '</tr>';
      }

      table_output += '</table>';
      document.getElementById('tabla').innerHTML = table_output;
    }
  };
}); //export {excel_file}