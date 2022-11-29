from termcolor import colored
from time import sleep
import os 
import base64
import requests as req
from bs4 import BeautifulSoup

class menu:
    endl = "\n"
    banner = """
    ____                      _______              ___
   / __ \________  ____ ___  / __/ (_)  __   _   _<  /
  / /_/ / ___/ _ \/ __ `__ \/ /_/ / / |/_/  | | / / / 
 / ____/ /  /  __/ / / / / / __/ / />  <    | |/ / /  
/_/   /_/   \___/_/ /_/ /_/_/ /_/_/_/|_|    |___/_/       
    """
    copyright_out = "              © 𝚃𝚑𝚒𝚜 𝚃𝚘𝚘𝚕 𝙱𝚢 𝙷𝟺𝚖𝚂𝟹𝚌"
    msg_out = "             For Educational Purposes\n"
    yt_msg_out = "        ~ Tool by H4ms3c follow me on YT"
    yt_link_out = " https://www.youtube.com/@h4ms3c "
    theme_colors = ["red","green","blue","white","yellow","cyan","magneta"]
    beg_out = colored("[~]",theme_colors[0])
    space = "     "

    def typeWriter(message):
        for char in message:
            sleep(0.1)
            print(char, end='', flush=True)        

    def menu_out():
        print(colored(menu.banner+menu.endl,menu.theme_colors[0]))
        print(colored(menu.copyright_out+menu.endl,menu.theme_colors[0]))
        print(colored(menu.msg_out,menu.theme_colors[3]))
        print(colored(menu.space+menu.beg_out+menu.yt_link_out+menu.beg_out+menu.endl+menu.endl,menu.theme_colors[3]))


class checker():
    url = 'REMOVED'
    url_2 = 'REMOVED'
    list_urls = []
    def createFile():
        try:
            f = open("./premflix-results/results.txt", "a",encoding="utf-8")
            f.close()
            return True
        except IOError:
            print(colored("[!] Error while Creating File . (Check Permissions) ",menu.theme_colors[0]))
            return False
    def createFolder():
        try:
            if not os.path.exists("./premflix-results"):
                os.mkdir("./premflix-results")
            return True
        except OSError:
            print(colored("[!] Error while Creating Folder . (Check Permissions) ",menu.theme_colors[0]))
            return False
    def openFile():
        f = open("./premflix-results/results.txt", "a",encoding="utf-8")
        return f
    def decode_url(url):
        url = str(base64.b64decode(url))
        url = url.replace("b'","")
        url = url.replace("'","")
        return url
    def checking_method():
        count = 0
        f = checker.openFile()
        request = req.get(str(checker.decode_url(checker.url)))
        soup = BeautifulSoup(request.text, 'html.parser')
        for table in soup.find_all('td'):
            for link in table.find_all('a'):
                checker.list_urls.append(str(checker.decode_url(checker.url_2))+str(link.get('href')))
        for link in checker.list_urls:
            request = req.get(str(link))
            soup = BeautifulSoup(request.text, 'html.parser')  
            for accs in soup.find_all("div", {"class": "page-inner hide-cm"}):
                if(str(accs) != "" and "@" in str(accs)):
                    for acc in accs.find_all("textarea"):
                        old = str(acc).replace('<textarea class="paste-box" id="paste-box" name="paste" placeholder="Text Here..." spellcheck="false">','')
                        new = old.replace('</textarea>','')
                        f.write(new)
            count+=1
            if(count == 3):
                break
menu.menu_out()
checker.createFolder()
checker.createFile()
checker.checking_method()







