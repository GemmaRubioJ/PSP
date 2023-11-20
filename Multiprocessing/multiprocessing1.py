
from multiprocessing.dummy import Pool as ThreadPool
import os

def my_id(task_id):
    print(f"Hi, I'm worker {task_id} (with PID {os.getpid()})")

cpu_cores = 8
pool_size = cpu_cores - 1
pool = ThreadPool(pool_size) # choose a number of workers


tasks = list(range(cpu_cores * 2)) 
pool.map(my_id, tasks)

pool.close() 
pool.join()




