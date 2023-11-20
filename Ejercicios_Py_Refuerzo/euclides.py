# Algoritmo de Euclides para calcular el máximo común divisor de dos números n y m,

def euclid_algorithm(n, m):
    while m != 0:
        r = n % m
        n, m = m, r
    return n

def main():
    n = 15
    m = 9
    print(f"el máximo común divisor de {n} y {m} es : ")
    print(euclid_algorithm(n, m))

if __name__ == '__main__':
    main()