from multiprocessing import queues
import queue
import threading
from queue import Queue
import random
import time

def producer(queu, pt):
    while True:
        for i in range(15):
            number = random.randint(51, 1999)
            queue.put(number) 
            time.sleep(pt)

def consumer(queue, ct, x):
    while True:
        numbers = []
        for i in range(x):
            numbers.append(queue.get())
        sum_of_squares = sum(number ** 2 for number in numbers)
        print(f"Consumidor {threading.current_thread().name} suma de los cuadrados : {sum_of_squares} ")
        time.sleep(ct)



def main():
    pt = 2
    ct = 6
    x = 4
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
        