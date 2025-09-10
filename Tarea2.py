# hacer un programa que en una lista se introdusca cadenas de 
# caracteres con las siguientes restricciones:
# 1.- las cadenas no tienen tener espacios
# 2.- la cadena solo puede tener mayuscula la primer letra
# 3.- obligatoriamente deben de tener todas las vocales.
# el programa no termina hasta que la lista tenga 5 elementos
def inicio():
    voc = "AEIOU"  # String containing vowels / Cadena con vocales (no usada)
    lis = []     # List to store valid words / Lista para almacenar palabras válidas
    ele = len(lis) # Variable initialized but unused / Variable inicializada pero no utilizada
    
    # Loop until the list contains 5 valid words / Bucle hasta que la lista tenga 5 palabras válidas
    while (len(lis) <= 4):
        cad = input('Ingresa una cadena:\n')  # Ask the user for input / Solicita al usuario ingresar una cadena
        c = 0   # Counter for spaces / Contador de espacios
        m = 0   # Counter for uppercase letters / Contador de letras mayúsculas
        ca = 0  # Counter for vowel 'a' / Contador para la vocal 'a'
        ce = 0  # Counter for vowel 'e' / Contador para la vocal 'e'
        ci = 0  # Counter for vowel 'i' / Contador para la vocal 'i'
        co = 0  # Counter for vowel 'o' / Contador para la vocal 'o'
        cu = 0  # Counter for vowel 'u' / Contador para la vocal 'u'
        
        # Iterate through each character in the string / Recorre cada carácter en la cadena
        for i in cad:
            if i == ' ':
                c += 1  # Count spaces / Contar espacios
            
            if ord(i) >= 65 and ord(i) <= 90:  # Check if character is uppercase / Verificar si el carácter es mayúscula
                m += 1

            if ord(i) >= 65 and ord(i) <= 97:  # Check if character is between 'A' and 'a' (possible mistake) / Verifica si el carácter está entre 'A' y 'a' (posible error)
                ca += 1

            if ord(i) == 69 or ord(i) == 101:  # Count vowel 'e' / Contar vocal 'e'
                ce += 1
            if ord(i) == 73 or ord(i) == 105:  # Count vowel 'i' / Contar vocal 'i'
                ci += 1
            if ord(i) == 79 or ord(i) == 111:  # Count vowel 'o' / Contar vocal 'o'
                co += 1
            if ord(i) == 85 or ord(i) == 117:  # Count vowel 'u' / Contar vocal 'u'
                cu += 1

        # -------------------- VALIDATIONS / VALIDACIONES --------------------
        # Check if first letter is uppercase and only one uppercase is allowed / Verifica que la primera letra sea mayúscula y solo exista una mayúscula
        if (m == 0) or (m == 1) and (ord(cad[0]) >= 65 and ord(cad[0]) <= 90):
            if c >= 1:
                print('No puede llevar espacios')  # Invalid if spaces exist / Inválido si existen espacios

            # Check if the word contains all vowels / Verifica si la palabra contiene todas las vocales
            elif ca >= 1 and ce >= 1 and ci >= 1 and co >= 1 and cu >= 1:
                lis.append(cad)  # Save the valid word / Guarda la palabra válida
                print('"Palabra aceptada"')  # Accepted word / Palabra aceptada
            else:
                print('Error, la palabra debe de llevar todas las vocales')  
                # Error if missing any vowel / Error si falta alguna vocal
        else:
            print('Error, solo la primer letra puede ser mayuscula')
            # Error if the first letter is lowercase or has multiple uppercase letters / Error si la primera letra es minúscula o si hay varias mayúsculas

    # Show all saved valid words / Muestra todas las palabras válidas guardadas
    print(f'Las palabras guardadas fueron {lis}')

# Program entry point / Punto de entrada del programa
if __name__ == '__main__':
    inicio()
