import requests
import time
import random
import hmac
import hashlib
import base64
from urllib.parse import urlencode


# 生成签名所需的参数
def generate_signature(Authorization):
    nonce = random.randint(1, int(1e6))
    open_id = "QL6ZOftGzbziPlZwfiXM"
    timestamp = int(time.time())
    secret = "sArMTldQ9tqU19XIRDMWz7BO5WaeBnrezA"
    message = f"nonce={nonce}&openId={open_id}&timestamp={timestamp}"
    signature = hmac.new(secret.encode(), message.encode(), hashlib.sha1).digest()
    signature_base64 = base64.b64encode(signature).decode()

    return nonce, open_id, timestamp, signature_base64


nonce, open_id, timestamp, signature_base64 = generate_signature()

print(signature_base64)

# 创建请求数据
common_data = {
    "platform": "wxapp",
    "version": "5.2.41",
    "imei": "",
    "osn": "microsoft",
    "sv": "Windows 10 x64",
    "lat": 27.615520477294922,
    "lng": 113.87162780761719,
    "lang": "zh_CN",
    "currency": "CNY",
    "timeZone": "",
    "nonce": nonce,
    "openId": open_id,
    "timestamp": timestamp,
    "signature": signature_base64
}

params_data = {
    "businessType": 1,
    "brand": 26000252,
    "tenantId": 1,
    "channel": 2,
    "stallType": "PD_S_004",
    "storeId": 26075421,
    "storeType": 2,
    "cityId": 360300,
    "appId": "wxab7430e6e8b9a4ab",
    "dAId": 45306,
    "signDate": "2024-7-19"
}

# URL 和 headers
url = "https://tm-web.pin-dao.cn/user/sign/save"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1bmlvbkNvZGUiOiJQOTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcJZCI6IjIyODM2NzA4NyIsImJyYW5kIjoiMjYwMDAyNTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLciLCJpc3MiOiJwZC1wYXNzcG9ydCIsInN1YiI6IjIyODM2NzA4NyIsImlhdCI6MTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc3fQ._LgoBO5P8HjcY7JPN-4RLhN049X1Rm93IEWSjeAGMpw",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "tm-web.pin-dao.cn",
    "Origin": "https://tm-web.pin-dao.cn",
    "Referer": "https://tm-web.pin-dao.cn/naixue/sign-in?sf=&accessToken=eyJhbGciOiJIUzI1NiJ9.eyJ1bmlvbkNvZGUiOiJQOTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcJZCI6IjIyODM2NzA4NyIsImJyYW5kIjoiMjYwMDAyNTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLciLCJpc3MiOiJwZC1wYXNzcG9ydCIsInN1YiI6IjIyODM2NzA4NyIsImlhdCI6MTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc3fQ._LgoBO5P8HjcY7JPN-4RLhN049X1Rm93IEWSjeAGMpw&commonParams=%257B%2522common%2522%253A%257B%2522platform%2522%253A%2522wxapp%2522%252C%2522version%2522%253A%25225.2.41%2522%252C%2522imei%2522%253A%2522%2522%252C%2522osn%2522%253A%2522microsoft%2522%252C%2522sv%2522%253A%2522Windows%252010%2520x64%2522%252C%2522lat%2522%253A27.615520477294922%252C%2522lng%2522%253A113.87162780761719%252C%2522lang%2522%253A%2522zh_CN%2522%252C%2522currency%2522%253A%2522CNY%2522%252C%2522timeZone%2522%253A%2522%2522%252C%2522nonce%2522%253A518391%252C%2522openId%2522%253A%2522QL6ZOftGzbziPlZwfiXM%2522%252C%2522timestamp%2522%253A1721380482%252C%2522signature%2522%253A%2522ReBwN5HZ5kEXyb%252FijPs85YghI9s%253D%2522%257D%252C%2522params%2522%253A%257B%2522businessType%2522%253A1%252C%2522brand%2522%253A26000252%252C%2522tenantId%2522%253A1%252C%2522channel%2522%253A2%252C%2522stallType%2522%253A%2522PD_S_004%2522%252C%2522storeId%2522%253A26075421%252C%2522storeType%2522%253A2%252C%2522cityId%2522%253A360300%252C%2522appId%2522%253A%2522wxab7430e6e8b9a4ab%2522%252C%2522dAId%2522%253A45306%257D%257D&static_time=1721380482134",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185"
}

# 将字典转换为URL编码格式
data = {
    "common": str(common_data).replace("'", '"'),
    "params": str(params_data).replace("'", '"')
}

payload = urlencode(data)

# response = requests.post(url, headers=headers, data=payload)
#
# print(response.text)

