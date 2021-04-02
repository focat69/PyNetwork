# Code1Tech (©) 2021. Do not remove this.

import socket

class ClientConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (self.host, self.port)
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)
    
    def send_to_server(self, _str, data='ascii'):
        """
        _str: str
        data = 'ascii' (default)
        """
        try:
            self.client.send(_str.encode(data))
            reply = self.client.recv(1024).decode()
            return reply
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)
    
    def recieve_from_server(self, _bytes):
        try:
            return self.client.recv(_bytes).decode()
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (self.host, self.port)
    
    def start(self, listenmsg="Listening for a connection.."):
        try:
            self.server.bind(self.addr)
            self.server.listen()
            print(listenmsg)
            self.client, self.address = self.server.accept()
            print(f"[+] Connected to {self.address}.")
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)

    def send_to_client(self, _str, data='ascii'):
        """
        _str: str
        data = 'ascii' (default)
        """
        try:
            self.client.send(_str.encode(data))
            reply = self.client.recv(1024).decode()
            return reply
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)
    
    def recieve_from_client(self, _bytes):
        try:
            self.client.recv(_bytes).decode()
        except socket.error as e:
            print(f"[!] The following error has occurred.\n{str(e)}\nThis will be returned.")
            return str(e)
    
    def close_client_connection(self):
        self.client.close()
        
