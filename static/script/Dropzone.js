Dropzone.autoDiscover = false;

let srcImages= [];

const csvDropzone = new Dropzone(".dropzone", {
    url: "/index",
    acceptedFiles: ".xlsx , .csv , .png",
    maxFileSize: '10MB',
    addRemoveLinks: true,
    dictRemoveFile: 'Quitar'
    /*init: function () {
        this.on("success", function (file, response){
            console.log(response)
        })
    }*/
})

csvDropzone.on("addedfile", file => {
   // console.log(file);
   srcImages.push(file)
})

/*document.getElementById('enviar').addEventListener('click', () => {
    console.log(srcImages);
})*/



