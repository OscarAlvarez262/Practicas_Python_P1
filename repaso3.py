
# def leer ():
#     #ORD que obtiene el ASCII del caracter
#     #ISALPHA para caracteres
#     #ISDIGIT para numeros
#     #TRY EXCEPT VALUEERROR:
#     a = input('Escribe un dato o valor')
#     validar(a)

# def validar(a):
#     c=0
#     d=0.0
#     try:
#         c= int(a)
#         print('Es un valor numerico sin decimales')
#     except ValueError:
#         print('No es un valor numerico sin decimales')
#     try:
#         d = float(a)
#         print('Es un valor numerico con decimales')
#     except ValueError:
#         print('No es un valor numerico con decimales')

# if __name__=='__main__':
#     leer()

# Hacer un programa que lea un dato, cualquiera que sea, y que lo almacene en una lista, respetando su tipo de dato
# Make a program that reads any input and stores it in a list, preserving its data type

list = []  # Lista para almacenar los datos ingresados | List to store the entered data

def dato():  # Función para leer un dato y validarlo | Function to read a data item and validate it
    d = input('Ingresa un dato\n')  # Solicita un dato al usuario | Asks the user for a data item
    dato = validar(d)  # Llama a la función validar para determinar el tipo de dato | Calls validar function to determine data type
    list.append(dato)  # Agrega el dato a la lista | Appends the data to the list

def validar(d):  # Función para verificar el tipo de dato ingresado | Function to check the data type of the input
    i = 0  # Variable para entero | Variable for integer
    f = 0.0  # Variable para flotante | Variable for float
    try:
        i = int(d)  # Intenta convertir a entero | Tries to convert to integer
        print('Tu valor es un entero')  # Mensaje si es entero | Message if input is integer
        return i  # Devuelve el entero | Returns the integer
    except ValueError:
        print('Tu valor no es un entero')  # Mensaje si no es entero | Message if input is not integer
    try:
        f = float(d)  # Intenta convertir a flotante | Tries to convert to float
        print('Tu valor es un flotante')  # Mensaje si es flotante | Message if input is float
        return f  # Devuelve el flotante | Returns the float
    except ValueError:
        print('Tu valor no es un flotante')  # Mensaje si no es flotante | Message if input is not float
    
    return d  # Si no es ni entero ni flotante, devuelve el dato original | If not int or float, returns the original input

if __name__ == '__main__':  # Punto de entrada del programa | Program entry point
    while True:
        dato()  # Llama a la función dato | Calls the dato function
        resp = input('Deseas otro S/N\n')  # Pregunta si desea ingresar otro dato | Asks if user wants to enter another data item
        if resp == 'N' or resp == 'n':  # Si la respuesta es no, termina el ciclo | If the answer is no, exits the loop
            print(list)  # Muestra la lista con los datos ingresados | Displays the list with entered data
            break
