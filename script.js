const data = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "descripcion": "La historia de la familia Buendía a lo largo de varias generaciones en el ficticio pueblo de Macondo.",
        "imagen": "cien_anos_soledad.jpg"
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "descripcion": "Una novela de ciencia ficción distópica que presenta una sociedad totalitaria vigilada por el Gran Hermano.",
        "imagen": "1984.jpg"
    },
    {
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "descripcion": "Un cuento filosófico y poético que sigue las aventuras de un joven príncipe en diferentes planetas.",
        "imagen": "el_principito.jpg"
    }
]

const booksList = document.getElementById("books")
let html = ""
data.forEach((data) => {
    html += `
<div class="col-md-4">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">${data.titulo}</h5>
            <p class="card-text">${data.autor}</p>
            <p class="card-text">${data.descripcion}</p>
            <form>
                <input >
                <a href="#" class="btn btn-primary">Agregar al carrito</a>
            </form>
        </div>
    </div>
</div>
`
})

booksList.innerHTML = html