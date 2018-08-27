# import sockets library
from socket import *

# server will listen for requests at this port
serverPort = 12000

# create a new TCP socket in the server
serverSocket = socket(AF_INET,SOCK_STREAM)

# bind the server port (12000) to the socket 
serverSocket.bind(('',serverPort)) 

# listen for TCP connections, the 1 means the max number of 
# queued connections (at least 1)
serverSocket.listen(1)

# print a message
print 'The server is ready to receive'

# repeat forever
while 1:
    # when a TCP connection reaches, create a new socket for this
    # specific client. 3-way handshake is done
    connectionSocket, addr = serverSocket.accept() 
    # get the information that the end host sends
    sentence = connectionSocket.recv(1024) 
    # print the information 
    print "From client: %s" % sentence
    # capitalize the sentence
    capitalizedSentence = sentence.upper() 
    # print our response
    print "Our response: %s " % capitalizedSentence
    # send the data back
    connectionSocket.send(capitalizedSentence) 
    # close the TCP connection of THIS client
    connectionSocket.close()