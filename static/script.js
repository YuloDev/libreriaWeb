// Obtener todos los botones "Agregar" en el documento
const botonesAgregar = document.querySelectorAll(".btn-primary");

// Iterar a través de los botones y agregar un controlador de eventos a cada uno
botonesAgregar.forEach(function (boton) {
  boton.addEventListener("click", function () {
    // Obtener información personalizada del botón clickeado
    var bookName = boton.getAttribute("data-book-name");
    var bookCategory = boton.getAttribute("data-book-category");
    var bookDescription = boton.getAttribute("data-book-description");
    const modalBookName = document.getElementById("name");
    const modalCategory = document.getElementById("category");
    const modalDescription = document.getElementById("description");
    const modalAmount = document.querySelector(".form-control");
    let cartBooks = JSON.parse(localStorage.getItem("cart-books"));
    modalBookName.value = bookName;
    modalCategory.value = bookCategory;
    modalDescription.value = bookDescription;

    const botonAceptar = document.querySelector(".btn-success");

    botonAceptar.addEventListener("click", () => {
      cartBooks.push({
        titulo: modalBookName.value,
        categoria: modalCategory.value,
        Descripcion: modalDescription.value,
        cantidad: modalAmount.value,
      });
      localStorage.setItem("cart-books", cartBooks);
      Swal.fire('Libro agregado con exito')
      console.log(localStorage.setItem("cart-books", JSON.stringify(cartBooks)));
    });
  });
});
