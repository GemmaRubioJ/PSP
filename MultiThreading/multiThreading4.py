import threading
import random

#tarea de los hilos que suma 100 numeros random
def task(thread_id, results):
    suma = sum(random.randint(1, 1000) for i in range(100))
    results[thread_id] = suma
    print(f"Hilo {thread_id} total :  {suma}")

#diccionario para guardar los resultados
results = {}

#lista para guardar los hilos
threads= []

def main():
    #definir los hilos
    for i in range(10):
        thread = threading.Thread(target=task,args=(i, results))
        threads.append(thread)
        thread.start()
    
    #esperar a que terminen
    for thread in threads:
        thread.join()
    
    #determinar el ganador
    winner_thread_id = max(results, key=results.get)
    winner_total = results[winner_thread_id]
    print(f"El ganador es el hilo {winner_thread_id} con la suma  {winner_total}")

if __name__ == "__main__":
    main()