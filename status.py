#
import vk
import random
import time
import logging
from time1 import ftime
from get_comment import get_comment
logging.basicConfig(level = logging.ERROR, filename = 'mylog.log')
while True:
    try:
        session = vk.Session()
        session = vk.AuthSession('5001234', "89999696689", "PoPcorN698h", scope='wall, users, status, photos')
        vk_api = vk.API(session)
        api = vk.API(session)
        while True:
            kolvo0 = get_comment(vk_api)
            if kolvo0 != 0:
                kol = int(kolvo0)
            else:
                kol = 600
            resp = vk_api.wall.get(owner_id = "-35029664", count = "100", filter = "owner")
            while True:
                i = random.randint(2,99)
                if int(resp[i]["marked_as_ads"]) != 1 and len(resp[i]["text"].encode('utf-8'))<250:
                    break;
            a = resp[i]["text"].encode('utf-8')
            times = a.rfind("<br>")
            elo = a[times:len(a)].replace("<br>","")
            a = a[0:int(a.find("<br>"))]
            a = '"' + a + '" - ' + elo
            log = a + " (" +time.ctime(time.time()) + ")"
            logging.critical(log)
            print log
            vk_api.status.set(text = a + "    " + ftime())
            time.sleep(kol)
    except:
        logging.critical("error")
