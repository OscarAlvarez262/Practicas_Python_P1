# Hacer un programa que lea 10 números y los almacene en un arreglo
# Make a program that reads 10 numbers and stores them in an array

a = [0,0,0,0,0,0,0,0,0,0]  # Se inicializa un arreglo con 10 elementos en 0 | Initialize an array with 10 elements set to 0

# Ciclo para leer 10 números y guardarlos en el arreglo | Loop to read 10 numbers and store them in the array
for i in range(0,10):
    a[i] = int(input(f'Ingresa un numero \n'))  # Solicita un número y lo guarda en la posición correspondiente | Asks for a number and stores it in the corresponding position

# Ciclo para imprimir los números almacenados en el arreglo | Loop to print the stored numbers in the array
for i in a:
    print(i)  # Muestra cada número en una nueva línea | Displays each number on a new line
