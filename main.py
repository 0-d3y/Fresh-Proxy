import requests
import re
import threading
import time
import sys
import os
import platform
try:
  import pyfiglet
except:
  os.system('pip install pyfiglet')
  os.system('pip install pyfiglet')
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"

proxy_error = []
proxy_yes = []

pages = [
        'https://free-proxy-list.net/',
         'https://www.sslproxies.org/',
         'https://www.us-proxy.org/',
         'https://www.socks-proxy.net/']


def banner():
  sami = pyfiglet.Figlet(font="slant")
  banner = sami.renderText("Fresh Proxy")
  print(f"""{green}
                  Coded By Mr.SaMi : @TYG_YE
                      Version : V 1.0
""")
  print(f"{red}{banner}")

def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")
def test_proxy(proxy):
    try:
        r = requests.get('https://www.google.com',
                         proxies={'http': proxy, 'https': proxy}, timeout=3)
        if r.status_code == 200:
            with open('proxy.txt', 'a') as f:
                f.write(proxy + '\n')
                print(f'{cyan}[{green}+{cyan}]{green} Proxy Added: {cyan}' + proxy+f"{cyan}---> {cyan}[{green}Yes:{len(proxy_yes)} - {red}No:{len(proxy_error)}{green}]")
                proxy_yes.append(1)
    except:
        print(f'{cyan}[{red}-{cyan}] {red}Failed Proxy: {cyan}' + proxy+f"{cyan}---> {cyan}[{green}Yes:{len(proxy_yes)} - {red}No:{len(proxy_error)}{green}]")
        proxy_error.append(2)
    
        


def get_proxies():
    for page in pages:
        r = requests.get(page)
        proxies = re.findall(r'<td>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</td>[\s\S]*?<td>\s*?(\d{2,6})\s*?</td>', r.text)
        for proxy in proxies:
            proxy = proxy[0] + ':' + proxy[1]
            threading.Thread(target=test_proxy, args=(proxy,)).start()

if __name__ == '__main__':
    clear()
    banner()
    print(f'{cyan}[*]{green} Fetching Proxies...')
    while True:
     try:
      get_proxies()
     except:
      print(f"""
{green}[+]{green}Proxy Ok = {len(proxy_yes)}
{red}[-]{red}Proxy Error = {len(proxy_error)}
""")
      sys.exit()
