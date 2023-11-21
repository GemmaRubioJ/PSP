# Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings
# y muestra por pantalla el String con mayor longitud y el String con menor longitud.

tabla = ['hola', 'que', 'tal', 'estas', '?']

def mayorYmenor (tabla):
    cadenaLarga = max(tabla, key=len)
    cadenaCorta  = min(tabla, key=len)
    print(f"La cadena más larga es:   {cadenaLarga}" )
    print(f"La cadena más corta es:   {cadenaCorta}")

mayorYmenor(tabla)

