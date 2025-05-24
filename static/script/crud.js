//new DataTable('#example');

$(document).ready(function () {
    $('#example').DataTable({
        dom: "Bfrtilp",
        buttons: [
            {
                extend: "excelHtml5",
                text: "<i class='fa-solid fa-file-excel'></i>",
                titleAttr: "Exportar a Excel",
                className: 'botonExcel btn-succes',
                
            }
        ],
        lengthMenu: [5,10,20,35],
        columnDefs: [
            {
               // orderable: false, target:[1,2,3,4,5,6,7]
            width: '10%', target: [2,4]
            }
        ],
        pageLength: 7,
        pagingType: 'simple_numbers'
        
    });
})
