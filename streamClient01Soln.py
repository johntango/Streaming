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
            # strip off the header
            if len(full_msg) >= HEADER:
                msg_len = int(full_msg[:HEADER])
            else:
                head = msg[:HEADER-len(full_msg)]
                msg_len = int(full_msg+head)
            new_msg = False

        full_msg += msg
        if len(full_msg) >= msg_len + HEADER:
            # strip off start of next message and put into full_msg
            next = len(full_msg) - HEADER - msg_len
            print(f"M:{full_msg[0:-next]}")
            full_msg = full_msg[-next:]  # clip off end to start new message
            new_msg = True
