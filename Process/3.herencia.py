import logging
import multiprocessing


#utiliza el módulo multiprocessing, pero esta vez, 
# en lugar de usar la función Process directamente,
# extiende la clase Process en una clase personalizada llamada ProcesoFacilito
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#clase heredada de multiprocessing.Process
#daemon es un booleano que determina si el proceso es un demonio. Se pasa False, asique no será un demonio
# y el proceso principal esperará a qe este proceso hijo termine antes de terminar él mismo
#name es el nombre del proceso
class ProcesoFacilito(multiprocessing.Process):
    def __init__(self, daemon, name):
        multiprocessing.Process.__init__(self, daemon=daemon, name=name)
    #se ejecuta automáticamente
    def run(self):
        logging.info('Este mensaje se crea en un nuevo proceso!')

if __name__ == '__main__':
    proceso_facilito = ProcesoFacilito(False, 'proceso-facilito')
    proceso_facilito.start()