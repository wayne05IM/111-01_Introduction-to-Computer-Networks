from http import client
import socket
import time

with open('./B09705039_p1_client_result.log', 'w') as logFile:
    logFile.write("The Client is running..\n")
    logFile.flush()

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # TODO start
    # If connect to local
    HOST, PORT = "127.0.0.1", (5039 + 1023) % 65535
    # if connect to remote
    # HOST, PORT = "140.112.42.104", 7777
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    # TODO end

    Testcase = open('./p1_testcase', 'r')
    TestcaseContents = Testcase.readlines()
    Testcase.close()

    # Write the information of HOST and PORT to the client_log.txt
    # TODO start
    logFile.write("Connected to " + HOST + ", using port number " + str(PORT) + "\n")
    logFile.flush()
    # TODO end

    # Read test cases from p1_testcase
    # You can change the test case or create other test cases on your own
    
    # line count
    count = 1
    for PreprossingLine in TestcaseContents:
        Line = PreprossingLine.strip()

        # For connection stability
        time.sleep(3)
        
        # Client sent the request to the server and receive the response from the server
        # TODO start
        if count % 2 == 1:
            # receive "Please input a question for calculation"
            message = clientSocket.recv(1024).decode()
            logFile.write("Received the message from server: " + message + "\n")
            logFile.flush()
            # pass question
            logFile.write("Question: " + Line + "\n")
            logFile.flush()
            clientSocket.send(Line.encode())
            # get answer
            message = clientSocket.recv(1024).decode()
            logFile.write("Answer: " + message + "\n")
            logFile.flush()
        else:
            # cont or not
            logFile.write(Line + "\n")
            logFile.flush()
            clientSocket.send(Line.encode())   
        count += 1 
        # TODO end


    # Close the socket
    # TODO start
    clientSocket.close()
    # TODO end
    logFile.close()
