import threading
import queue
import time
import random

q = queue.Queue()

class Productor(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        
    def run(self):
        while True:
            self.q.put(1)
            self.q.put(random.randint(1,5))
            print("Contenido de la lista: " +  str(list(q.queue)))
            time.sleep(1)

class Consumidor(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        
    def run(self):
        while True:
            a=self.q.get()
            b=self.q.get()
            print(a+b)
            time.sleep(3)

p = Productor(q)
c = Consumidor(q)

p.start()
c.start()

p.join()
c.join()