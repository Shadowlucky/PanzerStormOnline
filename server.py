import socket
from _thread import start_new_thread


server = '26.88.119.31'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as error_bind:
    print(error_bind)

s.listen(3)
print('Waiting...')


def mode_str(l):
    for n in range(len(l)):
        l[n] = str(l[n])
    return l


def thread(conn, ip):
    global ips
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode().split(';')
            conn.send(f'ok'.encode())
            for addr in ips.keys():
                if addr != conn:
                    addr.send(f'coords;{reply[0]};{reply[1]};{ip}$'.encode())
        except socket.error as e:
            print(e)
            break

    for addr in ips.keys():
        if addr != conn:
            addr.send(f'delete;{ip}$'.encode())
    ips.pop(conn)
    print('Lost Connection:', ip)
    conn.close()


ips = {}
while True:
    connect, address = s.accept()
    print('Подключен -', address)

    ips[connect] = address
    start_new_thread(thread, (connect, address))
