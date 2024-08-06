# cron: 10 */2 * * *  # 定时任务，每隔2小时的第10分钟运行一次
# new Env('更新IP代理白名单');  # 设置脚本的环境变量描述

import requests
import os

# 携趣的UID和UKEY，用于身份验证
XIEQU_UID = '144288'
XIEQU_UKEY = '7383ADCDFB3F82703BD476A6DF005EBD'

# 青龙环境变量（若上面不填写，则读取青龙环境变量）
XIEQU_UID = XIEQU_UID if XIEQU_UID else os.getenv("XIEQU_UID")
XIEQU_UKEY = XIEQU_UKEY if XIEQU_UKEY else os.getenv("XIEQU_UKEY")


def get_current_ip():
    # 获取当前设备的外网IP地址
    response = requests.get('https://myip.ipip.net/json')
    data = response.json()
    return data['data']['ip']


def update_xiequ_white_list(ip, XIEQU_UID, XIEQU_UKEY):
    # 更新携趣的IP白名单
    if XIEQU_UID and XIEQU_UKEY:
        # 获取当前白名单列表
        url = f'http://op.xiequ.cn/IpWhiteList.aspx?uid={XIEQU_UID}&ukey={XIEQU_UKEY}&act=get'
        response = requests.get(url)
        data = response.text
        arr = data.split(',')

        if ip not in arr:
            # 删除所有白名单IP
            requests.get(f'http://op.xiequ.cn/IpWhiteList.aspx?uid={XIEQU_UID}&ukey={XIEQU_UKEY}&act=del&ip={arr[0]}')
            # 添加新的IP到白名单
            response = requests.get(
                f'http://op.xiequ.cn/IpWhiteList.aspx?uid={XIEQU_UID}&ukey={XIEQU_UKEY}&act=add&ip={ip}')
            return '更新携趣白名单成功' if response.status_code == 200 else '更新携趣白名单出错'
        else:
            return '携趣白名单ip未变化'


def main():
    ip = get_current_ip()
    print('当前ip地址：', ip)
    print('更新携趣白名单结果：', update_xiequ_white_list(ip, XIEQU_UID, XIEQU_UKEY))

    # 手动更新指定的服务器IP地址
    ip = "47.121.117.196"
    print('服务器ip地址：', ip)
    print('更新携趣白名单结果：', update_xiequ_white_list(ip, XIEQU_UID, XIEQU_UKEY))


if __name__ == "__main__":
    main()
