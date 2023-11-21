# Implementa un programa Python con un método llamado indexContains(String[] tabla, 
#String cadena) que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”. 
#En caso de no haber ningún valor igual, devuelve -1

tabla = ['hola', 'que', 'tal', 'estas', '?']
cadena = "que"
def indexContains (tabla, cadena):
    if len(cadena) <= len(tabla):
        print(tabla[len(cadena)])
    else:
        print(-1)

indexContains(tabla, cadena)