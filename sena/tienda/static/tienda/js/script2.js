document.getElementById
("btn__iniciar-sesion").addEventListener("click", iniciarSesion);

document.getElementById
("btn__registrarse").addEventListener("click", register);

window.addEventListener("resize", anchoPagina)

//Declaracíón de variables
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var formulario_login = document.querySelector(".formulario__login")
var formulario_register = document.querySelector(".formulario__register")
var caja_trasera_login = document.querySelector(".caja__trasera-login")
var caja_trasera_register = document.querySelector(".caja__trasera-register")

function iniciarSesion(){
    if(window.innerWidth > 850) {
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "10px";
        formulario_login.style.display= "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.opacity = "0";}
    else {
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display= "block";
        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "none";
    }
}

function anchoPagina() {
    if (window.innerWidth > 850) {
        caja_trasera_login.style.display = "block";
        caja_trasera_register.style.display = "block";
    } else {
        caja_trasera_register.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display = "block";
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
    }
}

anchoPagina();
function register(){
    if (window.innerWidth > 850) {
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "410px";
        formulario_login.style.display= "none";
        caja_trasera_register.style.opacity = "0";
        caja_trasera_login.style.opacity = "1";
    }
    else {
        formulario_register.style.display = "block";
        contenedor_login_register.style.left = "0px";
        formulario_login.style.display= "none";
        caja_trasera_register.style.display = "none";
        caja_trasera_login.style.display = "block";
        caja_trasera_login.style.opacity = "1";
    }
}

/*
function mostrarAlerta(mensaje) {
    var alerta = document.createElement('div');
    alerta.classList.add('mi-alerta');
    alerta.textContent = mensaje;

    document.body.appendChild(alerta);

    setTimeout(function() {
      alerta.remove();
    }, 3000);
  }

  // Llamar a la función para mostrar la alerta


function validarUsuario() {
    let u = document.getElementById("usuario").value;
    let c = document.getElementById("contrasenaInicio").value;
    if (u == "admin") {
        if (c == "admin12345") {
            window.open("{% static 'templates/tienda/inicioAdmin.html' %}")
            event.preventDefault();
        }
    }
    else if (u == "empleado") {
        if (c == "empleado12345") {
            window.open("inicioEmpleado.html")
            event.preventDefault();
        }
    }
    else {
        mostrarAlerta("Por favor, ingresa un dato válido.");
        event.preventDefault();
    }
}*/

function toggleMostrarContrasenaRegistro() {
    var inputContrasenaRegistro = document.getElementById("contrasenaRegistro");
    var btnMostrarContrasenaRegistro = document.getElementById("btnMostrarContrasenaRegistro");
    var iconoMostrarRegistro = document.getElementById("iconoMostrarRegistro");
    var iconoOcultarRegistro = document.getElementById("iconoOcultarRegistro");

    if (inputContrasenaRegistro.type === "password") {
      inputContrasenaRegistro.type = "text";
      iconoMostrarRegistro.style.display = "none";
      iconoOcultarRegistro.style.display = "block";
    } else {
      inputContrasenaRegistro.type = "password";
      iconoMostrarRegistro.style.display = "block";
      iconoOcultarRegistro.style.display = "none";
    }
  }

  function toggleMostrarConfirmarContrasena() {
    var inputConfirmarContrasena = document.getElementById("confirmarContrasena");
    var btnMostrarConfirmarContrasena = document.getElementById("btnMostrarConfirmarContrasena");
    var iconoMostrarConfirmar = document.getElementById("iconoMostrarConfirmar");
    var iconoOcultarConfirmar = document.getElementById("iconoOcultarConfirmar");

    if (inputConfirmarContrasena.type === "password") {
      inputConfirmarContrasena.type = "text";
      iconoMostrarConfirmar.style.display = "none";
      iconoOcultarConfirmar.style.display = "block";
    } else {
      inputConfirmarContrasena.type = "password";
      iconoMostrarConfirmar.style.display = "block";
      iconoOcultarConfirmar.style.display = "none";
    }
  }

  function toggleMostrarContrasenaInicio() {
    var inputContrasenaInicio = document.getElementById("contrasenaInicio");
    var btnMostrarContrasenaInicio = document.getElementById("btnMostrarContrasenaInicio");
    var iconoMostrarInicio = document.getElementById("iconoMostrarInicio");
    var iconoOcultarInicio = document.getElementById("iconoOcultarInicio");

    if (inputContrasenaInicio.type === "password") {
      inputContrasenaInicio.type = "text";
      iconoMostrarInicio.style.display = "none";
      iconoOcultarInicio.style.display = "block";
    } else {
      inputContrasenaInicio.type = "password";
      iconoMostrarInicio.style.display = "block";
      iconoOcultarInicio.style.display = "none";
    }
  }

  // Ocultar los iconos de ocultar al cargar la página
  document.getElementById("iconoOcultarRegistro").style.display = "none";
  document.getElementById("iconoOcultarConfirmar").style.display = "none";
  document.getElementById("iconoOcultarInicio").style.display = "none";

  function validarContrasena() {
    var contrasenaRegistro = document.getElementById("contrasenaRegistro").value;
    var confirmarContrasena = document.getElementById("confirmarContrasena").value;

    if (contrasenaRegistro === confirmarContrasena) {
      // Las contraseñas coinciden, puedes realizar la acción deseada aquí
      console.log("Las contraseñas coinciden");
    } else {
      // Las contraseñas no coinciden, puedes mostrar un mensaje de error o realizar otra acción
      console.log("Las contraseñas no coinciden");
      mostrarAlerta("Las contraseñas no coinciden")
      event.preventDefault();
    }
  }
