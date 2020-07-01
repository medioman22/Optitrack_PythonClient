import os,sys, struct
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 9000
MESSAGE = [1, 2, 3, 4, 5, 6, 7, 8]*13

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

# for i in range(0,100):
while True:

    strs = 'ifffffff'*13

    data_packed = struct.pack(strs, *MESSAGE)

    print('{}\n\n\n'.format(data_packed))

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(data_packed, (UDP_IP, UDP_PORT))
    # time.sleep(0.1)
