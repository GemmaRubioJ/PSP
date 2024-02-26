import whois

#Enter an IP or host address and have it look it up through whois and return the results to you. 
def get_whois_info(domain_or_ip):
    try:
        w = whois.whois(domain_or_ip)
        return w.text
    except Exception as e:
        return f"Error al obtener la información WHOIS: {e}"

# Ejemplo de uso
address = input("Ingrese la dirección IP o el host: ")
whois_info = get_whois_info(address)

print(f"Información WHOIS para {address}:\n{whois_info}")