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
    'Host': 'webapi2.qmai.cn',
    'Qm-From': 'wechat',
    'Qm-From-Type': 'catering',
    'Referer': 'https://servicewechat.com/wxafec6f8422cb357b/178/page-frame.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
    'xweb_xhr': '1'
}

# 请求体
data = {
    "activityId": "947079313798000641",
    "appid": "wxafec6f8422cb357b"
}

# 你的多个 Qm-User-Token
qm_user_tokens = [
    'kxvT2klmhlTvD8TYPmrlpZ-Mj44XPop23u9t9dEyQlZXIN19QOyVv_uciSazdv_h'
]


def sign():
    # 签到的URL
    url = 'https://webapi2.qmai.cn/web/cmk-center/sign/takePartInSign'

    for token in qm_user_tokens:
        time.sleep(random.uniform(2, 3))
        headers = headers_template.copy()

        headers["Content-Length"] = '64'
        headers["Qm-User-Token"] = token

        response = requests.post(url, headers=headers, json=data)

        try:
            print(response.json()['message'])
        except ValueError:
            print("Response Content:", response.text)

        queryReward(token)
        querySignRecord(token)


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
        "activityId": "947079313798000641",
        "startDate": "2024-01-01",
        "endDate": "2024-08-31",
        "appid": "wxafec6f8422cb357b"
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

    print(f"当前连续签到天数是：{current_streak}")
    print("-" * 50)
    return current_streak


if __name__ == '__main__':
    sign()
