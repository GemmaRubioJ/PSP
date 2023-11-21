import threading
import random
import time

#crear la lista de numeros
lista = []
lista_lock = threading.Lock()
#el evento que hace parar a los hilos
stop_event = threading.Event()

#tarea del hilo que genera numero aleatorios y los mete en la lista
def generate_numbers():
    while not stop_event.is_set():
        with lista_lock:
            lista.append(random.randint(1,100))
        time.sleep(0.01) #ponemos a dormir para evitar que se solapen

#tarea que sustituye los numeros acabados en 0
def replace_zeros():
    index= 0
    while not stop_event.is_set():
        with lista_lock:
            if index < len(lista) and lista[index] % 10 == 0:
                lista[index] = -1
            index = (index+1) % len(lista) if lista else 0
        time.sleep(0.01)

#tarea que para los hilos cuando sumen 20000
def stop_threads():
    while not stop_event.is_set():
        with lista_lock:
            if sum(lista)>20000:
                stop_event.set()
        time.sleep(0.01)

#crear los threads
thread1 = threading.Thread(target=generate_numbers)
thread2 = threading.Thread(target=replace_zeros)
thread3 = threading.Thread(target=stop_threads)

def main():
    #inicializar los hilos
    thread1.start()
    thread2.start()
    thread3.start()
    #esperar a que el hilo de parada termine
    thread3.join()
    #indicar al resto de hilos en caso de que no hayan checkeado el evento todavía
    stop_event.set()
    #esperar a los otros hilos a que terminen
    thread1.join()
    thread2.join()
    print("Los hilos han parado")
    print(f"Suma final de la lista: {sum(lista)}")
    print(f"Lista final: {lista}")

if __name__ == "__main__":
    main()