import time

import requests
from datetime import datetime


class HttpClient:
    def __init__(self):
        self.session = requests.Session()

    def send_binary_data(self):
        url = "https://unitelogreport.reader.qq.com/ywslogcpt/QD/qdclientlog/access"
        headers = {
            "Host": "unitelogreport.reader.qq.com",
            "Accept": "*/*",
            "Content-Type": "application/octet-stream",
            "Connection": "keep-alive",
            "Cookie": (
                "QDH=XVe+f2Nacn+iMm+gDhsAbPHDmkWS6gIZQUlQSQolcHd/pKWiXEzvj0ZLwBhnKBdUxvxNDHOzb1IjZKxVaO9iyAjAvz4rG+CSAGbdcx6zXTnJBH/77FPW/uqIxKT427CFBLwplsN1UHshhI7dE+J8Lb01iwxg3EcWql5srITQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcM4AJMvSgPHGdy4Oma9TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcZtDB2yE0eMhOF/xcu1XxR5cp4GgKj+fodZPlVnNpHeJUW244rHvVz1NmQEIu52uxTz4q3y4wYFNYv4Q=;"
                "appId=12; areaId=40; bar=88; cmfuToken=N((0dqqkW3EzO4C_PlCn_IRmBxJZUSisbC2CHsK7wrTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcSsq2mnCERDQoB6ntRwO_2XyvpxQ6ZlqSz8mY7e7V813q_RMqwPUaSqAuvfII2_vGp41LxuE9BEDeWETI48SsC97vMcAPL2bcTD-er0K4lUV5HZP1Mzw8YCcqc7jkyXk-SfccYlwrca9bk1Aj_1FednoQ2AGFuvdvZWYHqr0JSWmNegcMjVxBS9eabFuJn4ZyblvIyZqXCEBdU2VhfQmHx_F0; "
                "mode=normal; qid=13d5e1a5e8508f9eeb3f65b6000010c17805; ywguid=1019950982; ywkey=ywsiT4HyL7KL; QDHeader=KG51bGwpfChudWxsKXw8Mjh8MTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcob25lLyhudWxsKXwwfChudWxsKxwobnVsbCl8MzE3NDQxMTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc8fHwobnVsbCl8KG51bGwpfDA="),
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Content-Length": "2156",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "QDReaderAppStore/1147 CFNetwork/1408.0.4 Darwin/22.5.0"
        }
        data = b'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'
        response = self.session.post(url, headers=headers, data=data)
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)

    def send_params_request(self):
        url = "https://path.book.qq.com/qreport"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        params = {
            "userid": "317441127",
            "guid": "1019950982",
            "version": "634",
            "path": "qdactivity",
            "fromstr": "qdapp",
            "logtime": current_time,
            "platform": "2",
            "uuid": "1721015011064869",
            "qimei": "13d5e1a5e8508f9eeb3f65b6000010c17805",
            "env": "ol",
            "activityid": "qd_fulizhongxin_new",
            "p2": "click",
            "action": "click",
            "p1": "15",
            "p3": "3",
            "p5": "T2022103101",
            "p6": "0",
            "p7": "qiandao",
            "p4": "8054520584600960",
            "p8": "1"
        }
        headers = {
            "Host": "path.book.qq.com",
            "Sec-Fetch-Site": "cross-site",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "no-cors",
            "Cache-Control": "max-age=0",
            "Origin": "https://h5.if.qidian.com",
            "Content-Length": "0",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/QDReaderiOS/5.9.362/634/QDReaderAppstore/QDNightStyle_2/QDShowNativeLoading",
            "Referer": "https://h5.if.qidian.com/",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Sec-Fetch-Dest": "empty"
        }
        response = self.session.post(url, params=params, headers=headers)
        print("Status Code:", response.status_code)
        print("Response Content:", response.content.decode('utf-8'))

    def send_json_data(self):
        url = "https://otheve.beacon.qq.com/analytics/upload"
        headers = {
            "Host": "otheve.beacon.qq.com",
            "Accept": "text/plain",
            "Sec-Fetch-Site": "cross-site",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "cors",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://wallpaper-1258344696.file.myqcloud.com",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Referer": "https://wallpaper-1258344696.file.myqcloud.com/",
            "Content-Length": "333",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty"
        }
        data = {
            "deviceId": "18d0a693ccf64c000",
            "appkey": "JS05KY1G393HQI",
            "versionCode": "22.0726.1727",
            "initTime": 1723357238176,
            "channelID": "",
            "sdkVersion": "js_v1.1.3",
            "pixel": "414*896*2",
            "language": "zh-CN",
            "msgs": [
                {
                    "type": 2,
                    "data": {
                        "id": "18d0a693ccf64c000172335784554800",
                        "start": 1723357845549,
                        "status": 1,
                        "duration": 53613,
                        "pages": [],
                        "events": []
                    }
                }
            ]
        }
        response = self.session.post(url, headers=headers, json=data)
        print("Status Code:", response.status_code)
        print("Response Content:", response.content.decode('utf-8'))


# 示例用法
if __name__ == "__main__":
    client = HttpClient()
    client.send_binary_data()
    # client.send_params_request()
    # client.send_json_data()

    print(time.time())
