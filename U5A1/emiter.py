# Generar la Clave Privada
# openssl genpkey -algorithm RSA -out clave-privada.key -pkeyopt rsa_keygen_bits:2048
 
# Generar certificado.pem
# openssl req -new -x509 -days 365 -key clave-privada.key -out certificado.pem

# Verificar la clave privada
#openssl rsa -check -in clave-privada.key

# Verificar el certificado
# openssl x509 -text -noout -in certificado.pem


import socket
import ssl

HOST = 'localhost'
PORT = 4444

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert-ssl/certificado.pem', 'cert-ssl/clave-privada.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Servidor corriendo en: {HOST}, {PORT}")
    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept()
            print(f"Conexión desde: {addr}")
            # Recibir datos (en este caso, podríamos tratarlo como el archivo o parte de él)
            file_content = conn.recv(1024)
            # Escribir el contenido en un archivo
            with open('archivo_recibido.txt', 'wb') as file:
                file.write(file_content)
            print("Archivo recibido y guardado.")