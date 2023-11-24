import logging
from concurrent.futures import ProcessPoolExecutor

# cómo usar el módulo concurrent.futures de Python para la ejecución
# concurrente de tareas en múltiples procesos.
logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
    return number % 2 == 0


#processPoolExecutor garantiza (con el bloque with) que los recursos se liberen cuando el bloque se complete
#se inicializa el ProcessPool con un máximo de 2 trabajadores (2 procesos separados).
# se envía una tarea al pool de procesos con 'submit'y agenda la función y el argumento.
# devuelve un objeto 'future' que representa la ejecución asíncrona.
# La función callback se añade a 'future' que se invoca cuando la tarea se compresa y 
#resgistra si el número es par. Se repite para el numero 1895
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:

        future = executor.submit(is_even, 10)
        future.add_done_callback(
            lambda future: logging.info(f'El número es par? {future.result()}')
        )

        future = executor.submit(is_even, 1895)
        future.add_done_callback(
            lambda future: logging.info(f'El número es par? {future.result()}')
        )