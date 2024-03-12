import socket
import ssl

HOST = 'localhost'
PORT = 4444

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert-ssl/certificado.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print(ssock.version())
        ssock.connect((HOST, PORT))
        print("Conexión con éxito")
        # Leer el contenido del archivo a enviar
        with open('archivo_a_enviar.txt', 'rb') as file:
            file_content = file.read()
        # Enviar el contenido del archivo
        ssock.sendall(file_content)
        print("Archivo enviado.")