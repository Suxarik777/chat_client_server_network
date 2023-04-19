import socket
import threading

LOCAL_HOST = "127.0.0.1"

host = LOCAL_HOST
port = 4444

server_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_test.bind((host, port))
server_test.listen()

clients_data = []
nicks_data = []


def broadcast(message):
    for client in clients_data:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients_data.index(client)
            clients_data.remove(client)
            client.close()
            nickname = nicks_data[index]
            broadcast(f'{nickname} left!'.encode('ascii'))
            nicks_data.remove(nickname)
            break


def accept_message():
    while True:
        client, address = server_test.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicks_data.append(nickname)
        clients_data.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server if listening...")
accept_message()
