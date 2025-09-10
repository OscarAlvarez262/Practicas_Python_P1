#Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo
# si es un caracter o caracteres se metera en una lista, cuando finalice el programa
# nos mostrara cuantos elementos numericos y cuantos caracteres hay en cada estructuras

car = 0   # EN: Variable declared but unused / ES: Variable declarada pero no utilizada
Arreglo = 0  # EN: Counter for total entered elements / ES: Contador para los elementos totales ingresados
n = 0     # EN: Counter for total entered elements / ES: Contador para los elementos ingresados
a = [0,0,0,0,0,0,0,0,0,0]  # EN: Initialize list 'a' with one numeric element (10) / ES: Inicializa la lista 'a' con un elemento numérico (10)
l = []    # EN: Initialize empty list 'l' to store alphabetic characters / ES: Inicializa la lista vacía 'l' para guardar caracteres alfabéticos

while (n < 10):  # EN: Loop until 10 valid elements are entered / ES: Bucle hasta que se ingresen 10 elementos válidos
    b = input('Ingresa un dato: ')  # EN: Request input from user / ES: Solicita un dato al usuario

    if b.isdigit():  # EN: Check if input is numeric / ES: Verifica si el dato ingresado es numérico
        a[Arreglo]=(b)  # EN: Add numeric input to list 'a' / ES: Agrega el dato numérico a la lista 'a'
        Arreglo +=1  # EN: Increase numeric counter / ES: Incrementa el contador de numéricos
        n += 1       # EN: Increment counter / ES: Incrementa el contador
    elif b.isalpha():  # EN: Check if input is alphabetic / ES: Verifica si el dato ingresado es alfabético
        l.append(b)    # EN: Add alphabetic input to list 'l' / ES: Agrega el dato alfabético a la lista 'l'
        n += 1         # EN: Increment counter / ES: Incrementa el contador
    else:
        print('No valido')  # EN: Show error message for invalid input / ES: Muestra mensaje de error para datos no válidos

# ---- Final results ----
print(f'El total de elementos numericos guardados es {(Arreglo)}')  
# EN: Show total numeric elements stored / ES: Muestra el total de elementos numéricos guardados
print(f'El total de caracteres guardados es {len(l)}')  
# EN: Show total alphabetic elements stored / ES: Muestra el total de caracteres guardados
"""print(f'Elementos numericos guardados {a}')  
# EN: Display list of numeric elements / ES: Muestra la lista de elementos numéricos
print(f'Elementos de caracteres guardados {l}')  
# EN: Display list of alphabetic elements / ES: Muestra la lista de elementos alfabéticos"""
