import time
import logging
from multiprocessing import Pool

#utiliza el módulo multiprocessing para ejecutar de manera concurrente una función que determina si un número es par o no
logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')



def is_even(number):
    time.sleep(1)
    return number % 2 == 0

def show_result(results):
    logging.info(f'El resultado es: {results}')

#se crea un pool de 2 procesos, se crea una lista de numeros del 1 al 10,
#con la función imap_unordered se aplica la función is_even para todos los numeros de la lista
#de manera asincrona y los procesos se procesan en el orden en que se completan
if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers = [ number for number in range(1, 11)]

        for element in executor.imap_unordered(is_even, numbers): # yield
            logging.info(element)

#Con time.sleep(1) en la función is_even, cada tarea se demorará un segundo,
# pero debido a la ejecución en paralelo, el script completo tomará
# significativamente menos de 10 segundos en ejecutarse, dependiendo 
# de la cantidad de núcleos disponibles en la CPU