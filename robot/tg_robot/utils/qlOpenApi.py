import json
import re
import subprocess
import time

import requests

from robot.tg_robot.spyConfig.sqyConfig import cache_tasks_data, client_id, client_secret
from robot.tg_robot.utils.readAndWrite import load_json


def updateEnv(config, id, name, remark, value):
    """
    更新环境变量的函数。

    参数:
        spyConfig: 配置对象，包含服务器 IP 和端口信息
        id: 环境变量的 ID
        name: 环境变量的名称
        remark: 环境变量的备注
        value: 环境变量的值

    返回:
        响应的状态码
    """
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
    """
    运行定时任务的函数。

    参数:
        spyConfig: 配置对象，包含服务器 IP 和端口信息
        id: 定时任务的 ID

    返回:
        响应的状态码
    """
    url = f"http://{config.serverIp}:{config.serverPort}/open/crons/run?t={time.time()}"
    headers = {
        'Authorization': config.authorization,
        'Content-Type': 'application/json'
    }
    data = [int(id)]

    response = requests.put(url, headers=headers, json=data)
    return response.json()['code']


def getCurrentIp():
    """
    获取当前公网 IP 地址的函数。

    返回:
        当前公网 IP 地址
    """
    response = requests.get('https://myip.ipip.net/json')
    data = response.json()
    return data['data']['ip']


def getIpv4Address():
    """
    获取本地 WLAN 适配器的 IPv4 地址的函数。

    返回:
        WLAN 适配器的 IPv4 地址，如果没有找到则返回 None
    """
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
    """
    更新授权令牌的函数。

    参数:
        serverIp: 服务器的 IP 地址

    返回:
        新的授权令牌
    """
    url = f'http://{serverIp}:5700/open/auth/token?client_id={client_id}&client_secret={client_secret}'
    response = requests.get(url)
    return response.json()['data']['token']


def createEnv(config, name, remark, value):
    """
    创建环境变量的函数。

    参数:
        spyConfig: 配置对象，包含服务器 IP 和端口信息
        name: 环境变量的名称
        remark: 环境变量的备注
        value: 环境变量的值

    返回:
        响应的状态码
    """
    url = f"http://{config.serverIp}:{config.serverPort}/open/envs?t={time.time()}"
    headers = {
        'Authorization': config.authorization,
        'Content-Type': 'application/json'
    }
    data = [
        {
            "value": value,
            "name": name,
            "remarks": remark
        }
    ]
    response = requests.post(url, headers=headers, json=data)
    return response.json()['code']


def calculateRunningTask(config):
    """
    计算正在运行的任务数量的函数。

    参数:
        spyConfig: 配置对象，包含服务器 IP 和端口信息

    返回:
        正在运行的任务数量
    """
    config.init_tasks()
    tasks = load_json(cache_tasks_data)
    sum = 0
    for task in tasks:
        if task['status'] == 0:
            sum += 1

    return sum