import os
import time
import requests
import json

from datetime import datetime

# 客户端 ID 和客户端密钥
client_id = "OM7ZQDuvtn_7"
client_secret = "mF0TdF5GcYqbnB-0xbhQOCAf"
serverIp = "47.121.117.196"

# 获取授权令牌
authorization = "Bearer " + requests.get(
    f'http://{serverIp}:5700/open/auth/token?client_id={client_id}&client_secret={client_secret}').json()['data'][
    'token']
print(f"Authorization: {authorization}")


def getShopSignDate(fileName, scriptPath):
    currentTime = time.time()

    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }
    data = {
        "file": fileName,
        "path": scriptPath,
        "t": currentTime
    }

    response = requests.get(
        f"http://{serverIp}:5700/open/scripts/detail?file={fileName}&path={scriptPath}&t={currentTime}",
        headers=headers,
        json=data)

    return response.json()['data']


def calculate_days_until_next_reward(start_time, rules):
    # 当前时间
    now = datetime.now()

    # 将 startTime 转换为 datetime 对象
    start_date = datetime.utcfromtimestamp(start_time / 1000)

    # 计算当前时间与开始时间的天数差
    days_elapsed = (now - start_date).days

    # 遍历奖励规则
    for rule in rules:
        if rule['havePrize']:
            next_reward_days = rule['days'] - days_elapsed
            if next_reward_days > 0:
                return next_reward_days, rule['prize']
    return None, None


# 获取 JSON 数据
data = getShopSignDate("rs_dpqd_tokens.json", "shufflewzc_faker3_main")

# 将 JSON 字符串解析为字典对象
if isinstance(data, str):
    data = json.loads(data)

# 存储有奖励阶段的活动
filtered_data = {}
new_index = 1

# 遍历 JSON 数据中的每一个条目
for key, activity in data.items():
    start_time = activity['startTime']
    rules = activity['rules']

    # 计算还有多少天可以领取下一阶段的奖励
    days_until_next_reward, next_reward = calculate_days_until_next_reward(start_time, rules)

    if days_until_next_reward is not None:
        # 打印店铺信息、奖励内容和剩余天数
        print(f"活动ID {key} - 距离下一阶段的奖励还有 {days_until_next_reward} 天，奖励内容：{next_reward}")

        # 复制原始活动数据
        new_activity = activity.copy()

        # 更新索引
        new_activity['index'] = new_index
        new_index += 1

        # 存储到新字典中
        filtered_data[key] = new_activity

# 输出最终的 JSON 格式数据
output_json = json.dumps(filtered_data, indent=4, ensure_ascii=False)
print(output_json)

# 将数据写入文件
output_file_path = os.path.join("data", "newShopTokens.json")
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(output_json)