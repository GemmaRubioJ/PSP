import requests


# Enter an IP address and find the country that IP is registered in.
def get_country(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return data['country']
        else:
            return "No se pudo obtener la información."
    except requests.RequestException as e:
        return f"Error de solicitud: {e}"

# Ejemplo de uso
ip_address = input("Ingrese la dirección IP: ")
country = get_country(ip_address)

if country:
    print(f"La dirección IP {ip_address} está registrada en: {country}")
else:
    print("No se pudo determinar el país de la dirección IP.")