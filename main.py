import base64
import time 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests 

def encode_event(e, t):
    r = f"{e}|{t}|{int(time.time())}"
    n = "tttttttttttttttttttttttttttttttt"
    i = n[:16]
    key = n.encode('utf-8') 
    iv = i.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(r.encode('utf-8'), AES.block_size))
    return base64.b64encode(base64.b64encode(encrypted)).decode('utf-8')

# replace your query id in the headers 
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'lan': 'en',
    'origin': 'https://bbqapp.bbqcoin.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bbqapp.bbqcoin.ai/',
    'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'use-agen': 'query_id=AAEO_is2AgAAAA7-KzZ_meMV&user=%7B%22id%22%3A5203820046%2C%22first_name%22%3A%22Ymx%20haxor%F0%9F%8D%85%E2%96%AA%EF%B8%8F%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1730348153&hash=c34c769e8c32743e4fd50d79a35ae46874d3a0d2dd025364b2bf3bfa1f8560e5',
    'user-agent': 'add your custom header here ',
    'x-requested-with': 'org.telegram.messenger',
}

user_id = '5203820046'#telegram user ID
taps = '3000' #amount of taps
def bbq_tap():
    data = {
        'id_user':user_id,
        'mm': taps ,
        'game': encode_event(user_id,taps),
    }
    response = requests.post('https://bbqbackcs.bbqcoin.ai/api/coin/earnmoney', headers=headers, data=data)
    print(response.json())
bbq_tap()
