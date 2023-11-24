import os
import time
import logging
import multiprocessing

#PROCESO SECUNDARIO 

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#Registra un proceso inicial, duerme 2 segundos(simulando una tarea) y registra 
#un mensaje de finalización.
def proceso_hijo():
    logging.info('Hola, desde el procesos hijo!')

    time.sleep(2)

    logging.info('Fin del proceso hijo!')


#Crea un objeto process y le asigna la funció anterior. Se inicia con process.start()
#duerme y comprueba si el proceso secundario sigue vivo. Si todavía está en ejecución, 
# se envía una señal de terminación con process.terminate() y lanza un mensaje de aviso. 
#Finalmente muestra un mensaje de que el programa principal ha terminado.
if __name__ == '__main__':
    process = multiprocessing.Process(target=proceso_hijo)
    process.start()

    time.sleep(5)

    if process.is_alive():
        process.terminate()
        logging.info('Proceso hijo finalizado antes de tiempo')

    logging.info('Fin del programa!')