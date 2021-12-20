import socket
import sys
import os
from useful import send_file, recv_file, send_listing, recv_listing

# a function which returns a raport on Success or Failure of the request process
def processing_request(sock, func):
    result = func
    if result == True:
        raport = "Success"
    else:
        raport = "Failure: "+ result
    return raport

try:
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    srv_adress = ("0.0.0.0", int(sys.argv[1]))
    srv_sock.bind(srv_adress)
    print(srv_adress, "server up and running")
    srv_sock.listen()
except Exception as e:
    print("Problem with connection",e)
    
try:
    while True:
        cli_sock, cli_adress = srv_sock.accept()

        request = cli_sock.recv(4086).decode()
        comm = request.split()[0]           #comm = client command
        filename = request.split()[1]
        
        if comm == "put":
            result = processing_request(cli_sock, recv_file(cli_sock, filename))
        elif comm == "get":
            result = processing_request(cli_sock, send_file(cli_sock, filename))
        elif comm == "list":
            result = processing_request(cli_sock, send_listing(cli_sock))
        
        print(cli_adress, "Request Type:", comm,("Filename: "+filename) if filename != "0" else "", "Status:", result)
        cli_sock.close()
        break
except Exception as e:
    print(e)

srv_sock.close()
    
