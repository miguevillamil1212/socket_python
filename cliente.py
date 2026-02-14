import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

mensaje = client.recv(1024)
nombre = mensaje.decode()
print("Hola Programación Distribuida, soy", nombre)

client.close()
