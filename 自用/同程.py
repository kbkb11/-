import requests


def sign_in():
    # 签到的URL
    url = 'https://wx.17u.cn/car-inter-h5/quickcar/activity/saveMoneyCenterSignIn'

    # 请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'ASP.NET_SessionId=nicw04vkwn3d0dhd4gctqxzl; WxUser=openid=oOCyauM0-NwzUJIpCorG8xkhi2zM&token=82_Tf6FsVeRNrr4JcGeYq0eCbn_nZJXul6BTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcBew2mmMwGEfO0XrK8IA7UQkplSHYaLZVhpH9SFrG4&userid=u+KoOsn9O8PTEJTm8wsZ4w==&unionid=ohmdTt9MIwNRt6-dovW91VCA-ANo&sectoken=ZfOeS2YX9IStsHx-3-C4u0ZEYTjkTbMftsru7jYwOeLv-xCw9hOlDAIgBpIja96vLXFRVtDuLG9gCvnqQRyLRfNfxohL6OCy6_II7gm8db8W4tg9WLDGnNtYW43ZThR50kjIkolA_HXQPF64HreUi4JKJFGWWyJWO669vQwxXJ9gHNj8UB_NU0LLDr204zlYkKM0MblViJDwYUjggUz4Rw**4641; cookieOpenSource=openid=oOCyauM0-NwzUJIpCorG8xkhi2zM&token=82_Tf6FsVeRNrr4JcGeYq0eCbn_nZJXul6BTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcBew2mmMwGEfO0XrK8IA7UQkplSHYaLZVhpH9SFrG4; CooperateWxUser=CooperateUserId=oOCyauM0-NwzUJIpCorG8xkhi2zM&openid=oOCyauM0-NwzUJIpCorG8xkhi2zM&MemberId=u%2bKoOsn9O8PTEJTm8wsZ4w%3d%3d&token=82_Tf6FsVeRNrr4JcGeYq0eCbn_nZJXul6BTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcBew2mmMwGEfO0XrK8IA7UQkplSHYaLZVhpH9SFrG4&MemberSysId=33&Key=R8aSbpCvbq9FcKlFeAwdyLPxKMYPUNoGj%2bON67RtXUIpdfWLrkVVVg%3d%3d&unionid=ohmdTt9MIwNRt6-dovW91VCA-ANo; CooperateTcWxUser=CooperateUserId=oOCyauM0-NwzUJIpCorG8xkhi2zM&openid=oOCyauM0-NwzUJIpCorG8xkhi2zM&MemberId=u%2bKoOsn9O8PTEJTm8wsZ4w%3d%3d&token=82_Tf6FsVeRNrr4JcGeYq0eCbn_nZJXul6BTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcBew2mmMwGEfO0XrK8IA7UQkplSHYaLZVhpH9SFrG4&MemberSysId=33&Key=R8aSbpCvbq9FcKlFeAwdyLPxKMYPUNoGj%2bON67RtXUIpdfWLrkVVVg%3d%3d&unionid=ohmdTt9MIwNRt6-dovW91VCA-ANo; __tctmc=0.251296448; __tctmd=0.1; __tctmb=0.3065270436106494.1720871116625.1720871116625.1; __tccgd=0.0; route=1a7bad0e4c621c74235e80bd7c285dda; __tctmc=217272534.50544495; __tctmd=217272534.213614290; __tctma=217272534.1720871116301098.1720871116625.1720871116625.1720871116625.1; __tctmb=217272534.4392946650437504.1720871116625.1720871116625.1; __tctmu=217272534.0.0; __tctmz=217272534.1720871116625.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1720871116301098; __tctrack=0',
        'Host': 'wx.17u.cn',
        'Origin': 'https://wx.17u.cn',
        'Referer': 'https://wx.17u.cn/ycoperation/?platform=xcx-usecar&code=oOCyauM0-NwzUJIpCorG8xkhi2zM&token=82_Tf6FsVeRNrr4JcGeYq0eCbn_nZJXul6BTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcBew2mmMwGEfO0XrK8IA7UQkplSHYaLZVhpH9SFrG4',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185'
    }

    # 请求体
    data = {
        "platform": "xcx-usecar",
        "memberId": "",
        "unionId": "ohmdTt9MIwNRt6-dovW91VCA-ANo",
        "unionid": "ohmdTt9MIwNRt6-dovW91VCA-ANo",
        "openId": "oOCyauM0-NwzUJIpCorG8xkhi2zM",
        "openid": "oOCyauM0-NwzUJIpCorG8xkhi2zM",
        "headImg": None,
        "userName": None
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, json=data)

    # 打印响应内容
    print(response.text)

    # 判断签到是否成功
    if response.status_code == 200:
        result = response.json()
        if result['response']['header']['rspType'] == "SUCCESS":
            print('签到成功')
        else:
            print('签到失败:', result['response']['header']['rspDesc'])
    else:
        print('请求失败，状态码:', response.status_code)


if __name__ == '__main__':
    sign_in()
