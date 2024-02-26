import requests
import time

#An application that attempts to connect to a website or server every so many minutes
# or a given time and check if it is up. If it is down, it will notify you by posting a notice on screen. 


def check_website(url, interval):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"El sitio web {url} está activo.")
            else:
                print(f"El sitio web {url} está inactivo. Código de estado: {response.status_code}")
        except requests.ConnectionError:
            print(f"No se pudo conectar al sitio web {url}. Podría estar inactivo.")

        time.sleep(interval * 60)  # Intervalo en minutos

# Ejemplo de uso
url = input("Ingrese la URL del sitio web: ")
interval = float(input("Ingrese el intervalo de tiempo en minutos: "))

check_website(url, interval)