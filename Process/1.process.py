import os
import time
import logging
import multiprocessing

#PROCESO PARALELO

logging.basicConfig(level=logging.DEBUG, format='%(process)s %(processName)s %(message)s')

#acepta un argumento (mensaje). Cuando se ejecuta en un nuevo proceso, mostrará
# un mensaje de inicio y espera 3 segundos, muestra el mensaje argumento y un mensaje de finalización.
def nuevo_proceso(mensaje):
    logging.info('Hola, soy un nuevo proceso')

    time.sleep(3)

    logging.info(mensaje)

    logging.info('Fin del proceso')

#crea un objeto process de multiprocessing.Process y le asigna la función anterior.
# y le pasa un diccionario con el mensaje "nuevo mensaje desde un argumento". 
#Inicia el proceso hijo con process.start(), espera que termine con process.join()
#Cuando ha terminado muestra un mensaje desde el proceso principal. 
if __name__ == '__main__':
    # args o kwargs
    process = multiprocessing.Process(target=nuevo_proceso, name='proceso-hijo',
                                        kwargs={'mensaje': 'Nuevo mensaje, desde un argumento!'})
    process.start()

    process.join()

    logging.info('Hola, desde el proceso padre')
    