import requests
import threading
apikey = "d54b8cee55f6d7"
subject = "Join the Round Table Today!"
Message = "| - Camelot, the Kingdom on Maroon - |

Welcome to Politics and War! I have ridden the length and breadth of the land in search of Knights who will join me in my court at Camelot. I must speak with you immediately ~

We’re about to embark on our quest to fetch the holy grail, but there is a mighty dragon guarding it. Join our ranks, and we’ll chat about Camelot after our assault...

We pride ourselves on maintaining:

A Close Community
An active discord with nightly voice chats! If you don’t have a mic, no worries; We’ve a text-channel to listen in!
A private minecraft server compatible for both java and bedrock players!
Weekly events from HOI4 to 
A detailed RP to really get into character!

A Meritocracy
Hard work earns rank, not seniority!
We vote on our issues and policies!
Transparency in the government!


The Best Economics
Cities 11-30 completely free
Funding for 12 different national projects
Emergency fund for war

A bit confused? No worries!
We offer an advanced academy to teach you the ropes. From playing the market to camelot history, we offer an unrivaled academy to help you turn your nation into a powerhouse!

Become a Knight!
I must go now. The kingdom needs me.To meet me there,
Simply join our discord (hyperlinked) and type the following command:
-ticket open applicant
This will open a new channel where we’ll discuss your qualifications as a knight."
 

doc = open("idstore.txt","r")
lastid = int(doc.read())
doc.close()


def repeatfunction():
    global lastid
    nations = requests.get("https://politicsandwar.com/api/v2/nations/"+apikey+"/&alliance_position=0").json()['data']
    switch = False
    sendtoo = []
    for nation in nations:

        if switch:
            sendtoo.append(nation['nation_id'])
        if nation['nation_id']==lastid:
            switch = True
    if len(sendtoo)>0:        
        lastid = sendtoo[-1]
        doc = open("idstore.txt","w")
        doc.write(str(lastid))
        doc.close()
        print(lastid)
        for nation in sendtoo:
            requests.post(url,{"key":apikey,"to":nation,"subject":subject,"message":message},timeout=300)
            

threading.Timer(600, repeatfunction).start()
