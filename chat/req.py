#python3.8
""""""
import json

import requests
from bs4 import BeautifulSoup

# import config

class config:
    #
    HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
            }
    APP_URL = "https://store.steampowered.com/app/"

def parse(data):

    datata = {}
    title = data["title"]
    type_ = {}

    for sys in data["SYSREQs"]:
        type = sys.ul.find("strong",recursive=False)#.text.strip().upper()
        if type == None:
            type = "SYSTEM REQUIREMENTS"
        else:
            type = type.text.strip().upper()

        bb_ul = sys.find("ul",{"class":"bb_ul"})
        type_[type] = {}

        for child in bb_ul.children:
            try:
                key = child.text.split(":")[0].strip()
                value = child.text.split(":")[1].strip()
                type_[type].setdefault(key,value)
            except:
                type_[type].setdefault("addition",child.text.strip())

    datata.setdefault(title,type_)
    print("%s Done" % title)
    return datata,title

def write_miss(app_id,message):
    """"""
    with open("miss.txt","a") as miss:
        miss.write(app_id+" "+message+"\n")

def scrapesysreq(app_id):
    """"""
    url = config.APP_URL + app_id   
    r = requests.get(url,headers=config.HEADERS)

    if r.ok == False:
        message = "Requests Not Ok %s" % app_id
        # print(message)
        write_miss(app_id,message)
        return False

    response = r.text
    soup = BeautifulSoup(response,"html.parser")

    #Game title:
    data = {}
    g_title = soup.find("div",{"class":"apphub_AppName"})#.text.strip()
    if g_title == None:
        g_title = app_id
    else:
        g_title = g_title.text.strip()

    #sysreq_contents container
    sysreq_contents = soup.find("div",{"class":"sysreq_contents"})
    if sysreq_contents:

        #Win System:
        win_os = sysreq_contents.find("div",{"data-os":"win"})

        if win_os == None:
            message = "%s Have no <div data-os=\"win\"" % g_title
            # print(message)
            write_miss(app_id,message)
            return False

        else:
            sysreqcontainer = []
            full = win_os.find("div",{"class":"game_area_sys_req_full"})
            if full == None:
                left = win_os.find("div",{"class":"game_area_sys_req_leftCol"})
                sysreqcontainer.append(left)
                right = win_os.find("div",{"class":"game_area_sys_req_rightCol"})
                sysreqcontainer.append(right)
            else:
                sysreqcontainer.append(full)
            data.setdefault("title",g_title)
            data.setdefault("SYSREQs",sysreqcontainer)
            return data

    elif sysreq_contents == None:
        message = "%s Have no <div class=\"sysreq_contents\"> " % g_title
        # print(message)
        write_miss(app_id,message)
        return False

def req(inp):
    inp.replace(" ","+")

    url = f"https://store.steampowered.com/search/?term={inp}"
    r = requests.get(url,headers=config.HEADERS)
    if r.ok:
        response = r.text
        soup = BeautifulSoup(response,"html.parser")
        apps = soup.findAll("a",{"class":"search_result_row ds_collapse_flag"})
        # print(apps[0]['data-ds-appid'])
    apps = apps[0]['data-ds-appid']

    #too long

    # with open("datata2.json","w", encoding='utf-8') as j_f:
    list = []
    
    sysreqcontainer = scrapesysreq(apps)
    if sysreqcontainer:
        data,title = parse(sysreqcontainer)
        list.append(data)
        # print(title)
        # print(data[title])
        return data[title],title
        # json.dump(list, j_f, ensure_ascii=False, indent=4)


