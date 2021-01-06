#! /usr/bin/python3

import socket
import threading

client_list = {}

def nameing(message, client_ip, sock):
    global client_list
    a = message.rindex('=')
    b = message.index(';')
    session =  (client_ip, int(message[a+1:b:]))
    a = message.rindex(';')
    name = message[a+1::]
    client_list[client_ip] = (name, session)
    message = name + " has joined the chat"

    threading.Thread(target=sending, args=(message, sock, client_ip)).start()

def sending(message, sock, client_ip):
    global client_list
    name = client_list[client_ip][0]
    for name2, session in client_list.values():
        message2 = f'{name}: {message}'.encode()
        sock.sendto(message2, session)

def server(sock):
    
    while True:
        s = sock.recvfrom(1024)
        client_ip = s[1][0]
        message = s[0].decode()

        print(client_list)

        if message.startswith('qwertyuioplkjhgfdsazxcvbnmip'):
            nameing(message, client_ip, sock)
        else:
            threading.Thread(target=sending, args=(message, sock, client_ip)).start()

# ip = input("Input server ip address: ")
# port = int(input("Server port no: "))
    
ip = '192.168.0.105'
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

th1 = threading.Thread(target=server, args=[sock], name="th1")
th1.start()