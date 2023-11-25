"""with open("estudiantes.csv", "r") as file_estudiantes:
    contenido = file_estudiantes.readlines()
    estudiantes = {}
    print(contenido[1:])"""

with open("estudiantes.csv", "r") as file_estudiantes:
    contenido = file_estudiantes.readlines()
    estudiantes = {}
    for linea in contenido:
        print(linea)
    