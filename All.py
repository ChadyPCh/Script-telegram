import os
import threading

def Dayi():
  os.system("python3 Dayi.py")

def Alcapone():
  os.system("python3 Alcapone.py")

t1= threading.Thread(target=Dayi)
t2= threading.Thread(target=Alcapone)

t1.start()
t2.start()
