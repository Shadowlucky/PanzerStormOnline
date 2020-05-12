import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "26.88.119.31"
        self.port = 5555
        self.address = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)

    def recv(self):
        try:
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

