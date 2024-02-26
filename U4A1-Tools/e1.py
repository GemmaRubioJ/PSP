from ftplib import FTP

#A file transfer program which can transfer files back and forth from a remote ftp sever.

#Servidor en contenedor Docker
# Configuración del servidor FTP
ftp_server = "127.0.0.1"
ftp_username = "admin"
ftp_password = "preguntaraalberto"

# Conexión al servidor FTP
ftp = FTP(ftp_server)
ftp.login(user=ftp_username, passwd=ftp_password)

# Subir un archivo
def upload_file(file_path, target_path):
    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {target_path}', file)

# Descargar un archivo
def download_file(target_path, local_path):
    with open(local_path, 'wb') as file:
        ftp.retrbinary(f'RETR {target_path}', file.write)

# Ejemplo de uso
upload_file('/mnt/c/Users/noabl/Documents/CLASE2/ejerciciosPSP/hola.txt', 'remote_file.txt')
download_file('remote_file.txt', '/mnt/c/Users/noabl/Documents/CLASE2/ejerciciosPSP')

# Cerrar la conexión
ftp.quit()