import time
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from random import randint

api_id = 7570073       
api_hash = '4bce4c74abc67c95cee1cee6507dabe9'	

phone = '+573013657189'  
session_file = 'SrDuwarswolf'  
string = '1AZWarzgBu217OzlIhNOvjL2mNYuLO_IipuRG46CqtCSDLDMiBnd97i9hnsnymoZGpat6nmflsY_nlqD4cN4xtudfSW8Teb8GEjn8LTfIon4ar2da3J5tDc1QdslritDOuPa70t53d3jQZ8fe-xEQDyv0w4tQa4re7ebqN_UspLldkPByciPiqOk43IT7zir5A9MEdw1sDv7Apbip1A0CwnN36ETUC4fxtrdMw9yLJREf_Ecop5K_psryDZkMCeTvvk0r8grAv8hFrZB2kWPTUpeGnYvWKvc2KvDTiYmSsesTXXYqgKsi7U9u6BsoWRIDq_ojMu09j3VyVT6ON6CdEifOLGq4zxw='
MOBS = False
HP = 0
LVL = 0
a = 0
STAMINA = 0
Forest , Swamp , Valley , RandomQuest , Foray = False , False , False , False , False
rangeMobs = {0,0,0,0,0,0,0,0,0,0}

def rang(text):
    global rangeMobs , HP
    can = False
    for i in rangeMobs:
        if (str(i) in text) and (HP > 500):
            can = True
    return can

client = TelegramClient('SrDuwarswolf', api_id, api_hash,sequential_updates=True)

@client.on(events.NewMessage(chats=408101137,incoming=True)) #CW bot
async def new_quest_handle(event):
    global HP,LVL,STAMINA,rangeMobs, Forest , Swamp , Valley , RandomQuest , a
    
    if "You were strolling around on your horse when you noticed" in event.raw_text:
        time.sleep(randint(10,60))
        await event.click(0)     

    if "Stamina restored." in event.raw_text:
        RandomQuest = True
        Forest = Swamp = Valley = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if a==1:
        if "Who knows what is lurking in mud." in event.raw_text:
            if Forest:
                time.sleep(3)
                await event.click(0, 0)

            if Swamp:
                time.sleep(3)
                await event.click(0,1)
                    
            if Valley:
                time.sleep(3)
                await event.click(0,2)

            if RandomQuest:
                time.sleep(3)
                await event.click(0,randint(0,2))

        if "You received:" in event.raw_text and "stands victorious over" not in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')

 #arenas
    if a==2:
        if "stands victorious over" in event.raw_text or "You didn’t find an opponent. Return later" in event.raw_text:
            await client.send_message('chtwrsbot','▶️Fast fight')

        if "Not enough gold to pay the entrance fee." in event.raw_text or "It's hard to see your opponent in the dark" in event.raw_text or  "You need to heal your wounds " in event.raw_text:
            a=0
            time.sleep(3)
            await client.send_message('chtwrsbot','🏅Me') 


    if "Not enough stamina. " in event.raw_text:
        a=0
        time.sleep(3)
        await client.send_message('chtwrsbot','/g_def')

    if "Battle is coming" in event.raw_text:
        a=0
        time.sleep(3)
        await client.send_message('chtwrsbot','/g_def')

    if "You met some hostile creatures" in event.raw_text:
        await client.forward_messages(-585896027,event.message) 
        await client.forward_messages(-1001156688513,event.message)

    if ("❤️Hp: " in event.raw_text) and ("Battle of the seven castles in" in event.raw_text):
            HP = (event.raw_text[event.raw_text.find("Hp:")+4:event.raw_text.find("Hp:")+8])
            LVL = int(event.raw_text[event.raw_text.find("Level:")+7:event.raw_text.find("Level:")+9])
            STAMINA = event.raw_text[event.raw_text.find("Stamina:")+9:event.raw_text.find("Stamina:")+11]
            if "/" in STAMINA:
                STAMINA = int(STAMINA[0:1])
            else:
                STAMINA = int(STAMINA)
            
            if "/" in HP:
                HP = (event.raw_text[event.raw_text.find("Hp:")+4:event.raw_text.find("Hp:")+7])
                if "/" in HP:
                    HP = (event.raw_text[event.raw_text.find("Hp:")+4:event.raw_text.find("Hp:")+6])
                    if "/" in HP:
                        HP =(event.raw_text[event.raw_text.find("Hp:")+4:event.raw_text.find("Hp:")+5])
                HP = int(HP) 
            else:
                HP = int(event.raw_text[event.raw_text.find("Hp:")+4:event.raw_text.find("Hp:")+8])

            rangeMobs = {LVL-2,LVL-1,LVL,LVL+1,LVL+2,LVL+3,LVL+4,LVL+5,LVL+6,LVL+7}
           
@client.on(events.NewMessage(chats= -585896027)) #Chat de control
async def new_group_handle(event):
    global HP , LVL , MOBS , Forest , Swamp , Valley  , RandomQuest , a

    if "Dwto" in event.raw_text:
        Forest = Swamp = Valley = RandomQuest = False
        a=0
    
    if "Dwq" in event.raw_text:
        RandomQuest = True
        Forest = Swamp = Valley = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Dwfor" in event.raw_text:
        Forest = True
        Swamp = Valley = RandomQuest = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Dws" in event.raw_text:
        Swamp = True
        Forest = Valley = RandomQuest = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Dwv" in event.raw_text:
        Forest = Swamp = RandomQuest = False
        Valley = True
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Hp" in event.raw_text:
        await client.send_message('chtwrsbot','🏅Me')

    if "DwOn" in event.raw_text:
        MOBS = True

    if "DwOf" in event.raw_text:
        MOBS = False

    if "Dwff" in event.raw_text:
        a=2
        await client.send_message('chtwrsbot','▶️Fast fight')

    if "Test" in event.raw_text:
        await client.send_message(-585896027,'Working')

@client.on(events.NewMessage(chats=807376493)) #PVE
async def new_mobs_handle(event):
    global HP , STAMINA , MOBS
    if ("Prepare yourself to fight:" in event.raw_text ) and (MOBS):
        urlfigth ='/'+ event.message.reply_markup.rows[0].buttons[0].url[event.message.reply_markup.rows[0].buttons[0].url.find("fight"):len(event.message.reply_markup.rows[0].buttons[0].url)]
        await client.send_message('chtwrsbot',urlfigth)

@client.on(events.NewMessage(from_users =  976918452,chats= 976918452, pattern= 'A new hunt is available:')) #Lycaon
async def new_LycanMobs_handle(event):
    global MOBS , HP
    if  MOBS:
        figth =  (str)(event.message.reply_markup.rows[0].buttons[0].query)
        #print(figth)
        await client.get_dialogs()
        time.sleep(1)
        results = await client.inline_query(bot='LycaonBot', query= figth , entity='LycaonBot')
        #print(results[0])
        time.sleep(1)
        message = await results[0].click('chtwrsbot')

print(time.asctime(), '-', 'Stared Duwars...')
client.start(phone)
client.loop.run_forever()
print(time.asctime(), '-', 'Stopped!')

"""
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
"""