import random
import time

import requests

# 请求头
headers_template = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'suid=oTlVde8RC0H9ore66iWt4Q==; suid=oTlVde8RC0H9ore66iWt4Q==',
    'Host': 'm.ctrip.com',
    'Origin': 'https://m.ctrip.com',
    'Referer': 'https://m.ctrip.com/activitysetupapp/mkt/index/membersignin2021?isHideNavBar=YES&pushcode=miniprogram&fromminiapp=weixin&allianceid=1314167&sid=4258862&ouid=mini1053&sourceid=55555549&_cwxobj=%7B%22cid%22%3A%2252271106496475974363%22%2C%22appid%22%3A%22wx0e6ed4f51db9d078%22%2C%22mpopenid%22%3A%22ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19%22%2C%22mpunionid%22%3A%22oHkqHt2jVThPy1BresSSBKQHh-WI%22%2C%22allianceid%22%3A%221314167%22%2C%22sid%22%3A%224258862%22%2C%22ouid%22%3A%22mini1053%22%2C%22sourceid%22%3A%2255555549%22%2C%22exmktID%22%3A%22%7B%5C%22openid%5C%22%3A%5C%22ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19%5C%22%2C%5C%22unionid%5C%22%3A%5C%22oHkqHt2jVThPy1BresSSBKQHh-WI%5C%22%2C%5C%22channelUpdateTime%5C%22%3A%5C%221721140817947%5C%22%2C%5C%22serverFrom%5C%22%3A%5C%22WAP%2FWECHATAPP%5C%22%2C%5C%22innersid%5C%22%3A%5C%22260%5C%22%2C%5C%22innerouid%5C%22%3A%5C%22%5C%22%2C%5C%22pushcode%5C%22%3A%5C%22%5C%22%2C%5C%22txCpsId%5C%22%3A%5C%22%5C%22%2C%5C%22search_keywords%5C%22%3A%5C%22%5C%22%2C%5C%22search_type%5C%22%3A%5C%22%5C%22%2C%5C%22amsPid%5C%22%3A%5C%22%5C%22%2C%5C%22gdt_vid%5C%22%3A%5C%22%5C%22%2C%5C%22xhs_click_id%5C%22%3A%5C%22%5C%22%7D%22%2C%22scene%22%3A1256%2C%22personalRecommendSwitch%22%3Atrue%2C%22localRecommendSwitch%22%3Atrue%2C%22marketSwitch%22%3Atrue%2C%22pLen%22%3A2%7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
    "content-type": "application/json",
    "cookieOrigin": "https://m.ctrip.com",
}

cookies = [
    '''cticket=BFEF38101F4BA46C7EB310FBCC7383E6B67EE299CC49BA4615031F26A1AE3651; login_type=0; login_uid=F1B9E5CD8A9C81AB8D5D50A05E9164B3; DUID=u=F1B9E5CD8A9C81AB8D5D50A05E9164B3&v=0; IsNonUser=F; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; GUID=52271106496475974363; nfes_isSupportWebP=1; nfes_isSupportWebP=1; UBT_VID=1717679887066.2f53XdBbzcTA; _RF1=106.5.206.132; _RSG=d5a9_K4GV77fylVagvH2ZA; _RDG=281e9ff590cbe32b4238bea72dbd99310e; _RGUID=71df4045-3f26-4167-a8c2-479aa47eff29; set_parentAllianceID=; environmentFrom=; envP=; atype=; _ubtstatus=%7B%22vid%22%3A%221717679887066.2f53XdBbzcTA%22%2C%22sid%22%3A6%2C%22pvid%22%3A2%2C%22pid%22%3A%2210650004935%22%7D; union_ticket=eyJpc0xvZ2luIjp0cnVlLCJpc0FjdGl2YXRlIjpmYWxzZX0%3D; MKT_Pagesource=H5; MKT_Applet=APPID=wx0e6ed4f51db9d078&OPENID=ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19&INNERSID=260&INNEROUID=task&PUSHCODE=&createtime=1721391504; _pd=%7B%22_o%22%3A8%2C%22s%22%3A14%2C%22_s%22%3A1%7D; MKT_Inner=INNERSID=task2104&INNEROUID=task&createtime=1721392038; _bfa=1.1717679887066.2f53XdBbzcTA.1.1721392037650.1721441184565.7.1.10650004935; Union=OUID=mini1053&AllianceID=1314167&SID=4258862&SourceID=55555549&createtime=1721441185&Expires=1722045985365; MKT_code=PUSHCODE=miniprogram&createtime=1721441185; MKT_OrderClick=ASID=13141674258862&AID=1314167&CSID=4258862&OUID=mini1053&CT=1721441185366&CURL=https%3A%2F%2Fm.ctrip.com%2Factivitysetupapp%2Fmkt%2Findex%2Fmembersignin2021%3FisHideNavBar%3DYES%26pushcode%3Dminiprogram%26fromminiapp%3Dweixin%26allianceid%3D1314167%26sid%3D4258862%26ouid%3Dmini1053%26sourceid%3D55555549%26_cwxobj%3D%257B%2522cid%2522%253A%252252271106496475974363%2522%252C%2522appid%2522%253A%2522wx0e6ed4f51db9d078%2522%252C%2522mpopenid%2522%253A%2522ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19%2522%252C%2522mpunionid%2522%253A%2522oHkqHt2jVThPy1BresSSBKQHh-WI%2522%252C%2522allianceid%2522%253A%25221314167%2522%252C%2522sid%2522%253A%25224258862%2522%252C%2522ouid%2522%253A%2522mini1053%2522%252C%2522sourceid%2522%253A%252255555549%2522%252C%2522exmktID%2522%253A%2522%257B%255C%2522openid%255C%2522%253A%255C%2522ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19%255C%2522%252C%255C%2522unionid%255C%2522%253A%255C%2522oHkqHt2jVThPy1BresSSBKQHh-WI%255C%2522%252C%255C%2522channelUpdateTime%255C%2522%253A%255C%25221721140817947%255C%2522%252C%255C%2522serverFrom%255C%2522%253A%255C%2522WAP%252FWECHATAPP%255C%2522%252C%255C%2522innersid%255C%2522%253A%255C%2522260%255C%2522%252C%255C%2522innerouid%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522pushcode%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522txCpsId%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522search_keywords%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522search_type%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522amsPid%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522gdt_vid%255C%2522%253A%255C%2522%255C%2522%252C%255C%2522xhs_click_id%255C%2522%253A%255C%2522%255C%2522%257D%2522%252C%2522scene%2522%253A1256%252C%2522personalRecommendSwitch%2522%253Atrue%252C%2522localRecommendSwitch%2522%253Atrue%252C%2522marketSwitch%2522%253Atrue%252C%2522pLen%2522%253A2%257D&VAL={"pc_vid":"1717679887066.2f53XdBbzcTA"}'''
]


def sign():
    # 签到的URL
    url = 'https://m.ctrip.com/restapi/soa2/22769/signToday?_fxpcqlniredt=52271106496475974363&x-traceID=52271106496475974363-1721441195359-8226602'

    # 请求体
    data = {
        "platform": "miniProgram",
        "openId": "ef8c44e3-c5ea-4ab0-a3b9-461fc9818b19",
        "rmsToken": "",
        "head": {
            "cid": "52271106496475974363", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888", "syscode": "09",
                 "auth": "", "xsid": "", "extension": []
        }
    }

    for cookie in cookies:
        time.sleep(random.uniform(2, 3))
        headers = headers_template.copy()

        headers["Content-Length"] = '351'
        headers["Cookie"] = cookie

        response = requests.post(url, headers=headers, json=data)

        try:
            print(response.json()['message'])
        except ValueError:
            print("Response Content:", response.text)


if __name__ == '__main__':
    sign()
