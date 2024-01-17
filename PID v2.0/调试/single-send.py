import socket
client = socket.socket()
ip_port = ('192.168.1.110', 8888)
client.connect(ip_port)
while True:
    datamanip='7 0'
    data = client.recv(1024)
    print(data.decode())
    msg_input = datamanip
    client.send(msg_input.encode())
    break