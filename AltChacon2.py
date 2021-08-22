import time
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from random import randint

API_ID = 2393137
API_HASH = '8203e58a082b0a00b8d0740175c4cec3'
string = '1AZWarzMBu6_YDGgDQI-fAtvPzaZDvxtFAoM6cPEiw_Po4i17P-cg1zUfazUtvgOE31S9MgKHLNwok8TdytOKJHzxUhJF4JIQCafmRVYGdbErbHFxD8ay082NBqMbazmPiEu7_AkbvCOcuXrb3ySOtYLL2S-D8Oxu0faaYm30aqcduelB1YXzKef0uuGkpfPasyT7AbLgqL0OKJfO7ZoUAu02W2YeFC6yxnL3hHf1dAFoi1JfTkk1CjU0tphDQ_JoTLrUdIKqxpZVAs0TH4fXL943fhgQCoXesm39mmzk272QtLZgYhvJgoIEFtsb69mDv5hAZBwD_LsSHjs10859vbvmpAyjZOw='
phone = '+53 54632942'
Forest , Swamp , Valley , RandomQuest , Foray = False , False , False , False , False
a=0
Richar = TelegramClient('resurrection_knight',API_ID,API_HASH,sequential_updates=True) 
@Richar.on(events.NewMessage(chats=408101137,incoming=True))
async def new_CW_handle(event):
    global HP , a , LVL , STAMINA , rangeMobs , Forest , Swamp , Valley , RandomQuest, Foray
    #print('   ',event.peer_id)
#FOR START QUESTS IF YOU'VE FULL STAMINA
#  
    if "Stamina restored." in event.raw_text:
            a = 1
            Foray = True
            await Richar.send_message('chtwrsbot','🗺Quests')

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

            if Foray:
                time.sleep(1)
                await event.click(1,1)

        if "You received:" in event.raw_text and "stands victorious over" not in event.raw_text:
            time.sleep(randint(5,10))
            await Richar.send_message('chtwrsbot','🗺Quests')

        if "was completely clueless" in event.raw_text or "tried stopping you,"  in event.raw_text or "noticed you and nearly"  in event.raw_text:
            time.sleep(randint(5,10))
            await Richar.send_message('chtwrsbot','🗺Quests')



#########################################################################################################
#WHEN YOU HAVN'T STAMINAS
    if "Not enough stamina. " in event.raw_text:
        a=0
        time.sleep(3)
        await Richar.send_message('chtwrsbot','🛡Defend')
        
    if "Battle is coming" in event.raw_text:
        a=0
        time.sleep(3)
        await Richar.send_message('chtwrsbot','🛡Defend')


@Richar.on(events.NewMessage(chats=-492486194))
async def new_group_handle(event):
    global HP , a , LVL , Forest , Swamp , Valley  , RandomQuest , Foray
    
#FOR UPDATE KNOW ABOUT YOUR LIFE
  
#############################################################################
#FOR START AND OFF THE QUEST


    if "Chq" in event.raw_text:
        RandomQuest = True
        Forest = Swamp = Valley = Foray = False
        a = 1
        await Richar.send_message('chtwrsbot','🗺Quests')

    if "Chto" in event.raw_text:
        a = 0
        Foray = Forest = Swamp = Valley = RandomQuest = False

    if "Chforay" in event.raw_text:
        a = 1
        Forest = Swamp = Valley = RandomQuest = False
        Foray = True
        await Richar.send_message('chtwrsbot','🗺Quests')

    if "Chfor" in event.raw_text:
        a = 1
        Forest = True
        Swamp = Valley = RandomQuest = False
        await Richar.send_message('chtwrsbot','🗺Quests')

    if "Chs" in event.raw_text:
        a = 1
        Swamp = True
        Forest = Valley = RandomQuest = False
        await Richar.send_message('chtwrsbot','🗺Quests')

    if "Chv" in event.raw_text:
        a= 1 
        Forest = Swamp = RandomQuest = False
        Valley = True
        await Richar.send_message('chtwrsbot','🗺Quests')


#####################################################################################
#FastFight
    if "Chff" in event.raw_text:
        await Richar.send_message('chtwrsbot','▶️Fast fight')
    
###########################################################################################################################
#MOBS

print(time.asctime(), '-', 'Stared Resurrection...')
Richar.start(phone)
Richar.loop.run_forever()
print(time.asctime(), '-', 'Stopped!')
"""
with TelegramClient(StringSession(), API_ID,API_HASH) as client:
    print(client.session.save())
"""
