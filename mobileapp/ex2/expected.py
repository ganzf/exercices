import socket
import threading
import time
import select
import base64

def recv_from_socket(s):
    data = select.select([s], [], [])
    if data[0]:
        size = int(s.recv(6).decode("utf-8"))
        print("size of data is {}".format(size))
    start_time = time.time()
    while True:
        s_data = b''
        print("waiting for data...")
        data = select.select([s], [], [])
        if data[0]:
            while len(s_data) != size:
                s_data += s.recv(size)
            with open("imageToSave.jpg", "wb") as fh:
                fh.write(base64.decodebytes(s_data))            


def socket_client():
    host = "127.0.0.1"
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    t = threading.Thread(target=recv_from_socket, args=(s,))
    t.start()
    t.join()
    s.close()

socket_client()
