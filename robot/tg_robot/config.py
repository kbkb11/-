import json
import time

import requests

from robot.tg_robot.qlOpenApi import updateAuthorization, getIpv4Address


class ServerConfig:
    def __init__(self, serverPort):
        self.serverIp = getIpv4Address()
        self.serverPort = serverPort
        self.authorization = updateAuthorization(self.serverIp)

    def init(self):
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
                    "schedule": item.get("schedule")
                }
                tasks_to_save.append(task_data)
            else:
                print("Unexpected item format:", item)
                return
        # 写入到 JSON 文件
        output_file = "tasks_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_to_save, f, ensure_ascii=False, indent=4)

        # 获取环境变量数据
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
        output_file = "envs_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(envs_to_save, f, ensure_ascii=False, indent=4)

        print("初始化json完成")
