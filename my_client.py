# 46.149.77.240
import socket
import threading

nickname = input("Your nick: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("127.0.0.1", 7777777)
client.connect(addr)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
