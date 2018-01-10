import socket
UDP_IP_ADDRESS = 'localhost'
UDP_PORT = 48051 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((UDP_IP_ADDRESS, UDP_PORT))
while True:
    data = client.recvfrom(4096)
    print(data)
