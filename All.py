import os
import threading

def Dayi():
  os.system("python3 Dayi.py")

def Alcapone():
  os.system("python3 Alcapone.py")

def Yenna():
  os.system("python3 Yenna.py")

t1= threading.Thread(target=Dayi)
t2= threading.Thread(target=Alcapone)
t3= threading.Thread(target=Yenna)

t1.start()
t2.start()
t3.start()
