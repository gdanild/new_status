import vk
import random
import time
import logging
logging.basicConfig(level = logging.ERROR, filename = 'mylog.log')
session = vk.Session()
session = vk.AuthSession('5001234', "89999696689", "PoPcorN698h", scope='wall, users, status')
vk_api = vk.API(session)
api = vk.API(session)
resp = vk_api.wall.get(owner_id = "-35029664", count = "100", filter = "owner")
while True:
    while True:
        i = random.randint(2,99)
        if int(resp[i]["marked_as_ads"]) != 1 and len(resp[i]["text"].encode('utf-8'))<250:
            break;
    a = resp[i]["text"].encode('utf-8')
    times = a.rfind("<br>")
    elo = a[times:len(a)].replace("<br>","")
    a = a[0:int(a.find("<br>"))]
    a = '"' + a + '" - ' + elo
    print a
    logging.critical(a)
    # vk_api.status.set(text = a)
    time.sleep(5)

