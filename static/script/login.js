const formOpenBtn = document.querySelector("#form-open"),
home = document.querySelector(".home"),
FormContainer = document.querySelector(".form_container"),
formCloseBtn = document.querySelector("#form_close"),
signupBtn = document.querySelector("#signup"),
loginBtn = document.querySelector("#login"),
login_now = document.querySelector('#button_registro'),
pwShowHide = document.querySelectorAll("#logo_ocultado")


formOpenBtn.addEventListener("click", () => home.classList.add("show"));
formCloseBtn.addEventListener("click", () => home.classList.remove("show"));

pwShowHide.forEach(icon => {
    icon.addEventListener("click", () => {
    let getPwInput = icon.parentElement.querySelector("input");
    if(getPwInput.type === "password")  {
        getPwInput.type = "text";
        icon.querySelector("#logo_ocultado");
        //icon.classList.replace("uil-eye-slash", "uil-eye");
    }else{
        getPwInput.type = "password";
        icon.querySelector("#logo_ocultado");
    }
    });
});


signupBtn.addEventListener("click", (e) => {
    e.preventDefault();
    FormContainer.classList.add("active");

});

loginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    FormContainer.classList.remove("active");

});

