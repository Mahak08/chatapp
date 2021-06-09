import os
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("\n\t\t\tEnter Your System IP : ")
port = 1234
s.bind((ip , port))

sip = input("\n\t\t\tEnter Server IP : ")
sport = 1235

print()
os.system("tput setaf 6")
os.system("figlet -c -f digital.flf CHAT APP")

def recv():
    while True:
        os.system("tput setaf 5")
        msg = s.recvfrom(1024)
        clientip = msg[1][0]
        data = msg[0].decode() 
        print("\n\t\t\t"+clientip + " sended message - " )
        os.system('tput setaf 3')
        print("\t\t\t" + data) 
        if data == "exit":
            os.system('tput setaf 7')
            os._exit(1)

def send():
    while True:
        os.system("tput setaf 2")
        print()
        msg = input("").encode()
        s.sendto(msg, (sip,sport))
        if msg.decode() == "exit":
            os.system('tput setaf 7')
            os._exit(1)


t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)
t1.start()
t2.start()

