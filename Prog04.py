# Hacer un programa que lea 10 números y los almacene en una lista
# Create a program that reads 10 numbers and stores them in a list

a = []   # Lista donde se guardarán los números | List where the numbers will be stored
s = 0    # Variable para almacenar la suma | Variable to store the sum
n = 0    # Contador para controlar la cantidad de números | Counter to control how many numbers are entered
numeros = "0,1,2,3,4,5,6,7,8,9";  # Define el rango de datos que se pueden usar | Defines the range of allowed digits

# Ciclo while que continúa hasta que se ingresen 10 números válidos | While loop that continues until 10 valid numbers are entered
while(n < 10):
    b = input('Escribe un numero: ')  # Solicita un número al usuario | Asks the user for a number
    x = 0  # Contador de dígitos válidos | Counter for valid digits
    
    for i in b:  # Recorre cada carácter ingresado | Iterates through each entered character
        # if (ord(i) >=48 and ord(i)<=57):  # El ord se utiliza para obtener el valor ASCII | The ord function is used to get the ASCII value
        if i in numeros:  # Verifica si el carácter es un número válido | Checks if the character is a valid number
            x += 1  # Incrementa el contador si es válido | Increments the counter if valid
    
    if len(b) == x:  # Compara si todos los caracteres son números | Checks if all characters are valid digits
        a.append(int(b))  # Convierte a entero el valor y lo agrega a la lista | Converts the value to integer and appends it to the list
        n += 1  # Incrementa el contador | Increments the counter
    else:
        print('El valor no es numero')  # Muestra un mensaje si hay caracteres inválidos | Displays a message if invalid characters are detected

# Imprime todos los números de la lista | Prints all the numbers stored in the list
for i in a:
    print(i)  # Muestra cada número | Displays each number
    s += i    # Suma cada número a la variable acumuladora | Adds each number to the accumulator

# Muestra la suma total de los números ingresados | Displays the total sum of the entered numbers
print(f'La suma es: {s}')

