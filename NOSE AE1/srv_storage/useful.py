import sys
import socket
import os

def send_file(socket, filename):
    try:
        f = open(filename, "rb")
        data = f.read()
        while len(data) > 0:
            socket.sendall(data)
            data = f.read()
        f.close()
        return True
    except Exception as e:
        return e
    
def recv_file(socket, filename):
    try:
        f = open(filename, "xb")
        user_data = socket.recv(4096)
        while len(user_data) > 0:
            f.write(user_data)
            user_data = socket.recv(4096)
        f.close()
        return True
    except Exception as e:
        return e

def send_listing(socket):
    try:
        current_dir_path = os.getcwd()
        listing = os.listdir(current_dir_path)
        for i in listing:
            socket.send(i.encode())
        return True
    except Exception as e:
        return e    

def recv_listing(socket):
    try:
        user_data = socket.recv(4096)
        while len(user_data) > 0:
            print(user_data.decode())
            user_data = socket.recv(4096)
        return True
    except Exception as e:
        return e  
