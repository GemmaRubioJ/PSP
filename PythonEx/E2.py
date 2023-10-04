# Escribe un programa Python que pregunte al usuario por 10 números enteros y muestre
# por pantalla el número total de veces que el usuario ha introducido el 0, el número total
# de enteros mayores que 0 introducidos y el número total de enteros menores que 0 introducidos.


contadorCeros = 0
contadorMayores = 0
contadorMenores = 0

for i in range(10):
    numero = int(input(f"Introduce el número {i+1}: "))
    if numero == 0:
        contadorCeros += 1
    if numero > 0:
        contadorMayores +=1
    if numero < 0: 
        contadorMenores +=1

print(f"Total de veces que introdujo el 0 : {contadorCeros}")
print(f"Total de número mayores que 0 : {contadorMayores}")
print(f"Total de números menores que 0: {contadorMenores}")