import socket
from threading import Thread
import random

# server's IP address
SERVER_HOST = "192.168.56.106"
SERVER_PORT = 8888 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize list/set of all connected client's sockets
all_cs = set()
pl = []
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
intro = "tes test test" #needs changing
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

class enemy:
    def __init__(self, typ,  health, stren, agil, intel):
        self.typ = typ
        self.m_health = health
        self.c_health = health
        self.stren = stren
        self.agil = agil
        self.intel = intel


def menu(cs):
    message = "1. Attack\n2. Defend\n3. Magic\n4. Item\n\nRemember these commands, because it will not show again\n"
    cs.send(message.encode())



def battle(cs, c, player):
    menu(cs)
    target_list = ["1. Player 1", "2. Player 2", "3. Enemy"]
    while True:
        try:
            command = cs.recv(1024).decode()
        except Exception as e:
            print(f"Error: {e}")
            all_cs.remove(cs)
        if command == "1":
            cs.send(target_list.encode())


def sto1(cs, msg):
    cs.send(msg.encode())

def stoa(msg):
    for cs in all_cs:
        cs.send(msg.encode())

"""
def adventure(cs):

    menu(cs)
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()

        except Exception as e:
            print(f"[!] Error: {e}")
            all_cs.remove(cs)
        # iterate over all connected sockets
        for client_socket in all_cs:
            if msg == "stat":
                client_socket.send(pl[0].p_stat().encode())
            if msg == "magic":
                client_socket.send(pl[1].m_list().encode())
                msg = cs.recv(1024).decode()
            if msg == "a":
                client_socket.send(pl[0].p_stat().encode())
                #if msg == "1":
                    #Damage definiontn
                #elif msg == "2":
                    #dmg
                #elif msg == "3":
                    #stuff
                #elif msg == "5"
                    #back
                #    continue
"""

class adv:
    def __init__(self, cl, stren, agil, intel):
        self.cl = cl
        if cl == "Warrior":
            self.c_hp = stren + 10
            self.m_hp = stren + 10
        elif cl == "Archer":
            self.c_hp = stren + 5
            self.m_hp = stren + 5
        elif cl == "Mage":
            self.c_hp = stren
            self.m_hp = stren
        self.stren = stren
        self.agil = agil
        self.intel = intel
        if (cl == "Mage"):
            self.spell = ["Magic Bolt", "Mind Shock", "Heal"]
        elif (cl == "Warrior" or cl == "Archer"):
            self.spell = [" ", " ", " "]

    def p_health(self):
        return f"Health {self.c_hp}/{self.m_hp}"

    def take_dmg(self, dmg):
        self.c_hp = self.c_hp - dmg

    def p_stat(self):
        return f"Class: {self.cl}\nHealth: {self.c_hp}/{self.m_hp}\nStrength: {self.stren}\nAgility: {self.agil}\nIntelligence: {self.intel}"

    def m_list(self):
        return f"Magic\n1. {self.spell[0]}\n2. {self.spell[1]}\n3. {self.spell[2]}\n\n5. Back"

def story(part):
    if part == "start":
        for cs in all_cs:
            cs.send(intro.encode())


def w_room():
    global pl1
    global pl2
    player = 1
    while player != 3:
    #while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        # add the new connected client to connected sockets
        all_cs.add(client_socket)
        if player == 1:
            pl1 = client_socket
            print("player 1")
            pl.append(adv("Warrior", 10, 5, 3)) #Should be changed with random class
        elif player == 2:
            pl2 = client_socket
            print("player 2")
            msg = "Player 2 has joined"
            pl1.send(msg.encode())
            pl.append(adv("Archer", 10, 5, 3)) #Also changed with random class
        player+=1

    # start a new thread that listens for each client's messages
        #t = Thread(target=create_player, args=(client_socket,len(all_cs)))
    # make the thread daemon so it ends whenever the main thread ends
        #t.daemon = True
    # start the thread
        #t.start()

def battle():
    sto1(pl2, "Battle")
    n_enemies = random.randint(1,2)


def trap():
    sto1(pl2, "Trap")

w_room()
n_room = 0
print(pl1)
print(pl2)

#story("start")
while n_room <= 5:
    room = random.randint(1,2)
    print(room)
    n_room += 1
    if room == 1:
        battle()
    elif room == 2:
        trap()








"""
#This is the before version of Waiting room, should be not relevant now
while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    all_cs.add(client_socket)
    if player == 1:
        pl1 = client_socket
        print("player 1")
        pl.append(adv("Warrior", 10, 5, 3))
    elif player == 2:
        pl2 = client_socket
        print("player 2")
        msg = "Player 2 has joined"
        pl1.send(msg.encode())
        pl.append(adv("Archer", 10, 5, 3))
    player+=1

    # start a new thread that listens for each client's messages
    t = Thread(target=create_player, args=(client_socket,len(all_cs)))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
"""
# close client sockets
for cs in all_cs:
    cs.close()
# close server socket
s.close()
