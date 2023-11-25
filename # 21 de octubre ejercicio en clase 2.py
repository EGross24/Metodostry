# 21 de octubre

#Definir la escala de las literales
Literales = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F" : 0}


Asignaturas = []

#Solicitar al usuario la cantidad de asignaturas
Cantidad_de_asignaturas = int(input("Ingrese la cantidad de asignaturas: "))

for i in range(Cantidad_de_asignaturas):
    nombre = input(f"Nombre de la asignatura: {i + 1}: ")
    creditos = int(input(f"Cantidad de creditos para {nombre}: "))
    calificacion = int(input(f"Calificacion final para {nombre}: "))

    asignatura = [nombre, creditos, calificacion] 
    Asignaturas.append(asignatura)

#Inicializar el calculo del indice
sum_creditos = 0
sum_mult = 0


for asignatura in Asignaturas:
    nombre = asignatura[0]
    creditos = asignatura[1]
    calificacion = asignatura[2]

#Determinar rango de la literal
if calificacion >= 90 and calificacion <= 100:
    N_literal = "A"
elif calificacion >= 80 and calificacion < 90:
    N_literal = "B"
elif calificacion >= 70 and calificacion < 80: 
    N_literal = "C"
elif calificacion >= 60 and calificacion < 70:
    N_literal = "D"
else:
    N_literal = "F"

#Calculamos la multiplicacion y sumamos los valores
multiplicacion = creditos * Literales[N_literal]
sum_creditos += creditos
sum_mult += multiplicacion


#Calculamos el indice
Indice = sum_mult / sum_creditos

print(f"El indice del cuatrimestre es: {Indice}")









