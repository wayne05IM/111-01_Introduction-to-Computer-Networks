import socket
from datetime import datetime

with open('./server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address
    # TODO start
    HOST, PORT = "127.0.0.1", (5039 + 1023) % 65535
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    # TODO end

    while True:
        # Listen to any request
        # TODO start
        serverSocket.listen()
        # TODO end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        while True:
            try:
                # Accept a new request
                # TODO start
                Client, Addr = serverSocket.accept()
                # TODO end

                while True:
                    Client.send(("Please input a question for calculation").encode())
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # TODO start
                    # input string
                    sentence = Client.recv(1024).decode()
                    sentence = sentence.split()
                    
                    # Calculate result
                    result = 0
                    if sentence[1] == "+":
                        result = float(sentence[0]) + float(sentence[2])
                    elif sentence[1] == "-":
                        result = float(sentence[0]) - float(sentence[2])
                    elif sentence[1] == "*":
                        result = float(sentence[0]) * float(sentence[2])
                    elif sentence[1] == "/":
                        result = float(sentence[0]) / float(sentence[2])
                    Client.send((str(result) + "\n" + "Do you wish to continue? (Y/N)").encode())
                    cont = False
                    
                    # continue or not
                    cont_or_not = Client.recv(1024).decode()
                    if cont_or_not != "Y":
                        break
                        
                Client.close()
                    # TODO end
            except ValueError:
                continue
        break
    logFile.close()
    # Close the socket
    # TODO start
    serverSocket.close()
    # TODO end
