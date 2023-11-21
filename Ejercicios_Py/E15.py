#Crea un fichero de texto con el nombre y contenido que tú desees. 
#Por ejemplo, Ejercicio15.txt. Realiza un programa en Python que lea
# el fichero <<Ejercicio15.txt>> y muestre su contenido por pantalla sin espacios.
# Por ejemplo, si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”.

def read_without_spaces(file):
    with open(file, 'r') as file:
        content = file.read()
        content_without_spaces = content.replace(" ", "")
        print(content_without_spaces)
        
        

def main():
    file = ('PSP\PythonEx\e15.txt')
    read_without_spaces(file)

main()
