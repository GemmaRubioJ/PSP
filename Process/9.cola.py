import logging
import multiprocessing

# uso de colas para la comunicación entre procesos en un entorno multiproceso utilizando el módulo multiprocessing.
logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# Es una función que se pasará a los procesos. Toma una cola como argumento y, en un bucle, retira elementos de la
# cola mientras no esté vacía, registrando cada elemento que se retira
def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f'El elemento es: {element}')


# se crea una cola gestionada por Manager, que puede ser compartida por varios
# procesos. Se llenan 20 elementos en la cola y se lanza un mensaje de que ya tiene elementos.
# Se crean tres procesos apuntando a la función get_elements y pasando la cola como argumento
# Se inicializan y se espera a que cada proceso termine con join(). Se muestra un mensaje de fin.
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(1, 21):
        queue.put(x)

    logging.info('La cola ya posee elementos!')

    process1 = multiprocessing.Process(target=get_elements, args=(queue, ))
    process2 = multiprocessing.Process(target=get_elements, args=(queue, ))
    process3 = multiprocessing.Process(target=get_elements, args=(queue, ))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    logging.info('Fin de los procesos!')