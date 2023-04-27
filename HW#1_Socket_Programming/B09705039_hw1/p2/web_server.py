from socket import *

# Note: After finishing the program, try to type http://127.0.0.1:6062/index.html in your browser for test

ServerSocket = socket(AF_INET, SOCK_STREAM)
# Create a socket and bind the socket to the address
# TODO start
HOST, PORT = "127.0.0.1", (5039 + 1023) % 65535
ServerSocket.bind((HOST, PORT))
# TODO end

while True:
    print('Ready to serve...')

    # Establish the connection
    # TODO start
    ServerSocket.listen()
    ConnectionSocket, Addr = ServerSocket.accept()
    print('Received a connection from:', Addr)
    # TODO end

    try:
        # Receive a HTTP request from the client
        # TODO start
        RecvMessage = ConnectionSocket.recv(1024).decode()
        print(RecvMessage)
        # TODO end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]
        print(FileName)
        f = open(FileName[1:])

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # TODO start
        DataInFile = f.read()
        DataInFile = DataInFile.splitlines()
        # TODO end

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # TODO start
        ConnectionSocket.send(("HTTP/1.1 200 OK\n").encode('utf-8'))
        # TODO end

        # Send the Content Type to the client
        # TODO start
        ConnectionSocket.send(("Content-Type:text/html\n\n").encode('utf-8'))
        # TODO end
        

        # Send the content of the requested file to the client
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send("\n".encode())

        ConnectionSocket.close()
    except IOError:
        # Send the response message if the file is not found
        # TODO start
        print("404 Not Found")
        ConnectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
        ConnectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\n".encode())
        # TODO end

        # Close client socket
        # TODO start
        ConnectionSocket.close()
        # TODO end