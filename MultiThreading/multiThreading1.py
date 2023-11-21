import threading
import time
import random

#Definir la tarea que van a realizar los hilos
def thread_task(id, number_of_writings):
    sleep_time = random.uniform(0.1, 0.3)
    for i in range (number_of_writings):
        time.sleep(sleep_time)
        print(f"Soy  {id}")


def main():
    #Crear el Pool de Hilos
    thread_pool= []
    for i in range(10): #pool de 10
        number_of_writings = random.randint(5,15)
        thread = threading.Thread(target=thread_task, args=(i, number_of_writings))
        thread_pool.append(thread)
    #inicializar todos los hilos
    for thread in thread_pool:
        thread.start()
    #esperar a que todos los hilos terminen
    for thread in thread_pool:
        thread.join()
    print("Todos los hilos han terminado su ejecución")

if __name__ == "__main__":
    main()