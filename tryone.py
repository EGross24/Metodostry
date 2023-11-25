
"""import json
lista_de_peliculas = []

with open ('movies.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)"""

with open("movies.txt", "r", encoding="utf-8") as file:
    contenido = file.readlines()
    print(contenido)