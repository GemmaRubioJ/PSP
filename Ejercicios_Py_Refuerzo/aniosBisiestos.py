# El usuario debe ingresar una fecha (día, mes, año) y el programa debe indicar si es
#válida o no. Considerar los años bisiestos.

def is_leap_year(year):
    # A year is a leap year if it is divisible by 4, except for end-of-century years
    # which must be divisible by 400.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(day, month, year):
    # Checks if the given date is valid.
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month == 2:
        if is_leap_year(year):
            return day <= 29
        else:
            return day <= 28
    if month in [4, 6, 9, 11]:
        return day <= 30
    return day <= 31

def main():
    # Solicitar la fecha al usuario
    day = int(input("Ingrese el día: "))
    month = int(input("Ingrese el mes: "))
    year = int(input("Ingrese el año: "))

    # Verificar si la fecha es válida
    if is_valid_date(day, month, year):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

if __name__ == '__main__':
    main()