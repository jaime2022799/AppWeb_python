const submit = document.getElementsByClassName("form-contact")[0];


const nombre = document.getElementById("nombre");
const apellido = document.getElementById("apellido");
const tipo_evento = document.getElementById("tipo_evento");
const contacto = document.getElementById("Contacto");
const direccion = document.getElementById("direccion");
const email = document.getElementById("Email");



submit.addEventListener("submit", (e)=> {

    console.log("clickend")

    // el html para el body 
    let ebody = `
            <b>Nombre: </b>${nombre.value}
            <br>
            <b>Apellido: </b>${apellido.value}
            <br>
            <b>Tipo_solicitud: </b>${tipo_evento.value}
            <br>
            <b>Contacto: </b>${contacto.value}
            <br>
            <b>Direccion: </b>${direccion.value}
            <br>
            <b>Email: </b>${email.value}
            <br>
            <br>
            `

    Email.send({
        SecureToken : "e3f85831-303d-4309-a248-d30c3b550ad8",
        To : 'jaimeretamal47@gmail.com',
        From : "jaimeretamal47@gmail.com",
        Subject : "Cotizacion formulario 2024" ,
        Body : ebody + 
        "Estimado(a) Esperando se encuentre bien  se a notificado los datos correspondientes del formulario , nos pondremos en contacto con usted "
        
    }).then(
        message => swal('Genial...','se a enviado una notificacion de su Formulario de cotizacion','success')
    );

    


    e.preventDefault();

})