
class Persona:
    def __init__(self):
        self.nombre = str
        self.edad = int
    
    def crear_personas(self):
        cantidad = int(input("Cantidad de personas: "))
        personas = []
        for idx in range(cantidad):
            persona = Persona()
            print(f" ========== PERSONA {idx + 1} ==========")
            persona.nombre = input("Ingrese el nombre: ")
            persona.edad = int(input("Ingrese la edad: "))
            personas.append(persona)
        self.listar_personas(personas)
    
    def listar_personas(self, lista_personas):
        for persona in lista_personas:
            print(f"Nombre: {persona.nombre}")
            print(f"Edad: {persona.edad}")