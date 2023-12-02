#Emily Gross 23-430
#PRT11

#Clase para la lista de las personas
class ListaPersonas:
    def __init__(self):
        self.personas = []

#creamos funcion para agregar a las personas por teclado
    def add_persona(self, nombre, edad):
        persona = {"Nombre": nombre, "Edad": edad}
        self.personas.append(persona)

#funcion para mostrar a las personas en la terminal
    def mostrar_personas(self):
        for persona in self.personas:
            print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}")

#funcion para guardar ent txt_file
    def guardar_listado(self,):
        with open("Listado_personas", 'w') as txt_file:
            for persona in self.personas:
                txt_file.write(f"{persona['Nombre']}|{persona['Edad']}\n")

    def agrupar_por_edad(self, nombre_archivo):
        grupos_por_edad = {}
        for persona in self.personas:
            edad = persona['Edad']
            if edad not in grupos_por_edad:
                grupos_por_edad[edad] = []
            grupos_por_edad[edad].append(persona['Nombre'])

        with open(nombre_archivo, 'w') as archivo:
            for edad, personas in grupos_por_edad.items():
                archivo.write(f"Edad: {edad}\n")
                for nombre in personas:
                    archivo.write(f"{nombre}\n")

    def filtrar_por_letra(self, letra, nombre_archivo):
        personas_con_letra = [persona for persona in self.personas if persona['Nombre'].startswith(letra)]

        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Nombre|Edad\n")
            for persona in personas_con_letra:
                archivo.write(f"{persona['Nombre']}|{persona['Edad']}\n")

def main():
    lista_personas = ListaPersonas()

    while True:
        print('-'*101)
        print("\n1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Guardar listado en archivo")
        print("4. Agrupar por edad y guardar en archivo")
        print("5. Filtrar por letra y guardar en archivo")
        print("6. Salir")
        print('-'*101)

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese la edad: ")
            lista_personas.add_persona(nombre, edad)
        elif opcion == '2':
            lista_personas.mostrar_personas()
        elif opcion == '3':
            
            print(f"Listado guardado en {nombre_archivo}")
        elif opcion == '4':
            nombre_archivo = input("Ingrese el nombre del archivo para agrupar por edad: ")
            lista_personas.agrupar_por_edad(nombre_archivo)
            print(f"Datos agrupados por edad y guardados en {nombre_archivo}")
        elif opcion == '5':
            letra = input("Ingrese la letra para filtrar por nombre: ")
            nombre_archivo = input("Ingrese el nombre del archivo para el filtrado por letra: ")
            lista_personas.filtrar_por_letra(letra, nombre_archivo)
            print(f"Datos filtrados por letra y guardados en {nombre_archivo}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()