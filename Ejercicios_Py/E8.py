# Implementa un programa Python con un método llamado sum(int [] tabla) que muestre
# por pantalla el resultado de sumar todos los elementos de la tabla pasada como parámetro.

tabla =  [1,2,3,4,5,6]

def sumar(tabla):
    total = sum(tabla)
    print(f"el total es : {total} ")

sumar(tabla)