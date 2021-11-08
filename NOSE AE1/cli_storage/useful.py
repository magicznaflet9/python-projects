import sys
import socket
import os

def send_file(socket, filename):
    try:
        f = open(filename, "rb")
##        file_content = f.read()
        socket.sendall(f.read())
        f.close()
        return 1
    except Exception as e:
        print("send_file issue")
        return e
    
def recv_file(socket, filename):
    try:
        f = open(filename, "xb")
        user_data = socket.recv(4096)
        while len(user_data) > 0:
            f.write(user_data,end="")
            user_data = socket.recv(4096)
        f.close()
        return True
    except Exception as e:
        print(e,"recv_file issue")
        return e

def send_listing(socket):
    print("Creating a listing")
    try:
        current_dir_path = os.getcwd()
        listing = os.listdir(current_dir_path)
        for i in listing:
            socket.send(i.encode())
        return True
    except Exception as e:
        print("send_listing issue")
        return e    

def recv_listing(socket):
    print("Reciving a listing")
    try:
        user_data = socket.recv(4096)
        while len(user_data) > 0:
            print(user_data.decode())
            user_data = socket.recv(4096)
        return True
    except Exception as e:
        print("recv_listing issue")
        return e  
