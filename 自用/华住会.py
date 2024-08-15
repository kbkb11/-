import random
import time
import requests

tokens = [
    '8a78b1ee16de4ed4af77f803b632f5a3334470658'
]


class SignIn:
    def __init__(self, token):
        self.token = token
        self.session = requests.Session()
        self.base_url = "https://appgw.huazhu.com"
        self.origin = "https://cdn.huazhu.com"
        self.user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781"
                           "(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF "
                           "WindowsWechat(0x63090b19)XWEB/11159")
        self.headers = {
            "Origin": self.origin,
            "User-Agent": self.user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive"
        }

    def send_options_sign_in(self):
        url = f"{self.base_url}/game/sign_in"
        params = {"date": str(int(time.time()))}
        headers = {
            **self.headers,
            "Accept": "*/*",
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "client-platform",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Dest": "empty",
            "Referer": self.origin
        }
        response = self.session.options(url, headers=headers, params=params)
        return response

    def send_get_sign_in(self):
        url = f"{self.base_url}/game/sign_in"
        params = {"date": str(int(time.time()))}
        headers = {
            **self.headers,
            "Accept": "application/json, text/plain, */*",
            "Client-Platform": "WX-MP",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Dest": "empty",
            "Referer": self.origin,
            "Cookie": f"userToken={self.token}"
        }
        response = self.session.get(url, headers=headers, params=params)
        return response

    def send_get_sign_header(self):
        url = f"{self.base_url}/game/sign_header"
        headers = {
            **self.headers,
            "Accept": "application/json, text/plain, */*",
            "Client-Platform": "WX-MP",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Dest": "empty",
            "Referer": self.origin,
            "Cookie": f"userToken={self.token}"
        }
        response = self.session.get(url, headers=headers)
        return response


if __name__ == "__main__":
    for token in tokens:
        # 使用示例
        sign_in = SignIn(token)
        # options_response = sign_in.send_options_sign_in()
        # print("OPTIONS Response:", options_response.status_code)

        sign_in_response = sign_in.send_get_sign_in()
        print("GET sign_in Response:", sign_in_response.status_code, sign_in_response.json())

        sign_header_response = sign_in.send_get_sign_header()
        print("GET sign_header Response:", sign_header_response.status_code, sign_header_response.json())

        time.sleep(random.uniform(5, 10))
