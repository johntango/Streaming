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

        # its an ongoing message so add next chunk
        full_msg += msg
        if len(full_msg) >= msg_len + HEADER:
            # we have complete message and maybe more
            print(f"Message:{full_msg[0:msg_len+HEADER]}")
            #  Start of next message may be in full_msg
            #
            #  Enter Code Here and correct
            #  below to deal with start of next message
            #
            full_msg = ""
            new_msg = True
