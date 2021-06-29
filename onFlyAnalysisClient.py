import socket
import numpy as np
import queue
HEADER = 10
ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ws.connect((socket.gethostname(), 9092))

run_mean = 0.0


def analyzeMessage(msg, run_mean):
    # strip off "The time is "

    msg = msg[23:]
    if len(msg) < 1:
        return
    run_mean = (run_mean + float(msg))/2
    print(run_mean)


while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = ws.recv(16).decode('utf-8')
        print(f"got: {msg}")
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

            analyzeMessage(full_msg[:-next], run_mean)
            print(f"Message:{full_msg}")
            full_msg = full_msg[-next:]  # clip off end to start new message
            new_msg = True
