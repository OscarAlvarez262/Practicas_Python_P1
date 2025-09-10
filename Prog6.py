def hola():  # Definición de método o función | Method or function definition
    c = 0  # Contador para controlar la posición en el arreglo | Counter to control the position in the array
    while (True):  # Bucle infinito hasta que se ingrese 10 datos | Infinite loop until 10 inputs are given
        a = input('Escribe un dato o valor \n')  # Solicita un dato al usuario | Asks the user for a value

        if a.isdigit():  # Verifica si la entrada es un número | Checks if the input is a number
            arr[c] = int(a)  # Convierte a entero y lo guarda en el arreglo | Converts to integer and stores it in the array
        elif a.isalpha():  # Verifica si la entrada es solo letras | Checks if the input is alphabetic
            car.append(a)  # Agrega la cadena a la lista car | Appends the string to the car list

        c += 1  # Incrementa el contador | Increments the counter

        if c >= 10:  # Condición para detener el ciclo después de 10 entradas | Stops the loop after 10 inputs
            break
    
    resultados()  # Llama a la función para mostrar los resultados | Calls the function to display results
    

def resultados():  # Definición de método o función | Method or function definition
    c2 = 0  # Contador de valores numéricos válidos en el arreglo | Counter for valid numeric values in the array
    print(f'La lista tiene {len(car)} ')  # Muestra la cantidad de cadenas guardadas | Displays the number of stored strings

    for i in arr:  # Recorre el arreglo numérico | Iterates over the numeric array
        if i != 0:  # Verifica si el valor no es cero | Checks if the value is not zero
            c2 += 1  # Incrementa el contador | Increments the counter

    print(f'El arreglo tiene {c2}')  # Muestra la cantidad de números guardados | Displays the number of stored numbers
    print(car)  # Imprime la lista de cadenas | Prints the list of strings
    print(arr)  # Imprime el arreglo de números | Prints the array of numbers


arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Arreglo inicializado con 10 ceros | Array initialized with 10 zeros
car = []  # Lista para almacenar cadenas | List to store strings

if __name__ == "__main__":  # Método principal | Main method
    hola()  # Llama a la función principal | Calls the main function
