# Hacer un programa que lea nombre, edad y sexo de 5 personas
# Make a program that reads name, age, and gender of 5 people

def lista():  # Definición de función | Function definition
    c = 0  # Contador para controlar cuántas personas se registran | Counter to control how many people are registered
    while True:  # Bucle infinito hasta que se ingresen 5 personas | Infinite loop until 5 people are entered
        n = input('Ingresa un nombre \n')  # Solicita el nombre | Asks for the name
        e = input('Ingresa su edad \n')  # Solicita la edad | Asks for the age
        g = input('Ingresa su sexo H o M \n').upper()  # Solicita el sexo y lo convierte a mayúsculas | Asks for gender and converts it to uppercase
        
        # Se guarda la información en la lista lis1 como una cadena | Stores the information in lis1 as a string
        lis1.append(n + ', ' + e + ', ' + g)
        
        c += 1  # Incrementa el contador | Increments the counter
        
        if c >= 5:  # Si ya se ingresaron 5 personas, sale del bucle | Stops the loop after 5 people are entered
            break
    
    resultado()  # Llama a la función para mostrar resultados | Calls the function to display results


def resultado():  # Definición de función para mostrar resultados | Function definition to display results
    print(lis1)  # Imprime la lista con los datos registrados | Prints the list with the stored data


lis1 = []  # Lista para almacenar nombre, edad y sexo | List to store name, age, and gender
lis2 = []  # Lista no utilizada actualmente | List not used currently

# Punto de inicio del programa | Program entry point
if __name__ == "__main__":
    lista()  # Llama a la función principal | Calls the main function
