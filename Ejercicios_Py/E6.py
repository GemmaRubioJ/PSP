# Implementa un programa Python que solicite al usuario una cadena de caracteres (String)
# y muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición.

cadena = (input("Introduce una cadena de caracteres: "))

if len(cadena) < 2 :
    print("Introduce una cadena más larga")
else :
    cadenaModificada = cadena[-1] + cadena[1:-1] + cadena[0]
    print("La nueva cadena es : ", cadenaModificada)
