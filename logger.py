import requests
import sys
import os
import random
from pystyle import *

os.system("cls")

os.system(f'title REAPER - Made By: Ecstacy & JJ')



Banner = '''
  ▄▄▄  ▄▄▄ . ▄▄▄·  ▄▄▄·▄▄▄ .▄▄▄    ▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄  
  ▀▄ █·▀▄.▀·▐█ ▀█ ▐█ ▄█▀▄.▀·▀▄ █·  ██•   ▄█▀▄ ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █·
  ▐▀▀▄ ▐▀▀▪▄▄█▀▀█  ██▀·▐▀▀▪▄▐▀▀▄   ██▪  ▐█▌.▐▌▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄ 
  ▐█•█▌▐█▄▄▌▐█ ▪▐▌▐█▪·•▐█▄▄▌▐█•█▌  ▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
  .▀  ▀ ▀▀▀  ▀  ▀ .▀    ▀▀▀ .▀  ▀  .▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀

  

  ╔═══════════════════════════════╗
  ║                               ║
  ║         REAPER LOGGER V1      ║
  ║     coded by Ecstacy, JJ      ║ 
  ║                               ║
  ║                               ║
  ║                               ║
  ╚═══════════════════════════════╝

  '''

print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(Banner)))
Write.Print("[+] Starting Reaper Logger", Colors.green_to_red, interval=0.04)
print()
Write.Print("[+] Fetching IP Information . . .", Colors.dark_red, interval=0.07)
url = "%Url_here%" #Add Your ip logger url here
headers={'User-Agent': 'Mozilla/5.0 (x11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'} #User-Agent can be change whatever you want
response= requests.get(url.strip(), headers=headers, timeout=5)
print()
Write.Print("[+] IP Logged successfully ! You may now check the results on Grabify.", Colors.blue_to_cyan, interval=0.04)
print()
Write.Print("[+] Thanks for using Reaper Logger!", Colors.dark_red, interval=0.01)
Write.Print("[+] Press any key to continue . . .", Colors.dark_green, interval=0.01)
input()