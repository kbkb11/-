from datetime import datetime
import time

import requests
from requests.exceptions import RequestException


class ApiClient:
    def __init__(self):
        # 初始化一个 requests Session 实例
        self.session = requests.Session()

    def get_formatted_date(self):
        # 获取当前日期
        now = datetime.now()
        # 格式化日期为 'YYYYMMDD'
        formatted_date = now.strftime("%Y%m%d")
        return formatted_date

    def _get_headers(self, additional_headers=None):
        """
        生成请求头
        :param additional_headers: 额外的请求头
        :return: 请求头字典
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36;xsb_wangchao;xsb_wangchao;6.0.2;native_app;6.10.0",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def get_user_sign(self, signature, tenant_id, session_id):
        """
        获取用户签名
        :param timestamp: 时间戳
        :param signature: 签名
        :param tenant_id: 租户ID
        :param session_id: 会话ID
        :return: 响应的 JSON 数据
        """
        url = "https://vapp.taizhou.com.cn/api/user_mumber/sign"
        headers = self._get_headers({
            "X-TIMESTAMP": time.time(),
            "X-SIGNATURE": signature,
            "X-TENANT-ID": tenant_id,
            "X-SESSION-ID": session_id,
            "Referer": "https://vapp.taizhou.com.cn/webFunction/userCenter?tenantId=64&gaze_control=023",
            "Cookie": "acw_tc=1a0c380d17236334624568513e0032157d6f4b32fc35a92763b77e1846c984"
        })
        try:
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"请求失败: {e}")
            return None

    def get_read_list(self):
        """
        获取阅读列表
        :param date: 日期（例如 '20240814'）
        :return: 响应的 JSON 数据
        """
        url = f"https://xmt.taizhou.com.cn/prod-api/user-read/list/{self.get_formatted_date()}"
        headers = self._get_headers({
            "Referer": "https://xmt.taizhou.com.cn/readingLuck-v1/",
            "Cookie": "JSESSIONID=FB8045FBA86903EA802226C60CD66904"
        })
        try:
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            if data and data.get('code') == 200:
                articles = data.get('data', {}).get('articleIsReadList', [])
                return articles
            else:
                print(f"响应码错误: {data.get('code')}")
                return None
        except RequestException as e:
            print(f"请求失败: {e}")
            return None

    def get_article_detail(self, article_id, session_id, request_id, signature, account_id):
        """
        获取文章详细信息
        :param article_id: 文章ID
        :param session_id: 会话ID
        :param request_id: 请求ID
        :param timestamp: 时间戳
        :param signature: 签名
        :param tenant_id: 租户ID
        :param account_id: 账户ID
        :return: 响应的 JSON 数据
        """
        url = f"https://vapp.taizhou.com.cn/api/article/detail?id={article_id}"
        headers = self._get_headers({
            "X-SESSION-ID": session_id,
            "X-REQUEST-ID": request_id,
            "X-TIMESTAMP": str(int(time.time()*1000)),
            "X-SIGNATURE": signature,
            "X-TENANT-ID": "64",
            "X-ACCOUNT-ID": account_id,
            "Cache-Control": "no-cache"
        })
        try:
            response = self.session.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"请求失败: {e}")
            return None

    def post_award_record(self):
        """
        提交抽奖记录更新请求
        :param data: 要提交的表单数据
        :return: 响应的 JSON 数据
        """
        url = "https://srv-app.taizhou.com.cn/tzrb/userAwardRecordUpgrade/saveUpdate"
        headers = self._get_headers({
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://srv-app.taizhou.com.cn",
            "Referer": "https://srv-app.taizhou.com.cn/luckdraw-ra-1/",
            "Cookie": "JSESSIONID=a9d8a672-18fc-48ce-ad2a-c72d380df0f6; tfstk=fi4KYqva0UspT7juRWsir5jF_EPRiyFU_JPXrYDHVReTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc8u3r0jeFPF8eDGIR9eTN824xe0QEUM8d-GlTe0Iea3USkYoK9u8N-0RntbcoWPE846cnQDwkSgjZYOBED9s56h5FQbcoWPQ9CnwTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcw711h-Gp9IV0g61bcW9VOSEQHMyuiOetAWmQ8yzPh1HxNK3flUWbot6cM9P54t9DHbtyPs5KcbDPn0A6sICkwUu0ieGB07ASUTDJA2P4NnF-H3Fgy8orUCzKcZWH1O63-rAfjTs3tiggdxEfHcsn-y4DCm6xfO63-rAfltn1fk43odi"
        })
        data = "activityId=67&sessionId=undefined&sig=undefined&token=undefined"
        try:
            response = self.session.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"请求失败: {e}")
            return None


if __name__ == "__main__":
    client = ApiClient()

    # 替换以下参数为实际值
    user_sign_response = client.get_user_sign("3e11a8b925c5bbde79c50b075066bb11b32f7b99e4c1210d72753f863a9bd93b", "64",
                                              "66bc6fbfbf15a47d51c0e366")
    print("用户签名响应:", user_sign_response)

    # articles = client.get_read_list()
    # print("阅读列表响应:", articles)

    # article_detail_response = client.get_article_detail("3470058", "66bc6fbfbf15a47d51c0e366",
    #                                                     "028c2433-e1a3-4403-9f86-32a799e94804",
    #                                                     "89898f90a594d0e123e596f140ab4298e8e76c6645e55571b36a585218550b34",
    #                                                     "666521f5bf15a47d5164f075")
    # print("文章详情响应:", article_detail_response)

    # post_award_record_response = client.post_award_record()
    # print("抽奖记录响应:", post_award_record_response)
