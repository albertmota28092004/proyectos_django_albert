

function validarUsuario() {
    let u = document.getElementById("usuario").value;
    let c = document.getElementById("contraseña").value;
    if (u == "admin") {
        if (c == "admin12345") {
            window.open("inicioAdmin.html")
        }
    }
    else if (u == "empleado") {
        if (c == "empleado12345") {
            window.open("inicioEmpleado.html")
        }
    }
    else {
        alert("Por favor, ingresa un dato válido.");
        event.preventDefault();
    }
}

function registrarUsuario() {
    let c = document.getElementById("contraseña_registro").value;
    let cc = document.getElementById("confirmar_contraseña_registro").value;
    if (c == cc) {
        window.open()
    }
    else {
        alert("Las contraseñas no coinciden");
        event.preventDefault();
    }
}

function customAlert() {
    var overlay = document.createElement('div');
    overlay.classList.add('alert-overlay');

    var box = document.createElement('div');
    box.classList.add('alert-box');

    var message = document.createElement('div');
    message.classList.add('alert-message');
    message.textContent = 'Este es un mensaje de alerta personalizada.';

    var button = document.createElement('button');
    button.classList.add('alert-button');
    button.textContent = 'Aceptar';
    button.addEventListener('click', function() {
    overlay.remove();
    });

    box.appendChild(message);
    box.appendChild(button);
    overlay.appendChild(box);
    document.body.appendChild(overlay);
}

function confirmar_eliminar(url) {
    if(confirm("¿Está seguro de eliminar el registro?")){
        location.href = url;
    }
}
