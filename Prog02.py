a = [10]  # Arreglo | Array
b = [ ]   # Lista | List

b.append(10000)
b = {'Hola', 10, 100.05, False, 'm'}
# Una lista permite guardar cualquier tipo de dato sin importar su categoría
# A list allows you to store any type of data regardless of its category

# b.append(10)  # Agrega un elemento al final de la lista | Adds an element to the end of the list

## Ciclos y condiciones | Loops and conditions
if(len(a) > len(b)):  # Compara el tamaño de las listas | Compares the size of the lists
    print('A es mayor')  # Imprime que A es mayor | Prints that A is greater
else:
    print('B es mayor')  # Imprime que B es mayor | Prints that B is greater

# Ciclo for para recorrer la lista | For loop to iterate through the list
for i in a:
    print(a)  # Imprime la lista completa en cada iteración | Prints the whole list on each iteration
