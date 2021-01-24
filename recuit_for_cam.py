import requests
import threading
url = "https://politicsandwar.com/api/send-message/"
apikey = "d54b8cee55f6d7"
subject = "The Round Table Beckons You!"
txtmsg = open("message.txt","r")
message = txtmsg.read()
txtmsg.close()

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
            

threading.Timer(60, repeatfunction).start()
