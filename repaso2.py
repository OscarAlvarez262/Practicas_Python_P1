# Hacer un programa que realice la operación de la fórmula general
# Make a program that performs the quadratic formula operation

a = 0   # Coeficiente A de la ecuación cuadrática | Coefficient A of the quadratic equation
b = 0   # Coeficiente B de la ecuación cuadrática | Coefficient B of the quadratic equation
c = 0   # Coeficiente C de la ecuación cuadrática | Coefficient C of the quadratic equation

p = 0   # Variable temporal para b² | Temporary variable for b squared
m = 0   # Variable temporal para 4ac | Temporary variable for 4ac
r = 0   # Discriminante b² - 4ac | Discriminant b² - 4ac

ra = 0.0   # Raíz cuadrada del discriminante | Square root of the discriminant
d = 0.0    # Denominador 2a | Denominator 2a
x1 = 0.0   # Primera solución de la ecuación cuadrática | First solution of the quadratic equation
x2 = 0.0   # Segunda solución de la ecuación cuadrática | Second solution of the quadratic equation


# Solicita los valores de A, B y C | Asks for the values of A, B, and C
a = int(input('Ingresa el valor de A: '))
b = int(input('Ingresa el valor de B: '))
c = int(input('Ingresa el valor de C: '))

# Calcula b² | Calculates b squared
p = b ** 2

# Calcula 4ac | Calculates 4ac
m = 4 * a * c

# Calcula el discriminante: b² - 4ac | Calculates the discriminant: b² - 4ac
r = p - m

# Verifica si el discriminante es positivo | Checks if the discriminant is positive
if r > 0:
    print('Si se puede')  # La ecuación tiene dos soluciones reales | The equation has two real solutions

    # Calcula la raíz cuadrada del discriminante | Calculates the square root of the discriminant
    ra = r ** (1/2)

    # Calcula 2a | Calculates 2a
    d = 2 * a

    # Calcula las dos soluciones de la ecuación | Calculates the two solutions of the equation
    x1 = (-b + ra) / d
    x2 = (-b - ra) / d

    # Muestra los resultados con dos decimales | Displays the results with two decimals
    print(f'El valor de x1 es: {x1:.2f} y de x2 es: {x2:.2f}')

else:
    # Si el discriminante es negativo, no hay soluciones reales | If the discriminant is negative, no real solutions
    print('No se puede')





