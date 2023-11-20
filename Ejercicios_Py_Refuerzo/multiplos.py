#3.- Escribir en código python una función que reciba dos números como parámetros, y
#devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

def count_multiples(first_number, second_number):
    count = 0
    for i in range(first_number, second_number, first_number):
        print(f"Multiplo actual: {i}")
        count += 1
    return print(f"Hay {count} multiplos")

def main():
    count_multiples(2, 10)

if __name__ == '__main__':
    main()