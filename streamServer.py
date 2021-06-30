import socket
import time
HEADER = 10

ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ws.bind((socket.gethostname(), 9092))
ws.listen(5)

while True:
    (clientsocket, address) = ws.accept()
    print(f"Connect from {address} established")

    msg = "Hello From Server- You are Connected"
    msg = f"{len(msg):<{HEADER}}"+msg

    #clientsocket.send(bytes(msg, 'utf-8'))
# start pushing messages every 3 seconds
    for i in range(20):
        time.sleep(0)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADER}}' + msg  # what is this doing?
        clientsocket.send(bytes(msg, 'utf-8'))
        print(msg)
