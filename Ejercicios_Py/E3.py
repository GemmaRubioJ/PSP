# Realiza un programa Python que adivine el número. El programa generará un
# número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario indicando 
#“mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente.
# El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones 
#junto al número de intentos que ha necesitado el usuario.

import random

numero_aleatorio = random.randint(0, 20)
intentos = 0

print("¡EMPIEZA EL JUEGO!")
print(numero_aleatorio)
while True :
    numero_usuario = int(input("Introduce un número: "))
    intentos += 1
    if numero_usuario == numero_aleatorio:
        print("¡Felicitaciones! Has adivinado el número en"  ,intentos, "intentos")
        break
    elif numero_usuario < numero_aleatorio:
        print("El número es MAYOR. Prueba otra vez")
    else:
        print("El número es MENOR. Prueba otra vez")