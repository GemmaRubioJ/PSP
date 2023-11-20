import psutil

def list_processes():
    process_list = []
    for process in psutil.process_iter(['pid', 'name']):
        process_info = {
            'PID' : process.info['pid'],
            'Name' : process.info['name']
        }
        process_list.append(process_info)
    return process_list

def terminate_process(pid_user):
    try:
        process = psutil.Process(pid_user)
        process.terminate()
        print(f"Process {pid_user} has been terminated.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid_user}")
    except psutil.AccessDenied:
        print(f"Access denied when trying to terminate process {pid_user}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main(): 
    while True:
        processes = list_processes()
        print(processes)
        pid_user = int(input("Introduce el PID a terminar : "))
        terminate_process(pid_user)

if __name__ == '__main__':
    main()