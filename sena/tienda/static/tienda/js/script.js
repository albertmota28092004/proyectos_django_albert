function validarUsuario() {
    let u = document.getElementById("usuario").value;
    let c = document.getElementById("contraseña").value;
    if (u == "admin") {
        if (c == "admin12345") {
            window.open("../html/inicioAdmin.html")
        }
        else {
            alert("Contraseña incorrecta. Ingrésala nuevamente.");
            event.preventDefault();
        }
    }
    else if (u == "empleado") {
        if (c == "empleado12345") {
            window.open("../html/inicioEmpleado.html")
        }
        else {
            alert("Contraseña incorrecta. Ingrésala nuevamente.");
            event.preventDefault();
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

/*
fetch('base.html')
.then(response => response.text())
.then(data => {
    document.getElementById('base-container').innerHTML = data;
});

fetch('base_admin.html')
.then(response => response.text())
.then(data => {
    document.getElementById('base-container_admin').innerHTML = data;
});*/

/*document.addEventListener("DOMContentLoaded", function () {
    const especieSelect = document.getElementById("especie");
    const tamañoSelect = document.getElementById("tamaño");
    const productos = document.querySelectorAll(".producto");

    function filtrarProductos() {
        const especieFiltro = especieSelect.value;
        const tamañoFiltro = tamañoSelect.value;

        productos.forEach(producto => {
            const especieProducto = producto.classList.contains(especieFiltro);
            const tamañoProducto = producto.classList.contains(tamañoFiltro);

            if ((especieFiltro === "todos" || especieProducto) &&
                (tamañoFiltro === "todos" || tamañoProducto)) {
                producto.style.display = "block";
            } else {
                producto.style.display = "none";
            }
        });
    }

    especieSelect.addEventListener("change", filtrarProductos);
    tamañoSelect.addEventListener("change", filtrarProductos);

    // Filtrar productos al cargar la página
    filtrarProductos();
});
*/
/*-----------------------------AGENDAR CITA----------------------------*/

function validarDatos() {
    // Obtener referencias a los campos del formulario
    var nombres = document.getElementById("nombres").value;
    var apellidos = document.getElementById("apellidos").value;
    var tipoDocumento = document.getElementById("tipodocumento").value;
    var numeroDocumento = document.getElementById("numerodocumento").value;
    var fechaNacimiento = document.getElementById("fechanacimiento").value;
    var nombreMascota = document.getElementById("nombremascota").value;
    var fechaNacimientoMascota = document.getElementById("fechanacimientomascota").value;
    var especieMascota = document.getElementById("especiemascota").value;
    var razaMascota = document.getElementById("razamascota").value;
    var sede = document.getElementById("sede").value;
    var servicio = document.getElementById("servicio").value;
    var dia = document.getElementById("dia").value;
    var hora = document.getElementById("hora").value;
    var profesional = document.getElementById("profesional").value;

    // Verificar si algún campo está vacío
    if (
      nombres.trim().length == 0 ||
      apellidos.trim().length == 0 ||
      tipoDocumento.trim().length == 0 ||
      numeroDocumento.trim().length == 0 ||
      fechaNacimiento.trim().length == 0 ||
      nombreMascota.trim().length == 0 ||
      fechaNacimientoMascota.trim().length == 0 ||
      especieMascota.trim().length == 0 ||
      razaMascota.trim().length == 0 ||
      sede.trim().length == 0 ||
      servicio.trim().length == 0 ||
      dia.trim().length == 0 ||
      hora.trim().length == 0 ||
      profesional.trim().length == 0
    ) {
      mostrarAlerta("Por favor, completa todos los campos.", "rojo");
    } else {
      // Todos los campos están llenos, se puede enviar el formulario
      mostrarAlerta("Cita agendada con éxito. Los campos han sido limpiados.", "verde");
      limpiarCampos();
    }
  }

  function limpiarCampos() {
    // Obtener referencias a los campos del formulario
    document.getElementById("nombres").value = "";
    document.getElementById("apellidos").value = "";
    document.getElementById("tipodocumento").value = "";
    document.getElementById("numerodocumento").value = "";
    document.getElementById("fechanacimiento").value = "";
    document.getElementById("nombremascota").value = "";
    document.getElementById("fechanacimientomascota").value = "";
    document.getElementById("especiemascota").value = "";
    document.getElementById("razamascota").value = "";
    document.getElementById("sede").value = "";
    document.getElementById("servicio").value = "";
    document.getElementById("dia").value = "";
    document.getElementById("hora").value = "";
    document.getElementById("profesional").value = "";
  }

  function mostrarAlerta(mensaje, color) {
    var alerta = document.createElement('div');
    alerta.classList.add('mi-alerta');
    alerta.textContent = mensaje;

    // Establecer el color de fondo y texto según el parámetro 'color'
    if (color === "rojo") {
      alerta.style.backgroundColor = "#FF0000";
      alerta.style.color = "#FFFFFF";
    } else if (color === "verde") {
      alerta.style.backgroundColor = "#00FF00";
      alerta.style.color = "#000000";
    }

    document.body.appendChild(alerta);

    setTimeout(function () {
      alerta.remove();
    }, 3000);
  }

  function validarDia() {
    var diaInput = document.getElementById("dia");
    var diaSeleccionado = new Date(diaInput.value);

    // Obtener el día de la semana (0 = domingo, 1 = lunes, ..., 6 = sábado)
    var diaSemana = diaSeleccionado.getDay();

    // Deshabilitar los domingos
    if (diaSemana === 6) {
      mostrarAlerta("No se pueden seleccionar citas los domingos. Por favor, elige otro día.");
      diaInput.value = "";
    }
  }

  /*document.getElementById("text2").style.display = "none";
  document.getElementById("text3").style.display = "none";*/

  function siguiente() {
    let text1 = document.getElementById("text1");
    let text2 = document.getElementById("text2");
    let text3 = document.getElementById("text3");

    if (text1.style.display !== "none") {
      text1.style.display = "none";
      text2.style.display = "block";
    } else if (text2.style.display !== "none") {
      text2.style.display = "none";
      text3.style.display = "block";
    }
  }

  function anterior() {
    let text1 = document.getElementById("text1");
    let text2 = document.getElementById("text2");
    let text3 = document.getElementById("text3");

    if (text3.style.display !== "none") {
      text3.style.display = "none";
      text2.style.display = "block";
    } else if (text2.style.display !== "none") {
      text2.style.display = "none";
      text1.style.display = "block";
    }
  }

  function mostrar(numero) {
    let text1 = document.getElementById("text1");
    let text2 = document.getElementById("text2");
    let text3 = document.getElementById("text3");

    if (numero == 1) {
      text1.style.display = "block";
      text2.style.display = "none";
      text3.style.display = "none";
    } else if (numero == 2) {
      text2.style.display = "block";
      text1.style.display = "none";
      text3.style.display = "none";
    } else if (numero == 3) {
      text3.style.display = "block";
      text2.style.display = "none";
      text1.style.display = "none";
    }
   }

  function ver_carrito(url_django){
        $.ajax({
            url: url_django
        })
        .fail(function( result ) {
            alert("Error: " + result);
        })
        .done(function( result ) {
            cuerpo = $('#respuesta_carrito');
            // Sobreescribir el contenido del offcanvas
            cuerpo.html(result)
            // Mostrar el OffCanvas
            const myOffcanvas = $('#offcanvasRight');
            myOffcanvas.offcanvas('toggle');
        });

  }

$( document ).ready(function() {
    console.log( "ready!" );
    // abrir off canvas en caso especial después de agregar producto
    var pathname = window.location.pathname;
    pathname = pathname.split("/")
    if (pathname[2] == "si"){
        ver_carrito("/carrito_listar/")
    }
});

/*--------------------------------------*/

function actualizar_totales(id, cantidad, precio){
    console.log(`Id producto ${id} - Cantidad ${cantidad} - Precio ${precio}`)

    id_subtotal = document.getElementById("subtotal_"+id)
    total_carrito = document.getElementById("total_carrito")

    id_subtotal.innerHTML = "$"+ (cantidad * precio).toLocaleString()

    precios = document.getElementsByName("precios")
    cantidades = document.getElementsByName("cantidades")

    total = 0
    for (obj=0; obj < precios.length; obj++){
        total = total + (precios[obj].value * cantidades[obj].value);
    }

    total_carrito.innerHTML = `Total: $${total.toLocaleString()}`
}

function actualizar_carrito(url_django, id, cantidad){
    loader = $('#loading_cc');
    loader.removeClass("d-none")
    loader.addClass("d-block")

    $.ajax({
      url: url_django,
      method: "GET",
      data: { "id": id, "cantidad": cantidad }
    })
    .fail(function( result ) {
        alert( "Error: " + result );
        loader.removeClass("d-block")
        loader.addClass("d-none")
    })
    .done(function( result ) {
        loader.removeClass("d-block")
        loader.addClass("d-none")
    });
}


