import random
import time
import requests
from datetime import datetime, timedelta

headers_template = {
    "Accept": "v=1.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "webapi.qmai.cn",
    "Qm-From": "wechat",
    "Qm-From-Type": "catering",
    "Referer": "https://servicewechat.com/wx3423ef0c7b7f19af/48/page-frame.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185",
    "xweb_xhr": "1"
}

# 你的多个 Qm-User-Token
qm_user_tokens = [
    "KsRoHC34Iy8moLpHRvG_iSfkYUuheUuaoL4Gc4_53roKoxR1zCLU5b41htzjMSAS",
    'rGd0dSXPlNxtlOUXVYQIEu9i8xlw-7EbnSBU3U7IP7oI9qY9yVUkbTStxJJxq6mi'
]


def sign(token):
    url = "https://webapi.qmai.cn/web/cmk-center/sign/takePartInSign"

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()
    headers["Qm-User-Token"] = token
    headers["Content-Length"] = "64"

    data = {
        "activityId": "983701274523176960",
        "appid": "wx3423ef0c7b7f19af"
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        print("Response JSON:", response.json()['message'])
    except ValueError:
        print("Response Content:", response.text)


def queryMobilePhone(token):
    url = 'https://webapi.qmai.cn/web/catering/crm/personal-info?appid=wx3423ef0c7b7f19af'

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()
    headers["Qm-User-Token"] = token
    headers["channelCode"] = ""
    headers["gdt-vid"] = ""
    headers["multi-store-id"] = ""
    headers["promotion-code"] = ""
    headers["scene"] = "1145"
    headers["store-id"] = "216652"
    headers["work-staff-id"] = ""
    headers["work-staff-name"] = ""
    headers["work-wechat-userid"] = ""

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200，会引发HTTPError
        data = response.json()
        print(f"手机号: {data.get('data', {}).get('mobilePhone', 'No mobile phone found')}")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    except ValueError:
        print("Response Content:", response.text)


def querySignRecord(token):
    # 查询签到记录的URL
    url = 'https://webapi.qmai.cn/web/cmk-center/sign/userSignRecordCalendar'
    payload = {
        "activityId": "983701274523176960",
        "startDate": "2024-01-01",
        "endDate": "2024-08-31",
        "appid": "wx3423ef0c7b7f19af"
    }

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()
    headers["Content-Length"] = '112'
    headers["Qm-User-Token"] = token

    response = requests.post(url, headers=headers, json=payload)

    try:
        response_json = response.json()
        calculate_consecutive_days(response_json['data']['signDateList'])
    except ValueError:
        print("签到记录 Response Content:", response.text)


def calculate_consecutive_days(sign_date_list):
    # 解析签到日期
    sign_dates = [datetime.strptime(item['signDate'], "%Y-%m-%d") for item in sign_date_list]
    sign_dates.sort(reverse=True)  # 从最近的日期开始

    current_streak = 1

    for i in range(1, len(sign_dates)):
        if sign_dates[i - 1] - sign_dates[i] == timedelta(days=1):
            current_streak += 1
        else:
            break

    print(f"当前连续签到天数是：{(current_streak-1) % 30 + 1}")
    return current_streak


if __name__ == "__main__":
    for token in qm_user_tokens:
        time.sleep(random.uniform(3, 6))

        queryMobilePhone(token)
        sign(token)
        querySignRecord(token)
        print("-" * 50)
        time.sleep(random.uniform(1, 2))
