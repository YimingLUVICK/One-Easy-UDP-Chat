import socket
import sys

SENDER_PORT=55555
RECVER_PORT=55556

def print_chat():
    with open('udp_chat.txt', 'r') as file:
        file_content=file.read()
        print(file_content)

def recver(sock):
    while True:
        data, addr=sock.recvfrom(1024)
        message=data.decode()

        if message.lower() == 'exit' and addr == ('127.0.0.1', SENDER_PORT):
            break
        if message.lower() == 'exit' and addr != ('127.0.0.1', SENDER_PORT):
            print('Friend has been disconnected')
        if message.lower() != 'exit' and addr == ('127.0.0.1', SENDER_PORT):
            print(f"You: {message}")
        if message.lower() != 'exit' and addr != ('127.0.0.1', SENDER_PORT):
            print(f"Frd: {message}")

if __name__ == "__main__":
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', RECVER_PORT))

    print_chat()
    recver(sock)
    sock.close()