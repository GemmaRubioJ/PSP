#4.- Escribir en código python una función que reciba dos números como parámetros, y
#devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

def  count_multiples_with_while(first_number, second_number):
    count = 0
    multiple = first_number
    while multiple < second_number:
        count += 1
        multiple += first_number
    return print(f"Hay {count} multiplos")

def main():
    count_multiples_with_while(2, 10)

if __name__ == '__main__':
    main()