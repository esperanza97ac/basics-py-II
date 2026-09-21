from libreria import agregar_libro, listar_libros, libros_por_autor, existe_libro


# Añade una colección de libros
libros = [
    agregar_libro("Cien años de soledad", "Gabriel García Márquez"),
    agregar_libro("1984", "George Orwell"),
    agregar_libro("El principito", "Antoine de Saint-Exupéry"),
]

# Muestra la colección de libros creada
print("Colección de libros:", listar_libros(libros))

# Busca un libro por el autor
autor = "George Orwell"
print(f"Libros de {autor}:", libros_por_autor(libros, autor))

# Verifica si un libro está disponible
titulo = "1984"
if existe_libro(libros, titulo):
    print(f"El libro '{titulo}' está disponible.")
else:
    print(f"El libro '{titulo}' no está disponible.")

    