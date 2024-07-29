import random

import requests
import hmac
import hashlib
import base64
import time
from datetime import datetime


# 签名生成函数
def generate_signature(nonce, openId, timestamp, secret_key):
    # 生成需要签名的字符串
    n = f"nonce={nonce}&openId={openId}&timestamp={timestamp}"

    # 生成 HMAC-SHA1 签名
    signature = hmac.new(secret_key.encode(), n.encode(), hashlib.sha1).digest()

    # 将签名转换为 Base64 编码
    signature_base64 = base64.b64encode(signature).decode()

    return signature_base64


# 生成 signDate
def generate_sign_date():
    # 获取当前日期
    current_date = datetime.now()

    # 格式化日期为 "YYYY-M-D"
    sign_date = current_date.strftime("%Y-%m-%d")

    # 去掉前导零
    sign_date_parts = sign_date.split('-')
    sign_date_parts[1] = str(int(sign_date_parts[1]))
    sign_date_parts[2] = str(int(sign_date_parts[2]))
    formatted_sign_date = '-'.join(sign_date_parts)

    return formatted_sign_date


def verify():
    # 请求 URL
    url = "https://tm-api.pin-dao.cn/passport/authenticate/wxapp/verify/grc"

    # 生成动态参数
    nonce = random.randint(0, 999999)
    timestamp = int(time.time())
    signature = generate_signature(nonce, "QL6ZOftGzbziPlZwfiXM", timestamp, "sArMTldQ9tqU19XIRDMWz7BO5WaeBnrezA")

    # 请求头部
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Authorization": "Bearer null",
        "Connection": "keep-alive",
        "Content-Length": "481",
        "Content-Type": "application/json",
        "Host": "tm-api.pin-dao.cn",
        "Referer": "https://servicewechat.com/wxab7430e6e8b9a4ab/660/page-frame.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/11159",
        "storeId": "",
        "xweb_xhr": "1"
    }

    # 请求数据
    data = {
        "common": {
            "platform": "wxapp",
            "version": "5.2.41",
            "imei": "",
            "osn": "microsoft",
            "sv": "Windows 10 x64",
            "lang": "zh_CN",
            "currency": "CNY",
            "timeZone": "",
            "nonce": nonce,
            "openId": "QL6ZOftGzbziPlZwfiXM",
            "timestamp": timestamp,
            "signature": signature
        },
        "params": {
            "businessType": 1,
            "brand": 26000252,
            "tenantId": 1,
            "channel": 2,
            "stallType": None,
            "storeId": "",
            "storeType": "",
            "cityId": "",
            "appId": "wxab7430e6e8b9a4ab",
            "dAId": "",
            "type": 3,
            "wxappCode": "0e3oQM0w3IB2c33Qyq1w3fWz944oQM0t" #这个会变
        }
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data)

    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


def sign():
    # 生成动态参数
    nonce = random.randint(0, 999999)
    openId = "QL6ZOftGzbziPlZwfiXM"
    timestamp = int(time.time())
    secret_key = "sArMTldQ9tqU19XIRDMWz7BO5WaeBnrezA"

    # 生成签名
    signature = generate_signature(nonce, openId, timestamp, secret_key)

    sign_date = generate_sign_date()

    # 设置请求URL
    url = "https://tm-web.pin-dao.cn/user/sign/save"

    # 设置请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1bmlvbkNvZGUiOiJQOTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcJZCI6IjIyODM2NzA4NyIsImJyYW5kIjoiMjYwMDAyNTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLciLCJpc3MiOiJwZC1wYXNzcG9ydCIsInN1YiI6IjIyODM2NzA4NyIsImlhdCI6MTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc3fQ._LgoBO5P8HjcY7JPN-4RLhN049X1Rm93IEWSjeAGMpw",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "tm-web.pin-dao.cn",
        "Origin": "https://tm-web.pin-dao.cn",
        "Referer": "https://tm-web.pin-dao.cn/naixue/sign-in?sf=&accessToken=eyJhbGciOiJIUzI1NiJ9.eyJ1bmlvbkNvZGUiOiJQOTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcJZCI6IjIyODM2NzA4NyIsImJyYW5kIjoiMjYwMDAyNTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLciLCJpc3MiOiJwZC1wYXNzcG9ydCIsInN1YiI6IjIyODM2NzA4NyIsImlhdCI6MTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc3fQ._LgoBO5P8HjcY7JPN-4RLhN049X1Rm93IEWSjeAGMpw&commonParams=%257B%2522common%2522%253A%257B%2522platform%2522%253A%2522wxapp%2522%252C%2522version%2522%253A%25225.2.41%2522%252C%2522imei%2522%253A%2522%2522%252C%2522osn%2522%253A%2522microsoft%2522%252C%2522sv%2522%253A%2522Windows%252010%2520x64%2522%252C%2522lat%2522%253A27.615520477294922%252C%2522lng%2522%253A113.87162780761719%2522lang%2522%253A%2522zh_CN%2522%2522currency%2522%253A%2522CNY%2522%2522timeZone%2522%253A%2522%2522%2522nonce%2522%253A241623%2522openId%2522%253A%2522QL6ZOftGzbziPlZwfiXM%2522%2522timestamp%2522%253A1721577486%2522signature%2522%253A%252225GQb3r%252Fhr1680%252FzTIzk47dWXoQ%253D%2522%257D%2522params%2522%253A%257B%2522businessType%2522%253A1%2522brand%2522%253A26000252%2522tenantId%2522%253A1%2522channel%2522%253A2%2522stallType%2522%253A%2522PD_S_004%2522storeId%2522%253A26075421%2522storeType%2522%253A2%2522cityId%2522%253A360300%2522appId%2522%253A%2522wxab7430e6e8b9a4ab%2522%2522dAId%2522%253A45306%257D%257D&static_time=1721577486749",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185"
    }

    # 设置请求体
    data = {
        "common": {
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
            "openId": openId,
            "timestamp": timestamp,
            "signature": signature
        },
        "params": {
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
            "signDate": sign_date
        }
    }

    # 发送请求
    response = requests.post(url, headers, data)
    print("响应结果:", response)


if __name__ == '__main__':
    # verify()
    sign()