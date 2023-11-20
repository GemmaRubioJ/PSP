
from multiprocessing import Process



def print_cube(num):
    print(f"The cube of {num} is {num ** 3}")

def print_square(num):
    print(f"The cube of {num} is {num ** 2}")

def run_parallel_task(func, num):
    process= Process(target=func, args=(num,))
    process.start()
    return process

def main():
    numbers= [2, 3, 4, 5]
    processes=[]
    for num in numbers:
        processes.append(run_parallel_task(print_cube, num))
        processes.append(run_parallel_task(print_square, num))
        
    for process in processes : 
        process.join()

if __name__ == '__main__':
    main()