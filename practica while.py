Menu = """Seleccione una opcion: 
[1] Analisis_de_numeros
[2] Tablas_de_multiplicar"""

print(Menu)

opcion = input("Seleccione la opcion '1' o '2': ")


Analisis_de_numeros = 1
Tablas_de_multiplicar = 2


#Analisis de numeros
if opcion == '1':
    num = int(input("Ingrese un numero entero: "))
    total_pares = 0
    total_impares = 0
    while num != 0:
        pares = 0
        impares = 0
        while num != 0:
            last_digit = num % 10
            if last_digit % 2 == 0:
                pares += 1
                total_pares += 1
            else:
                impares += 1
                total_impares += 1
            num = num // 10
        
        print(f"el numero ingresado tiene {pares} digitos pares y {impares} digitos impares")
        num = int(input("Ingrese otro numero entero: "))
    print(f"Total de digitos pares: {total_pares}")
    print(f"Total de numeros impares: {total_impares}")


if opcion == '2':
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese otro numero entero: "))
    