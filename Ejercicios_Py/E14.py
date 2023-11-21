#Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
    #- 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
    #- 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
    #- 3. Salir del Programa.




def writeFile(file):
    with open(file, 'w') as file:              #La clausula with indica que al terminar cierre el archivo.
        for number in range(0, 101, 2):
            file.write(str(number) + "\n")


def showFile(file):
    with open(file, 'r') as file:
        print(file.read())
        

def menu():
    print(" ***** MENÚ ******* ")
    print(" 1 - Volcado ")
    print(" 2 - Mostrar ")
    print(" 3 - Salir ")

def main():
    file = ('e14.txt')
    while True:
        menu()
        option = int(input("Selecciona una opción :  "))
        if option == 1:
            writeFile(file)
        elif option == 2:
            showFile(file)
        elif option == 3:
            print("  ¡Adiós!")
            break
        else:
            print("Opción no válida")


main()