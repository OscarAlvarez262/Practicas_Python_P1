arr = [0,0,0,0,0,0,0,0,0,0]  # Arreglo para almacenar números | Array to store numbers
car = []  # Lista para almacenar cadenas | List to store strings
c = 0    # Contador para la posición del arreglo | Counter for array position
c2 = 0   # Contador de números válidos en el arreglo | Counter for valid numbers in the array

# Bucle para leer hasta 10 datos | Loop to read up to 10 inputs
while (True):
    a = input('Escribe un dato o valor \n')  # Solicita un dato al usuario | Asks the user for a value
    
    if a.isdigit():  # Verifica si es un número | Checks if the input is a number
        arr[c] = int(a)  # Convierte a entero y lo guarda en el arreglo | Converts to integer and stores in the array
    elif a.isalpha():  # Verifica si es solo letras | Checks if the input contains only letters
        car.append(a)  # Agrega la cadena a la lista | Appends the string to the list
    
    c += 1  # Incrementa el contador | Increments the counter
    if c >= 10:  # Sale del bucle después de 10 entradas | Exits the loop after 10 inputs
        break

# Cuenta cuántos números válidos hay en el arreglo | Counts how many valid numbers are in the array
for i in arr:
    if i != 0:
        c2 += 1

print(f'El arreglo tiene {c2}')  # Muestra la cantidad de números | Displays the number of numbers
print(f'La lista tiene {len(car)} ')  # Muestra la cantidad de cadenas | Displays the number of strings

print(car)  # Imprime la lista de cadenas | Prints the list of strings
print(arr)  # Imprime el arreglo de números | Prints the array of numbers

