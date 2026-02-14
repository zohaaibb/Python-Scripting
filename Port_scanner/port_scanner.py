import sys
import socket
import threading

try:
    target = sys.argv[1]
    print(f" The Target is {target}")
except IndexError:
    print(" Usage: port_scanner.py <I>")

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f" [+] Port {port} is Open")
    
    s.close()
threads = []
for port in range(1, 101):
    thread = threading.Thread(target=target,args=(port,))
    threads.append(thread)
    thread.start()

for t in threads:
    thread.join()

print("All threads are done. Moving on!")