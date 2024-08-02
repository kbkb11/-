import json
import re
import time

import requests


def parseMessage(ql_env, message):
    envData = ql_env.list()['data']

    # 使用正则表达式解析URL
    url_pattern = r'http[s]?://[^\s"]+'
    match = re.search(url_pattern, message)
    url = match.group()

    keywords = ['interactsaas', '']

    if keywords[0] in message:
        # 10024是加购有礼，10069是关注店铺有礼
        activityTypes = ['10024', '10069']
        activityTypes_pattern = r'activityType=(\d+)'
        activityTypes_match = re.search(activityTypes_pattern, message)
        activityType = activityTypes_match.group(1)

        print(activityType)
        if activityType == activityTypes[0]:
            print('开始更新加购有礼变量')
            temp = list(ql_env.search('jd_lzkj_cart_url'))
            res = ql_env.update(value=url, name='jd_lzkj_cart_url', id=temp[0][0], remarks='加购有礼链接')
            if res['code'] == 200:
                print('更新成功,开始进行执行操作')

            else:
                print(f'更新失败,{res}')
