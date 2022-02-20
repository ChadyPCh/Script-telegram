import time
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from random import randint


api_id = 3424510          # aqui va el id de tu api
api_hash = '09012e5bdfb2a43cfe89eb4df5240c0e'		 # aqui el hash de tu api
# fill in your own details here

phone = '+5353695749'  # Cambiarlo
session_file = 'Luis'  # use your username if unsure
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

client = TelegramClient('RhaegarLaxus', api_id, api_hash,sequential_updates=True)

@client.on(events.NewMessage(chats=408101137,incoming=True)) #CW bot
async def new_quest_handle(event):
    global HP,LVL,STAMINA,rangeMobs, Forest , Swamp , Valley , RandomQuest , a
    
    if "You were strolling around on your horse when you noticed" in event.raw_text:
        time.sleep(randint(10,60))
        await event.click(0) 

    if "To accept their offer, you shall" in event.raw_text:
        time.sleep(randint(10, 30))
        await client.send_message('chtwrsbot', '/pledge')    

    if "Stamina restored." in event.raw_text:
        RandomQuest = True
        Forest = Swamp = Valley = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if a==1:
        if "Who knows what is lurking in mud." in event.raw_text:
            if RandomQuest:
                if "🔥" in event.raw_text:
                    if event.raw_text.find("🔥") == 121:
                        time.sleep(1)
                        await event.click(0,2)
                    if event.raw_text.find("🔥") == 64:
                        time.sleep(1)
                        await event.click(0,1)
                    if event.raw_text.find("🔥") == 13:
                        time.sleep(1)
                        await event.click(0,0)
                else:
                    time.sleep(3)
                    await event.click(0,randint(0,2))

            if Forest:
                time.sleep(3)
                await event.click(0, 0)

            if Swamp:
                time.sleep(3)
                await event.click(0,1)
                    
            if Valley:
                time.sleep(3)
                await event.click(0,2)

            
        if "You received:" in event.raw_text and "stands victorious over" not in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')

        #EMPTY QUEST 

        if "You found yourself in a land you where you did not want to appear again. The land crawling with vermin. Eight-legged, no-legged, and everything in between. Life here has become twisted and hateful. Nature does not stand a chance while it has creatures like that at its throat. Trying to escape from that evil place you’ve only stained your armor with blood." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')    
        if "It was a really nice and sunny day, so you sat under a tree and enjoyed the weather..." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "You fell asleep and in your dream there was a beautiful land where seven colourful armies were battling each other. “How is that different from real life and why is there a taste of mushrooms and berries in my mouth?” was your thought when you woke up" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "As you were about to head out for an adventure, you got a feeling you were forgetting something, so you wasted some time trying to remember what it was. Finally you gave up and stayed home" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Walking through the swamp, you found yourself surrounded by the mist. Suddenly you heard a dog howling in the distance. You decided to save yourself and ran back home, as your butler promised to cook some porridge." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Mrrrrgl mrrrgl mrrrrrrgl mrrrgl. Mrrrrrrrrrrrgl mrrrrgl mrrrrrrrgl mrrrrrrgl mrrrrrrrrl. Mrrrrrgl." in event.raw_text and "You received:" not in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "It was a cool and refreshing night, so you made a campfire out in the woods." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Being a naturally bad pathfinder, you got lost and just wandered around the forest for no reason." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "In the forest you met a redhead woman. Now you know nothing. You returned home empty handed" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "In and out, 20 second adventure!" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "A knight writes haikus all day," in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Looking at the overcast sky you decide to take a day off and work on your art. With the occasional ray of light breaking through the clouds you feel inspired for your work - it looks like once you finish this it's going to be a masterpiece!" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "In the forest you came upon a bold man who offered to fulfill your every wish. Being very cautious, you decided to reject his kind offer." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "On your quest you came to the town of Honeywood. Here you found a blacksmith having an argument with a garlic farmer. You wanted to buy something, but got annoyed by a fisherman who kept " in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Wandering around, you saw a little golden ball flying around. Quickly, you hopped on your broom and started chasing it. Just as you were about to catch the ball, you woke up, realising it was just a dream" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "As you were strolling through the forest, you noticed a group of people building a giant wall on a small meadow. Their leader, an orange man with crazy hair, looked dangerous, so you decided to head back to your castle" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "You've stepped into a pile of dung. Now you stink. Nothing else happened." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')   
        if "Being a naturally bad pathfinder, you got lost and just wandered around the forest for no reason." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Suddenly you were surrounded by a huge band of orcs, led by an orc shaman. They demanded you give them everything you have. You killed every single one of them and collected a lot of loot." in event.raw_text and "When you woke up, there were no orcs and most importantly - no loot. Such a pity" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "You found yourself in a land you where you did not want to appear again. The land crawling with vermin. Eight-legged, no-legged, and everything in between. Life here has become twisted and hateful. Nature does not stand a chance while it has creatures like that at its throat. Trying to escape from that evil place you’ve only stained your armor with blood" in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Somewhere in the forest, you encounter a deer who stops you and asks if you wish to make a trade- your lunchbox for her 31 pouches of gold. Before you could say a word, an urn smashes the poor deer." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "Statistically speaking, you come back empty handed from every third adventure in the forest. Seems like you drew your lucky ticket. You came back from the forest. And guess what? Nothing interesting happened." in event.raw_text:
            time.sleep(randint(5,10))
            await client.send_message('chtwrsbot','🗺Quests')
        if "In the forest you came across a tavern where all kinds of magical creatures played a card game. It was called something like Fireplacerock. You stole their golden cards but they turned into dust." in event.raw_text:
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
        MOBS = False

    if "Battle is coming" in event.raw_text:
        a=0
        MOBS = False

    if "You met some hostile creatures" in event.raw_text:
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
 

@client.on(events.NewMessage(chats=-1001657461170)) #alianza ordenes
async def new_alianza_handle(event):
    global a 
    
    if "#luis" in event.raw_text:
        orden = str(event.raw_text[6:len(event.raw_text)])
        a=0
        await client.send_message('chtwrsbot', orden)

          
@client.on(events.NewMessage(chats= -1001657461170)) #Chat de control
async def new_group_handle(event):
    global HP , LVL , MOBS , Forest , Swamp , Valley  , RandomQuest , a

    if "You met some hostile creatures" in event.raw_text and MOBS:
        await client.forward_messages('chtwrsbot',event.message)

    if "LGA" in event.raw_text:
        orden = str(event.raw_text[4:len(event.raw_text)])
        a=0
        MOBS = False
        await client.send_message('chtwrsbot', orden)


    if "Lto" in event.raw_text:
        Forest = Swamp = Valley = RandomQuest = False
        a=0
    
    if "Lq" in event.raw_text:
        RandomQuest = True
        Forest = Swamp = Valley = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Lfor" in event.raw_text:
        Forest = True
        Swamp = Valley = RandomQuest = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Ls" in event.raw_text:
        Swamp = True
        Forest = Valley = RandomQuest = False
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Lv" in event.raw_text:
        Forest = Swamp = RandomQuest = False
        Valley = True
        await client.send_message('chtwrsbot','🗺Quests')
        a=1

    if "Hp" in event.raw_text:
        await client.send_message('chtwrsbot','🏅Me')

    if "LOn" in event.raw_text:
        MOBS = True

    if "LOf" in event.raw_text:
        MOBS = False

    if "Lff" in event.raw_text:
        a=2
        await client.send_message('chtwrsbot','▶️Fast fight')

    if "Test" in event.raw_text:
        await client.send_message(-1001657461170,'Working')

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

print(time.asctime(), '-', 'Stared Luis...')
client.start(phone)
client.loop.run_forever()
print(time.asctime(), '-', 'Stopped!')

"""
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
"""
