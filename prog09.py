def minusculas(c1):  # Verifica si todos los caracteres excepto el primero son minúsculas | Checks if all characters except the first are lowercase
    cm = 0  # Contador de minúsculas | Counter for lowercase letters
    for i in c1[1:]:  # Recorre la cadena desde el segundo carácter | Iterates over the string from the second character
        if ord(i) >= 97 and ord(i) <= 122:  # Comprueba si el carácter es minúscula | Checks if the character is lowercase
            cm += 1
    if cm == len(c1) - 1:  # Si todas excepto la primera son minúsculas | If all except the first are lowercase
        print(f'La cadenas son minusculas excepto la primera')  # Mensaje de confirmación | Confirmation message
        vocales(c1)  # Llama a la función vocales para verificar que contenga todas las vocales | Calls vocales function to check all vowels
    else:
        print('La cadena no cumple')  # Mensaje si no cumple la condición | Message if condition is not met

def vocales(cad):  # Verifica si la cadena contiene todas las vocales | Checks if the string contains all vowels
    ba = False  # Bandera para la vocal 'a' | Flag for vowel 'a'
    be = False  # Bandera para la vocal 'e' | Flag for vowel 'e'
    bi = False  # Bandera para la vocal 'i' | Flag for vowel 'i'
    bo = False  # Bandera para la vocal 'o' | Flag for vowel 'o'
    bu = False  # Bandera para la vocal 'u' | Flag for vowel 'u'
    
    if 'a' in cad or 'A' in cad:
        ba = True
    if 'e' in cad or 'E' in cad:
        be = True
    if 'i' in cad or 'I' in cad:
        bi = True
    if 'o' in cad or 'O' in cad:
        bo = True
    if 'u' in cad or 'U' in cad:
        bu = True
    
    # Si contiene todas las vocales, se agrega a la lista | If it contains all vowels, append to list
    if ba and be and bi and bo and bu:
        list.append(cad)

def leer():  # Función para leer y procesar la cadena | Function to read and process the string
    ce = 0  # Contador de caracteres sin espacio | Counter for characters without spaces
    nc = ""  # Nueva cadena filtrada sin números | New filtered string without numbers
    c = input('Introduce una cadena\n')  # Solicita al usuario la cadena | Asks the user for a string
    
    # Contar caracteres que no sean espacios | Count characters that are not spaces
    for i in c:
        if ord(i) != 32:
            ce += 1
    
    if ce == len(c):  # Si no hay espacios | If there are no spaces
        if c.isalpha():  # Si la cadena es solo letras | If string contains only letters
            minusculas(c)  # Llama a la función minusculas | Calls minusculas function
        else:  # Si contiene números u otros caracteres | If it contains numbers or other characters
            for i in c:
                if ord(i) >= 48 and ord(i) <= 57:  # Ignora números | Ignores numbers
                    pass
                else:
                    nc += i  # Construye cadena filtrada | Builds filtered string
            print(nc)  # Muestra la cadena filtrada | Displays filtered string
            minusculas(nc)  # Llama a minusculas con la cadena filtrada | Calls minusculas with filtered string
    else:
        print('Error, hay espacios en la cadena')  # Mensaje de error si hay espacios | Error message if spaces are present

list = []  # Lista para almacenar cadenas válidas | List to store valid strings

if __name__ == '__main__':  # Punto de entrada del programa | Program entry point
    while True:
        leer()  # Llama a la función leer repetidamente | Calls leer function repeatedly
        if len(list) >= 5:  # Sale del bucle cuando la lista tiene 5 elementos válidos | Exit loop when list has 5 valid strings
            break
