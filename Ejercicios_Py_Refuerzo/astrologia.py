def zodiac_sign(day, month):
    # Define the zodiac signs with their respective date ranges
    zodiacs = [
       ((3, 21), (4, 20), "Aries"),
        ((4, 21), (5, 20), "Tauro"),
        ((5, 21), (6, 21), "Geminis"),
        ((6, 22), (7, 23), "Cancer"),
        ((7, 24), (8, 23), "Leo"),
        ((8, 24), (9, 23), "Virgo"),
        ((9, 24), (10, 22), "Libra"),
        ((10, 23), (11, 22), "Escorpio"),
        ((11, 23), (12, 21), "Sagitario"),
        ((12, 22), (1, 20), "Capricornio"),
        ((1, 21), (2, 19), "Acuario"),
        ((2, 20), (3, 20), "Piscis"),
    ]

    birthday = (month, day)
    for start, end, sign in zodiacs:
         # Para Capricornio, que cruza el año
        if start > end:
            if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
                return sign
        # Para los otros signos
        elif start <= birthday <= end:
            return sign


def main():
    while True:
        print("Introduzca su día de nacimiento con el siguiente formato : ")
        day = int(input("Día : "))
        month = int(input("MES : "))
        zodiac = zodiac_sign(day, month)
        print(f"Tu signo zodiacal es: {zodiac}")

if __name__ == '__main__':
    main()