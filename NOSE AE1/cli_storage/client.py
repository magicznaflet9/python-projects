import socket
import sys
import os
from useful import send_file, recv_file, send_listing, recv_listing

### Argument Parser
def usage():
    print('Usage: <port> <put filename|get filename|list>')
    sys.exit(1)

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
except IndexError:
    print('Wrong Number of Arguments')
    usage()

def result_meassage(result):
    if ( result == True):
        print("Sucess")
    else:
        print("Faliure", result)
        
### initislising the connection
try:
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_address = ("0.0.0.0", port)
    cli_sock.connect(srv_address)
    print("Connection with the server successful")

    request_msg = comm +" "+ filename
    request = cli_sock.send(request_msg.encode())
    
    print("Initialising", comm, "request")
    
    while True:
        if comm == "put":
            result_meassage(send_file(cli_sock, filename))
            print("Closing connection with the server")
            cli_sock.close()
            break
        elif comm == "get":
            result_meassage(recv_file(cli_sock, filename))
            print("Closing connection with the server")
            cli_sock.close()
            break
        elif comm == "list":
            result_meassage(recv_listing(cli_sock))
            print("Closing connection with the server")
            cli_sock.close()
            break
    
except Exception as e:
    print(e)
    usage()



        


