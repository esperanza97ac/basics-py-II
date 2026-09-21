"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

def agregar_libro(titulo, autor):
    return {"titulo": titulo, "autor": autor}

libro1 = agregar_libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = agregar_libro("1984", "George Orwell")
libro3 = agregar_libro("El principito", "Antoine de Saint-Exupéry")
print(libro1, libro2, libro3)

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

def listar_libros(libros):
    return [libro["titulo"] for libro in libros]

libros = [libro1, libro2, libro3]
print(listar_libros(libros))

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

def buscar_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            return libro
    return None

print(buscar_libro(libros, "1984"))
print(buscar_libro(libros, "No existe"))


"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

def quitar_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            libros.remove(libro)
            return
    print(f"Error: el libro '{titulo}' no se encontró.")

quitar_libro(libros, "1984")
print(libros)
quitar_libro(libros, "No existe")



"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

def crear_inventario(libros):
    inventario = {}
    for libro in libros:
        autor = libro["autor"]
        inventario[autor] = inventario.get(autor, 0) + 1
    return inventario

print(crear_inventario(libros))

"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

def libros_por_autor(libros, autor):
    return [libro["titulo"] for libro in libros if libro["autor"] == autor]

print(libros_por_autor(libros, "Gabriel García Márquez"))


"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

def existe_libro(libros, titulo):
    return any(libro["titulo"] == titulo for libro in libros)

print(existe_libro(libros, "El principito"))
print(existe_libro(libros, "1984"))

