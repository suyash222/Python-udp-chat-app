#! /usr/bin/python3

import socket
import threading
from time import sleep

def receving(sock):
    while True:
        print(sock.recv(1024).decode())

def sending(sock):
    while True:
        message = input('').encode()
        sock.sendto(message, (server_ip, server_port))
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = input("Server IP address: ")
server_port = int(input("Server port number: "))
client_ip = input("Client IP address: ")

while True:

    client_port = int(input("Enter Port number: "))

    try:
        sock.bind((client_ip, client_port))
    except OSError as a:
        if(a.errno == 98):
            print('select another port number: ')
    else:
        break

name = input('Enter your chat name: ')
randstr = f"qwertyuioplkjhgfdsazxcvbnmip={client_ip}port={client_port};{name}".encode()
sock.sendto(randstr, (server_ip, server_port))

send_th = threading.Thread(target=receving, args=[sock])
recv_th = threading.Thread(target=sending, args=[sock])

send_th.start()
recv_th.start()
