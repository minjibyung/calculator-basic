
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

operador = input("Introduce la operacion que deseas realizar(suma, resta, multiplicacion, division): ")

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'multiplicacion':
    resultado = num1 * num2
elif operador == 'division':
    resultado = num1 / num2

else:
    resultado = None
    print("operador no valido")

if resultado is not None:
    print("El resultado de la operacion solicitada es:", resultado) 
