import json
import random
import time
import requests
from datetime import datetime, timedelta

# 请求头
headers_template = {
    'Accept': 'v=1.0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'webapi.qmai.cn',
    'Qm-From': 'wechat',
    'Qm-From-Type': 'catering',
    'Referer': 'https://servicewechat.com/wxd92a2d29f8022f40/325/page-frame.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
    'xweb_xhr': '1'
}

# 请求体
data = {
    "activityId": "1004435002421583872",
    "appid": "wxd92a2d29f8022f40"
}

# 你的多个 Qm-User-Token
qm_user_tokens = [
    'w4jV1nIrNMYkwNJm7aVGwmodxD_BM_EXiNB-M5H2m3Zxlo8adPdD4ZmgwTg4BEti',
]


def sign(token):
    # 签到的URL
    url = 'https://webapi2.qmai.cn/web/cmk-center/sign/takePartInSign'

    time.sleep(random.uniform(5, 10))
    headers = headers_template.copy()

    headers["Content-Length"] = '65'
    headers["Qm-User-Token"] = token

    response = requests.post(url, headers=headers, json=data)

    try:
        print(response.json()['message'])
    except ValueError:
        print("Response Content:", response.text)

def queryMobilePhone(token):
    url = 'https://webapi.qmai.cn/web/catering2-apiserver/crm/personal-info?appid=wxafec6f8422cb357b'

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()
    headers["Qm-User-Token"] = token
    headers["channelCode"] = ""
    headers["gdt-vid"] = ""
    headers["multi-store-id"] = ""
    headers["promotion-code"] = ""
    headers["scene"] = "1256"
    headers["store-id"] = "49006"
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


def queryReward(token):
    # 查询奖励的URL
    url = 'https://webapi2.qmai.cn/web/cmk-center/common/getCrmAvailablePoints?appid=wxafec6f8422cb357b'

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()

    headers["Qm-User-Token"] = token

    response = requests.get(url, headers=headers)

    try:
        response_json = response.json()
        points = response_json['data']
        print(f"当前积分为：{points}")
    except ValueError:
        print("Response Content:", response.text)


def querySignRecord(token):
    # 查询签到记录的URL
    url = 'https://webapi2.qmai.cn/web/cmk-center/sign/userSignRecordCalendar'
    payload = {
        "activityId": "1004435002421583872",
        "startDate": "2024-02-01",
        "endDate": "2024-09-30",
        "appid": "wxd92a2d29f8022f40"
    }

    time.sleep(random.uniform(2, 3))
    headers = headers_template.copy()
    headers["Content-Length"] = '113'
    headers["Qm-User-Token"] = token

    response = requests.post(url, headers=headers, json=payload)
    response_content = response.content

    # 先将字节数据解码为字符串
    decoded_content = response_content.decode('utf-8', errors='replace')

    # 然后解析 JSON 数据
    try:
        data = json.loads(decoded_content)
        calculate_consecutive_days(data['data']['signDateList'])
    except json.JSONDecodeError as e:
        print(f"JSON 解码错误: {e}")
        print(f"解码后的内容: {decoded_content}")


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


if __name__ == '__main__':
    for token in qm_user_tokens:
        # queryMobilePhone(token)
        sign(token)
        queryReward(token)
        querySignRecord(token)
        print("-" * 50)
        time.sleep(random.uniform(3, 6))