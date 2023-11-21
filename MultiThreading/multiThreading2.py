import threading
import random
import statistics

#crear un array de 100 numeros aleatorios
array =[random.randint(0,100) for i in range(100)]

#definir la tarea de cada hilo

def calculate_mean():
    print(f"La media de la tabla es {statistics.mean(array)}")

def calculate_max_min():
    print(f"El número mayor es {max(array)}")
    print(f"El número menor es {min(array)}")

def calculate_std_dev():
    print(f"La desviación típica del array es {statistics.stdev(array)}")


def main():
    threads = [
    threading.Thread(target=calculate_mean),
    threading.Thread(target=calculate_max_min),
    threading.Thread(target=calculate_std_dev)
    ]
    #inicializar los hilos
    for thread in threads :
        thread.start()
    #esperar a que terminen
    for thread in threads:
        thread.join()
    print("Todos los hilos han terminado")

if __name__ == "__main__":
    main()