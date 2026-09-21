from libreria import agregar_libro, listar_libros, buscar_libro, existe_libro


# Añade una colección de libros
libros = []
libros.append(agregar_libro("Cien años de soledad", "Gabriel García Márquez"))
libros.append(agregar_libro("1984", "George Orwell"))
libros.append(agregar_libro("El principito", "Antoine de Saint-Exupéry"))

# Muestra la colección de libros creada
print(listar_libros(libros))

# Busca un libro por el autor
autor = "George Orwell"
resultado = [libro for libro in libros if libro["autor"] == autor]
print(resultado)

# Verifica si un libro está disponible
titulo = "1984"
if existe_libro(libros, titulo):
    print(f"El libro '{titulo}' está disponible.")
else:
    print(f"El libro '{titulo}' no está disponible.")

    