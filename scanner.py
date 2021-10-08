import threading
import socket
from tqdm import tqdm

adr = '89.108.93.102'

free_port = []
start = 0
finish = 500
NumbersOfThreads = 150
one_percent = int((finish-start)/100)
all_port = [i for i in range(start, finish)]
procent = 0
pbar = tqdm(total=100)


def port_connect(adr, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    if conn.connect_ex((adr, port)):
        return False
    else:
        return port


def port_thread():
    while all_port:
        global procent
        global loading
        port = all_port.pop()
        procent += 1
        if procent % one_percent == 0:
            pbar.update(1)
        if port_connect(adr, port):
            free_port.append(port)
    pbar.close()

threads = [threading.Thread(target=port_thread) for i in range(NumbersOfThreads)]

[i.start() for i in threads]
[i.join() for i in threads]
print("\n")
lenght = len(free_port)
print(f"Список открытых портов (всего {finish-lenght}):")
print('Закрытые порты:')

print(sorted(free_port))
print(len(free_port))
