import os
import threading

def PedroSam():
  os.system("python3 PedroSam.py")

def Bia():
  os.system("python3 Bia.py")

def Richar():
  os.system("python3 Richar.py")

t1= threading.Thread(target=PedroSam)
t2= threading.Thread(target=Bia)
t3= threading.Thread(target=Richar)

t1.start()
t2.start()
t3.start()