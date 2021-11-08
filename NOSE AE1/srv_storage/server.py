import socket
import sys
import os
from useful import send_file, recv_file, send_listing, recv_listing

def processing_request(comm, fnc):
    if ( fnc == True):
        print("Success")
        return True
    else:
        print("Failure",fnc)
        return fnc
    return
    
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv_adress = ("0.0.0.0", int(sys.argv[1]))
srv_sock.bind(srv_adress)
print(srv_adress, "server up and running")
srv_sock.listen()

current_dir_path = os.getcwd()
file_list = os.listdir(current_dir_path)

while True:
    cli_sock, cli_adress = srv_sock.accept()

    request = cli_sock.recv(1048).decode()
    print(" REQUEST ", request)
    print(" REQUEST.SPLIT ", request.split())
    comm = request.split()[0]
    filename = request.split()[1]
    
    print("request recived: ", comm, filename if filename != "0" else "")

    if comm == "put":
        processing_request(comm, recv_file(cli_sock, filename))
        cli_sock.close()
        break
    elif comm == "get":
        processing_request(comm, send_file(cli_sock, filename))
        cli_sock.close()
        break
    elif comm == "list":
        processing_request(comm, send_listing(cli_sock))
        print("closing client socket")
        cli_sock.close()
        break

print("Closing server socket")
srv_sock.close()
    
