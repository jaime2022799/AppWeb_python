


$("#formulario_contacto").validate({
        rules: {
            nombre: {
                required: true,
                minLength: 3,
                maxlength: 30
            },
            apellido: {
                required: true,
                minLength: 3,
                maxlength: 30
            },
            Email: {
                required: true,
                Email: true,
                terminaPor: "gmail.com"
            },
            tipo_evento: {
                required: true
            },
            direccion: {
                required: true,
                minLength: 5,
                maxlength: 50
            },
            Contacto: {
                required: true
    
            }
        }
})





$("#guardar").click(function() {
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let tipo_evento = $("#tipo_evento").val()
    let celular = $("#Contacto").val()
    let direccion = $("#direccion").val()
    let correo = $("#Email").val()


    //console.log(nombre)
})