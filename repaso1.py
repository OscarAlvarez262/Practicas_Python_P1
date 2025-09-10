"""intrucciones de entrada y salida"""
#Print() o print(f)
# print('Hola mundo')
# print(f'Hola mundo {10}')

"""Entrada de datos"""
#input
# input('Escrobe un numero')#Se introducen SOLO letras
# #Casting para convertir a valores especificos
# f=0.0
# f = float(input('Ingresa un numero con decimales'))#Solo numeros flotantes
# e=0
# e= int(input('Escribe un numero'))#SOLO numeros enteros
# c =120
# print(str(c))#Convertir a cadena 
# v=""
# v=str(c)
"""NOTA: SOLO las variables que no se introducen por teclado se OBLIGAN a inicializarlas"""


# # Hacer un programa que sea nombre y precio de un producto, el programa
# # calculara el costo y precio de venta, el costo involucra el 12% 
# y el iva 16%



for i in range(0, 5):  # Repite el ciclo 5 veces | Loops 5 times
    P = ""  # Variable para almacenar el nombre del producto | Variable to store the product name
    c = 0.0  # Precio bruto | Base price
    u = 0.0  # Precio con IVA del 12% | Price with 12% tax
    v = 0.0  # Precio de venta final con IVA + 16% | Final selling price with additional 16%

    # Solicita el nombre del producto | Asks for the product name
    p = input('Ingresa el nombre de un producto\n')

    # Solicita el precio bruto del producto | Asks for the base price of the product
    c = float(input(f'Ingresa el precio bruto del producto: {p}\n'))

    # Calcula el precio con el 12% agregado | Calculates the price with an additional 12%
    u = float(c * 1.12)

    # Calcula el precio final de venta con otro 16% agregado | Calculates the final price with an extra 16%
    v = (u * 1.16)

    # Muestra el precio con el 12% de incremento | Displays the price after 12% increase
    print(f'tu costo del producto: {p}, es de ${u:.2f}')  # :.2f muestra 2 decimales | :.2f shows 2 decimals

    # Muestra el precio final de venta | Displays the final selling price
    print(f'tu precio de venta del producto: {p}, es de ${v:.2f}')  # :.2f muestra 2 decimales | :.2f shows 2 decimals