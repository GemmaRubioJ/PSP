import threading
from queue import Queue
import random
import time

#funcion del productor que genera y mete numeros en la cola
def producer(q, pt):
    while True:
        for i in range(15):
            number = random.randint(51, 1999)
            q.put(number) 
            time.sleep(pt)

#funcion del consumidor que coge numeros de la cola y calcula la suma de sus cuadrados
def consumer(q, ct, x):
    while True:
        numbers = []
        for i in range(x):
            numbers.append(q.get())
        sum_of_squares = sum(number ** 2 for number in numbers)
        print(f"Consumidor {threading.current_thread().name} suma de los cuadrados : {sum_of_squares} ")
        time.sleep(ct)



def main():
    pt = 1 #sleeptime del productor
    ct = 3 #sleetime del consumidor
    x = 5 #numeros que el consumidor lee a la vez
    queue = Queue()
    # Create and start the producer threads
    producer_thread = threading.Thread(target=producer, args=(queue, pt))
    producer_thread.daemon = True
    producer_thread.start()

    # Create and start the consumer threads
    consumer_thread = threading.Thread(target=consumer, args=(queue, ct, x))
    consumer_thread.daemon = True
    consumer_thread.start()
    for i in range(1):
        threading.Thread(target=consumer, args=(queue, pt), daemon=True).start()

    for i in range(1):
        threading.Thread(target=consumer, args=(queue, ct, x), daemon=True).start()
    time.sleep(60)
    print("Programa Productor-Consumidor terminado")

if __name__ == "__main__":
    main()
        