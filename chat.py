#!/usr/bin/env python3

import socket
import threading
import sys
import time
from random import randint

class Server:
   connections = []
   peers = []

   def __init__(self):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      sock.bind(('0.0.0.0', 10000))
      sock.listen(1)
      print("Server running...")

      while True:
         conn, addr = sock.accept()
         cThread = threading.Thread(target=self.handler, args=(conn,addr))
         cThread.daemon = True
         cThread.start()
         self.connections.append(conn)
         self.peers.append(addr[0])
         print(str(addr[0]) + ":" + str(addr[1]), "connected")
         self.sendPeers()

   def handler(self, conn, addr):
      while True:
         data = conn.recv(1024)
         for connection in self.connections:
            if connection != conn:
               connection.send(data)

         if not data:
            print(str(addr[0]) + ":" + str(addr[1]), "disconnected")
            self.connections.remove(conn)
            self.peers.remove(addr[0])
            conn.close()
            self.sendPeers()
            break

   def sendPeers(self):
      p = ""
      for peer in self.peers:
         p = p + peer + ","

      for connection in self.connections:
         connection.send(b'\x11' + bytes(p, 'utf-8'))

class Client:
   username = ""
   def __init__(self, address, username):
      randomColor = randint(0, 6)
      colorStr = color.colors[randomColor]
      self.username = color.BOLD + colorStr + username + color.END
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      sock.connect((address, 10000))

      iThread = threading.Thread(target=self.sendMsg, args=(sock,))
      iThread.daemon = True
      iThread.start()

      while True:
         data = sock.recv(1024)
         if not data:
            break
         if data[0:1] == b'\x11':
            self.updatePeers(data[1:])
         else:
            print(str(data, 'utf-8'))

   def sendMsg(self, sock):
      while True:
         message = self.username
         message = message + ": " + input("")
         sock.send(bytes(message, 'utf-8'))

   def updatePeers(self, peerData):
      p2p.peers = str(peerData, 'utf-8').split(",")[:-1]

class p2p:
   peers = ['127.0.0.1']

class color:
   colors = [
      '\033[95m', # Purple
      '\033[96m', # Cyan
      '\033[36m', # Dark Cyan
      '\033[94m', # Blue
      '\033[92m', # Green
      '\033[93m', # Yellow
      '\033[91m'] # Red
   BOLD = '\033[1m'
   END = '\033[0m'

username = ""
if (len(sys.argv) == 2):
   username = sys.argv[1]
   print("Hello, " + username)

while True:
   try:
      print("Trying to connect...")
      time.sleep(randint(1, 5))
      for peer in p2p.peers:
         try:
            client = Client(peer, username)

         except KeyboardInterrupt:
            sys.exit(0)

         except:
            pass

         if randint(1, 5) == 1:
            try:
               server = Server()

            except KeyboardInterrupt:
               sys.exit(0)

            except:
               print("Couldn't start the server...")

   except KeyboardInterrupt:
      sys.exit(0)
