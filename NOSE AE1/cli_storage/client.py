import socket
import sys
import os
from useful import send_file, recv_file, send_listing, recv_listing

# FUNCTIONS

def usage():
    print('Usage: <port> <put filename|get filename|list>')
    sys.exit(1)

# a function which returns a result of the request process
def processing_request(sock, func):
    result = func
    if (result == True):
        raport = "Success"
    else:
        raport = "Failure "+ str(result)
    return raport

### Argument Parser

accepted_commands = set(["put","get","list"])

try:
    port = int(sys.argv[1])
    comm = str(sys.argv[2])
    filename = "0"
    if comm not in accepted_commands:
        print('2nd Argument can be either "put" "get" or "list"')
        usage()
    if comm != "list":
        filename = str(sys.argv[3])
except Exception as e:
    print(e)
    usage()


# Connecting to the server and sending a request

try:
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_address = ("0.0.0.0", port)
    cli_sock.connect(srv_address)
    print("Connection with the server successful")

    request_msg = comm +" "+ filename
    request = cli_sock.send(request_msg.encode())
        
    while True:
        if comm == "put":
            result = processing_request(cli_sock, send_file(cli_sock, filename))
        elif comm == "get":
            result = processing_request(cli_sock, recv_file(cli_sock, filename))
        elif comm == "list":
            result = processing_request(cli_sock, recv_listing(cli_sock))

        print(srv_address,"Request Type:", comm, ("Filename: "+filename) if filename != "0" else "", "Status:", result) 
        break
    
except Exception as e:
    print(e)
    usage()

cli_sock.close()



        


