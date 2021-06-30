import socket
HEADER = 10

ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ws.connect((socket.gethostname(), 9092))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = ws.recv(16).decode('utf-8')
        #print(f"got: {msg}")
        if new_msg:
            # get length from Header
            tmp_msg = full_msg + msg
            msg_len = int(tmp_msg[:HEADER])
            new_msg = False

        full_msg += msg
        if len(full_msg) >= msg_len + HEADER:
            total_msg_len = msg_len + HEADER
            print(f"M:{full_msg[0:total_msg_len]}")
            next = full_msg[total_msg_len:]
            full_msg = next
            new_msg = True
