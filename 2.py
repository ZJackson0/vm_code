import socket

def send(host, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(message.encode())
    s.close()

input = input(">>")
send("127.0.0.1", 10001, input)

