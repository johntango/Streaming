import socket
HEADER = 10
ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ws.connect((socket.gethostname(), 9092))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = ws.recv(16).decode('utf-8')
        print(f"got: {msg}")
        if new_msg:
            # strip off the header if full_msg already contains it for sure
            # Focus here as well - You will need to change something below
            if len(full_msg) >= HEADER:
                msg_len = int(full_msg[:HEADER])
            else:
                # only come here if we have a partial header already in full_msg
                # how much of msg do we need to gram rest of header
                head = msg[:HEADER-len(full_msg)]
                msg_len = int(full_msg+head)
            new_msg = False

        # its not a new message but we need to complete ongoing message
        full_msg += msg
        if len(full_msg) >= msg_len + HEADER:
            # strip off start of next message and put into full_msg
            print(f"Message:{full_msg}")
           #
           #  Enter Code Here
           #
            full_msg = ""
            new_msg = True
