# Echo server program
import socket
from threading import Thread


class MyThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        with self.conn:
            print('Connected by', self.addr)
            while True:
                data = self.conn.recv(1024)
                if not data: break
                self.conn.sendall(data)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("!")
    N_clients = 2
    s.listen(N_clients)
    threads = []
    for i in range(N_clients):
        conn, addr = s.accept()
        threads.append(MyThread(conn, addr))
    for thread in threads:
        thread.start()
    # while True:
    #     conn, addr = s.accept()
    #     with conn:
    #         print('Connected by', addr)
    #         while True:
    #             data = conn.recv(1024)
    #             if not data: break
    #             conn.sendall(data)
