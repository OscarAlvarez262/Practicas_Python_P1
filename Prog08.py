# Hacer un programa que lea una cadena y que muestre en pantalla
# cuántos números tiene, cuántas mayúsculas, cuántas minúsculas
# y cuántos espacios
# Make a program that reads a string and displays how many numbers, uppercase letters,
# lowercase letters, and spaces it contains

def inicio():  # Definición de función | Function definition
    numeros = "0123456789"  # Cadena de números válidos | String containing valid numbers
    cn = 0   # Contador de números | Counter for numbers
    e = 0    # Contador de espacios | Counter for spaces
    min = 0  # Contador de minúsculas | Counter for lowercase letters
    may = 0  # Contador de mayúsculas | Counter for uppercase letters

    cadena = input('Escribe una cadena \n')  # Solicita una cadena al usuario | Asks the user to enter a string

    # Recorre cada carácter en la cadena | Iterates over each character in the string
    for i in cadena:
        if i in numeros:  # Verifica si el carácter es un número | Checks if the character is a number
            cn += 1  # Incrementa el contador de números | Increments the number counter

        if i == ' ':  # Verifica si el carácter es un espacio | Checks if the character is a space
            e += 1  # Incrementa el contador de espacios | Increments the space counter

        if ord(i) >= 97 and ord(i) <= 122:  # Verifica si es una letra minúscula | Checks if it's a lowercase letter
            min += 1  # Incrementa el contador de minúsculas | Increments lowercase counter

        if ord(i) >= 65 and ord(i) <= 90:  # Verifica si es una letra mayúscula | Checks if it's an uppercase letter
            may += 1  # Incrementa el contador de mayúsculas | Increments uppercase counter

    # Muestra los resultados finales | Displays the final results
    print(f'Los numeros son {cn},\n los espacios: {e},\n las minusculas son: {min},\n las mayusculas son: {may}')


# Punto de inicio del programa | Program entry point
if __name__ == '__main__':
    inicio()  # Llama a la función principal | Calls the main function

