import re
import subprocess
import time

import requests

client_id = "h_EAL1JJV92j"
client_secret = "_UW_1DuQKE2eYtbJgfNMG_7H"


def updateEnv(config, id, name, remark, value):
    url = f"http://{config.serverIp}:{config.serverPort}/open/envs?t={time.time()}"
    headers = {
        'Authorization': config.authorization,
        'Content-Type': 'application/json'
    }
    data = {
        "id": id,
        "name": name,
        "remarks": remark,
        "value": value
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()['code']


def runCorn(config, id):
    url = f"http://{config.serverIp}:{config.serverPort}/open/crons/run?t={time.time()}"
    headers = {
        'Authorization': config.authorization,
        'Content-Type': 'application/json'
    }
    data = [int(id)]

    response = requests.put(url, headers=headers, json=data)
    return response.json()['code']


def getCurrentIp():
    response = requests.get('https://myip.ipip.net/json')
    data = response.json()
    return data['data']['ip']


def getIpv4Address():
    # 运行 ipconfig 命令并获取输出
    result = subprocess.run(['ipconfig'], capture_output=True, text=True)
    output = result.stdout

    # 定义正则表达式以匹配 WLAN 适配器的 IPv4 地址
    wlan_pattern = re.compile(r'无线局域网适配器 WLAN:.*?IPv4 地址 . . . . . . . . . . . . : (\d+\.\d+\.\d+\.\d+)',
                              re.S)

    # 查找匹配项
    match = wlan_pattern.search(output)
    if match:
        return match.group(1)
    return None


def updateAuthorization(serverIp):
    url = f'http://{serverIp}:5700/open/auth/token?client_id={client_id}&client_secret={client_secret}'
    response = requests.get(url)
    return response.json()['data']['token']
