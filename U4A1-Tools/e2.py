import socket

#Enter an IP address and a port range where the program will then attempt to find open ports
# on the given computer by connecting to each of them. On any successful connections mark the port as open.

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout para la conexión
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Ejemplo de uso
ip_address = input("Ingrese la dirección IP: ")
start_port = int(input("Ingrese el puerto inicial: "))
end_port = int(input("Ingrese el puerto final: "))

open_ports = scan_ports(ip_address, start_port, end_port)

if open_ports:
    print("Puertos abiertos encontrados:", open_ports)
else:
    print("No se encontraron puertos abiertos en el rango dado.")