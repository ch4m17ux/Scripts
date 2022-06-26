import socket
import random
from threading import Thread
from datetime import datetime
SERVER_HOST = "localhost"
SERVER_PORT = 9001 # server's port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
while True:
    message = s.recv(1024).decode()
    print(message.replace("\n",""))
    if message.__contains__("white"):
        print("white")
        s.sendall(("white").encode())
    if message.__contains__("rings"):
        print("19")
        s.sendall(("19").encode())
    if message.__contains__("Guybrush"):
        print("threepwood")
        s.sendall(("threepwood").encode())
    if message.__contains__("armored"):
        print("mithril")
        s.sendall(("mithril").encode())
    if message.__contains__("token"):
        break
s.close()
