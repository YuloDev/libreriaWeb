const tbody = document.querySelector("tbody");
let cartBooks = JSON.parse(localStorage.getItem("cart-books")) || []; // Inicializa con un arreglo vacío si no hay datos en el localStorage

function renderTable() {
  let html = "";
  cartBooks.forEach((element, index) => {
    html += `
      <tr>
          <td>${element.titulo}</td>
          <td>${element.categoria}</td>
          <td>${element.Descripcion}</td>
          <td>${element.cantidad}</td>
          <td>
              <button class="btn btn-danger" onclick="deleteRow(${index})">Eliminar</button>
          </td>
      </tr>
    `;
  });
  tbody.innerHTML = html;
}

function deleteRow(index) {
  cartBooks.splice(index, 1); // Elimina el libro en el índice especificado
  localStorage.setItem("cart-books", JSON.stringify(cartBooks)); // Actualiza el localStorage
  renderTable(); // Vuelve a renderizar la tabla
}

renderTable(); // Llama a la función para mostrar la tabla inicialmente

const botonConfirmar = document.querySelector(".btn-success");

botonConfirmar.addEventListener("click", function () {
  // Prepara los datos para enviar en el cuerpo de la solicitud POST
  const data = {
    libros: cartBooks,
  };

  // Convierte el arreglo de libros en una cadena JSON para incluirlo en la URL
  const librosJSON = encodeURIComponent(JSON.stringify(cartBooks));

  // Construye la URL con los parámetros de los libros
  const url = `/cart?libros=${librosJSON}`;

  // Redirige a la página /cart con los datos en la URL
  window.location.href = url;
  // // Realiza la solicitud POST utilizando fetch
  // fetch("/cart", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  //   body: JSON.stringify(data),
  // })
  //   .then((response) =>{
  //     if (response.ok) {
  //       // Si la respuesta del servidor es exitosa (código 200), muestra un alert
  //       Swal.fire("¡La reserva se realizó con éxito!")
  //       // Puedes redirigir al usuario o hacer cualquier otra acción deseada
  //     } else {
  //       // Si la respuesta no es exitosa, muestra un mensaje de error
  //       Swal.fire("Error al realizar la reserva.")
  //     }
  //   })
  //   .catch((error) => {
  //     console.error("Error al realizar la solicitud POST:", error);
  //   });
});
