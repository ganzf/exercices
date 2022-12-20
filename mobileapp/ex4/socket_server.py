import socket
import threading
import time
import base64


def send_to_client(c, data):
    start_time = time.time()
    while time.time() - start_time < 300:
        print("sending data")
        c.send(data)
        time.sleep(5)


def socket_server():
    #Retrieve image data
    image_bytes = b''
    with open("image.jpg", "rb") as image_file:
        image_bytes = base64.b64encode(image_file.read())
        size = str(len(image_bytes))
        print(size)
        

    host = "127.0.0.1"
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    (clientConnected, clientAddress) = s.accept()
    print("Got new client")
    print("sending picture size.. ")
    clientConnected.send(size.encode())
    t = threading.Thread(target=send_to_client, args=(clientConnected, image_bytes))
    t.start()
    t.join()
    s.close()

socket_server()
