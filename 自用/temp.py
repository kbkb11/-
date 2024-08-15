import hashlib
import urllib

import requests


def getList():
    # 请求的 URL
    url = "https://xmt.taizhou.com.cn/prod-api/user-read/list/20240815"

    # 请求头
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36;xsb_wangchao;xsb_wangchao;6.0.2;native_app;6.10.0",
        "Accept": "*/*",
        "X-Requested-With": "com.shangc.tiennews.taizhou",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://xmt.taizhou.com.cn/readingLuck-v1/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "tfstk=fTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcCKpvhF_flNwaH0B9hOwfIyDuHwIU5-bIWYERHG_jCFbhFLpRUNabIynSci6ClO4K7Y6fDiztWNXQhYdfvVLtepkWHKBHROY3XeLIdxfG6Yc9JeuF6RDlfxvvmU9c3dci6eLvz3Ze-fvHGR6fhtM4lK-DVCOShEuAhiZXGC7jhxBvm39WUx7jhKKbce9dBO_5YjT_oQ_DORTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc-bQovQBlzXTxFUh7ykXEJei79aa-Eacj5csOPeNmUJMjzTWBDPNtpvDUFrtBV1xkDpYpNLz7k-nzLJaL131McQyUdrtBV1xk4JyQRpt5snO5..; JSESSIONID=AFE0FFAE9E3992C49A680E39B016C850"
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers)

    # 输出响应内容
    print(response)
    print(response.json())
    print(response.text)


# p0为url encodePath，p1为sessionId, p2为requestId（uuid）, p3为timestamp
def signature(p0, p1, p2, p3):
    api_version = "6.0.2"
    encoded_url = urllib.parse.quote(p0, safe='')

    # 去除前缀
    if api_version and encoded_url.startswith(api_version):
        encoded_url = encoded_url[len(api_version):]

    # 创建参数列表
    obj_array = [encoded_url, p1, p2, p3, "FR*r!isE5W", "64"]

    # 拼接字符串
    combined_string = "&&".join(obj_array)

    print(combined_string)

    # 计算 SHA-256 哈希
    sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()

    return sha256_hash


# getList()


print(signature("https://vapp.taizhou.com.cn/api/article/detail?id=3470058",
                "66bc6fbfbf15a47d51c0e366",
                "028c2433-e1a3-4403-9f86-32a799e94804",
                "1723633749896"))
