#Emily Rosario 23-0430

#Creamos la lista para almacenar los productos
Productos = []

#Se captura el numero de caja, el nombre de cajero que atiende y el nombre del cliente
N_Caja = int(input("Numero de caja: "))
Cajero = input("Ingrese su nombre: ")
Cliente = input("Ingrese el nombre del cliente: ")

#Utilizamos el bucle "for" para capturar los productos en un rango determinado
for _ in range(100):
    nombre = input("Ingrese nombre del producto ('fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
#Se solicita el precio del producto y cantidad a comprar
    precio = float(input("Ingrese precio del producto: "))
    cantidad = int(input("Ingrese cantidad: "))
    Valor = precio * cantidad
#Determinamos si el producto lleva ITBIS o no, (el producto por defecto no lleva itbis) para esto hacemos una pregunta de si lleva o no
    ITBIS = 0.00
    lleva_itbis = input("lleva itbis? (S/N): ")
    if lleva_itbis.lower() == 's':
        ITBIS = (Valor / 1.18) * 0.18

#Agregamos los datos del producto a lista
    Productos.append([nombre, precio, cantidad, ITBIS, Valor])

#Imprimir la factura
print('-'*101)
print(f"Cliente: {Cliente}")
factura = "***FACTURA PARA CONSUMIDOR FINAL***"
print(factura.center(100, " "))
print('-'*101)
print('|{:45} | {:<10} | {:<10} | {:<10} | {:<10}|'.format("Producto", "Precio", "Cantidad", "ITBIS", "Valor"))
print('-'*101)

#Inicializar las variables para el total del itbis y el total del precio de los productos
Total_ITBIS = 0
Total = 0

#Iteramos en una lista para imprimir cada producto y sus respectivos datos
for producto in Productos:
    nombre, precio, cantidad, ITBIS, subtotal = producto
    print('|{:45} | {:<10.2f} | {:<10} | {:<10.2f} | {:<10.2f}|'.format(nombre, precio, cantidad, ITBIS, subtotal))
    Total_ITBIS += ITBIS
    Total += subtotal

#Imprimimos el total de itbis, total y el total final a pagar y todos los otros datos solicitados al incio
Total_a_pagar = Total_ITBIS + Total
print('-'*101)
print(f"Total ITBIS:{Total_ITBIS: .2f}$")
print(f"Total:{Total: .2f}$")
print(f"Total a pagar:{Total_a_pagar: .2f}$")
print('-'*101)
print(f"Le atendió: {Cajero}")
print(f"Caja: {N_Caja}")