# import sockets library
from socket import *

# serverName will be the server that we'll use. We will later be able to 
# type either an IP address (your local IP) or a host address (for ex: google.com). If the
# latter is used, a DNS lookup will be done to get the IP of the host.
serverName = 'localhost'

# the port where the server will be listening for requests. Can be random. Don't use a common one (for ex: port 80 [HTTP])
serverPort = 12000

# here we bind the IP address to the transport layer protocol. 
# :param AF_INET: tells the underlying OS to get the IP address of the host
# :param SOCK_DGRAM: tells the OS this is a UDP datagram
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get a message from console
message = raw_input('Input lowercase sentence: ')

# create a packet with the IP and port with a payload (message) and send it to the UDP socket (clientSocket). Then wait for a response from the server
clientSocket.sendto(message,(serverName, serverPort))

# save the data received from the server in a variable called modifiedMessage
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print it
print modifiedMessage

# close the socket, terminate the process
clientSocket.close()