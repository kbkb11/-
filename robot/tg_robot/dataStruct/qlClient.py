import json
import re
import time

import requests

from robot.tg_robot.spyConfig.sqyConfig import cache_envs_data, cache_tasks_data
from robot.tg_robot.utils.qlOpenApi import updateAuthorization, getIpv4Address, updateEnv
from robot.tg_robot.utils.readAndWrite import load_env_by_name, update_env_by_name


class QLClient:
    def __init__(self, serverPort):
        self.serverIp = getIpv4Address()
        self.serverPort = serverPort
        self.authorization = "Bearer " + updateAuthorization(self.serverIp)
        print(f"初始化完成，IP地址为：{self.serverIp}, 端口号为：{self.serverPort}, 授权码为：{self.authorization}")

    def init_tasks(self):
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        data = {
            "t": time.time()
        }

        response = requests.get(f"http://{self.serverIp}:{self.serverPort}/open/crons", headers=headers, json=data)
        tasks = response.json().get('data', {}).get('data', [])

        # 存储任务数据到本地 JSON 文件
        tasks_to_save = []
        for item in tasks:
            if isinstance(item, dict):  # 确保 item 是字典
                task_data = {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "command": item.get("command"),
                    "schedule": item.get("schedule"),
                    'status': item.get("status")
                }
                tasks_to_save.append(task_data)
            else:
                print("Unexpected item format:", item)
                return
        # 写入到 JSON 文件
        output_file = cache_tasks_data
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_to_save, f, ensure_ascii=False, indent=4)
        print("任务数据初始化完成")

    def init_envs(self):
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        data = {
            "t": time.time()
        }

        response = requests.get(f"http://{self.serverIp}:{self.serverPort}/open/envs", headers=headers, json=data)
        envs = response.json()['data']
        # 存储环境变量数据到本地 JSON 文件
        envs_to_save = []
        for item in envs:
            if isinstance(item, dict):
                env_data = {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "remarks": item.get("remarks"),
                    "value": item.get("value"),
                }
                envs_to_save.append(env_data)
            else:
                print("Unexpected item format:", item)
                return
        # 写入到 JSON 文件
        output_file = cache_envs_data
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(envs_to_save, f, ensure_ascii=False, indent=4)
        print("环境变量数据初始化完成")

    def updateJDSignIp(self):
        try:
            # 先更新当前IP
            self.serverIp = getIpv4Address()

            # 获取京东签名JSON缓存
            jdSign = load_env_by_name('JD_SIGN_API')
            # 检查是否存在
            if jdSign is None:
                print('未找到JD_SIGN_API环境变量')
                return

            url = jdSign.get('value')

            # 匹配URL中的IP地址
            match = re.search(r"http[s]?://((\d+\.){3}\d+):32772/sign", url)
            signIp = match
            if not match:
                print('未能在URL中找到有效的IP地址,签名服务出错，需要更新')
            else:
                signIp = match.group(1)

            # 如果IP不一致则更新
            if signIp is None or signIp != self.serverIp:
                print('开始更新JD_SIGN_API环境变量')
                newJDSign = f"http://{self.serverIp}:{32772}/sign"

                jdSign['value'] = newJDSign
                res = updateEnv(self, jdSign['id'], jdSign['name'], "自建京东签名", jdSign['value'])
                if res == 200:
                    print('青龙环境变量JD_SIGN_API更新成功')
                else:
                    print(f'更新失败, {res}')

                print("开始更新本地JSON缓存")
                update_env_by_name(jdSign['name'], jdSign)
            else:
                print('京东签名未改变，无需更新')
        except Exception as e:
            print(f"发生错误: {e}")
