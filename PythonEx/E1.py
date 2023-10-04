# Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y)
# y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, 
#con el siguiente formato:
    # x + y = …
    #x – y = …
    #x * y = …
    #x / y = …
    #x % y = …

x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y

print(f"{x} + {y} = {suma}")
print(f"{x} - {y} = {resta}")
print(f"{x} * {y} = {multiplicacion}")
print(f"{x} / {y} = {division}")