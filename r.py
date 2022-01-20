import json
from uuid import UUID
import uuid
import random
import string
import base64
import hmac
from hashlib import sha1
from time import time as timestamp
from time import sleep
import requests
import aiohttp
import asyncio
import threading

HEX_KEY = "76b4a156aaccade137b8b1e77b435a81971fbd3e"
uid: str = str(uuid.uuid4())
mac: hmac.HMAC = hmac.new(bytes.fromhex(HEX_KEY), "2".encode() + sha1(uid.encode()).digest(), sha1)
uniqueId: str = "32" + sha1(uid.encode()).digest().hex()
device: str = (uniqueId + mac.hexdigest()).upper()


headers = {'NDCLANG': 'en', 'NDCDEVICEID': device, 'SMDEVICEID': 'b89d9a00-f78e-46a3-bd54-6507d68b343c', 'Accept-Language': 'en-US', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)', 'Host': 'service.narvii.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
async def join(chatId, session):
	async with session.post(f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chatId}/member/{uid}", headers=headers) as res:
		pass
async def spam(message,messageType, session, chat):
    async def spams(message, messageType, session):
	    data = {
	        "type": messageType,
	        "content": message,
	        "clientRefId": int(timestamp() / 10 % 1000000000),
	        "attachedObject": None,
	        "timestamp": int(timestamp() * 1000)
	    }
	    data = json.dumps(data)
	    async with session.post(url=f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chat}/message",headers=headers,data=data) as res:
	        pass
    await asyncio.gather(*[asyncio.create_task(spams(message=message,messageType=messageType, session=session)) for gay in range(100)])

email=str(input("Введите почту: "))
password=str(input("Введите пароль: "))

data = {"email": email,
"secret": f"0 {password}",
"deviceID": device,
"clientType": 100,
"action": "normal",
"timestamp": int(timestamp() * 1000)}
data = json.dumps(data)
signature = base64.b64encode(bytes.fromhex("32") + hmac.new(bytes.fromhex("fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2"), data.encode("utf-8"), sha1).digest()).decode("utf-8")
headers["NDC-MSG-SIG"]=signature
res = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/login", data=data, headers=headers).json()
headers.pop("NDC-MSG-SIG")
headers["NDCAUTH"]=f"sid={res['sid']}"
uid=res["auid"]
code = input("Введите ссылку на соо: ")
response = requests.get(f"https://service.narvii.com/api/v1/g/s/link-resolution?q={code}", headers=headers)
if response.status_code != 200:
    print("Шашибка получения")
comId = json.loads(response.text)["linkInfoV2"]["path"].split("x")[1].split("/")[0]

res=requests.get(f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread?type=public-all&filterType=recommended&start=0&size=100", headers=headers).json()["threadList"]
chats=[]
for i in res:
	chats.append(i["threadId"])

mes = str(input("Введите текст сообщений: "))
mestype = int(input("Введите тип сообщений: "))

async def main(mes, mestype):
    session = aiohttp.ClientSession()
    await asyncio.gather(*[asyncio.create_task(join(chatId=gay, session=session)) for gay in chats])
    while True:
        try:
        	await asyncio.gather(*[asyncio.create_task(spam(message=mes,messageType=mestype, session=session, chat=gay)) for gay in chats])
        except Exception as e:
        	pass
loop = asyncio.new_event_loop()
loop.run_until_complete(main(mes, mestype))
