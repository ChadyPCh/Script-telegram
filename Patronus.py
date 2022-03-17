import time
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from random import randint


api_id = 12407376          # aqui va el id de tu api
api_hash = '6dbec3d7a4409365be3b02179de64f65'		 # aqui el hash de tu api
# fill in your own details here

phone = '+5355581282'  # Cambiarlo
session_file = 'Patronus'  # use your username if unsure
MOBS = False
HP = 0
LVL = 0
a = 0
STAMINA = 0
myclass =0
myrange =0
Forest , Swamp , Valley , RandomQuest , Foray = False , False , False , False , False
rangeMobs = {0,0,0,0,0,0,0,0,0,0}

def rang(text):
    global rangeMobs , HP
    can = False
    for i in rangeMobs:
        if (str(i) in text) and (HP > 500):
            can = True
    return can

client = TelegramClient('AcereQueBola', api_id, api_hash,sequential_updates=True)

@client.on(events.NewMessage(chats=408101137,incoming=True)) #CW bot
async def new_quest_handle(event):
    global HP,LVL,STAMINA,rangeMobs, Forest , Swamp , Valley , RandomQuest , a
    
    if "You were strolling around on your horse when you noticed" in event.raw_text:
        time.sleep(randint(10,60))
        await event.click(0) 

    if "To accept their offer, you shall" in event.raw_text:
        time.sleep(randint(10, 30))
        await client.send_message('chtwrsbot', '/pledge')    
        
    if "You met some hostile creatures" in event.raw_text:
        await client.forward_messages(-1001156688513,event.message) 



@client.on(events.NewMessage(chats=-1001657461170)) #alianza ordenes
async def new_alianza_handle(event):
    global a 
    
    if "#patronus" in event.raw_text:
        orden = str(event.raw_text[10:len(event.raw_text)])
        a=0
        await client.send_message('chtwrsbot', orden)

print(time.asctime(), '-', 'Stared Patronus...')
client.start(phone)
client.loop.run_forever()
print(time.asctime(), '-', 'Stopped!')