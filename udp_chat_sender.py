import socket
import threading
import sys

SENDER_PORT=55555
RECVER_PORT=55556

def print_chat():
    with open('udp_chat.txt', 'r') as file:
        file_content=file.read()
        print(file_content)

def send_message(sock, message, host, port):
    sock.sendto(message.encode(), (host, port))

def sender(sock, host):
    while True:
        message=input("Send: ")
        send_thread1 = threading.Thread(target=send_message, args=(sock, message, host, RECVER_PORT))
        send_thread2 = threading.Thread(target=send_message, args=(sock, message, '127.0.0.1', RECVER_PORT))
        send_thread1.start()
        send_thread2.start()
        if message.lower() == 'exit':
            break

if __name__ == "__main__":
    host=input("Who do you want to chat with: ")
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', SENDER_PORT))

    print_chat()
    sender(sock, host)
    sock.close()
