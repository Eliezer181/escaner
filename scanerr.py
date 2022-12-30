import socket
from colorama import Fore

def get_open_ports():
    open_ports = []
    for port in range(1, 6555):
        print("Escaneando puerto {}".format(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        if result == 0:
            open_ports.append(port)
            print(Fore.GREEN + "Puerto abierto: {}".format(port))
        sock.close()
    if not open_ports:
        print("No hay puertos abiertos, sorry.")
    return open_ports

print(get_open_ports())
