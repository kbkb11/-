import json
from datetime import datetime

# 原始数据
data = {
    "D65F939F8004AC423F2126D460207525": {
        "index": 17,
        "venderId": 16803032,
        "shopName": "文和大药房旗舰店",
        "activityId": 12673938,
        "startTime": 1722614400000,
        "endTime": 1725119999000,
        "isValid": True,
        "rules": [
            {
                "days": 0,
                "prize": [
                    "1京豆（共10000份）"
                ],
                "havePrize": True
            },
            {
                "days": 7,
                "prize": [
                    "10京豆（共1000份）"
                ],
                "havePrize": True
            }
        ],
        "minLevel": 0,
        "maxLevel": 7
    }
}


# 转换函数
def convert_data(data):
    new_data = {}
    for key, value in data.items():
        start_time = datetime.fromtimestamp(value['startTime'] / 1000).strftime('%Y/%m/%d %H:%M:%S')
        end_time = datetime.fromtimestamp(value['endTime'] / 1000).strftime('%Y/%m/%d %H:%M:%S')

        prize_list = []
        for rule in value['rules']:
            days = rule['days']
            if rule['havePrize']:
                prize = rule['prize'][0].split('（')[0]  # 获取豆数或奖品名称
                quantity = rule['prize'][0].split('（')[1].split('份')[0]  # 获取份数
                prize_list.append(f"{days}天{prize}{quantity}份")

        prize_str = '|'.join(prize_list)

        new_data[key] = {
            "index": value['index'],
            "shopName": value['shopName'],
            "venderId": value['venderId'],
            "activityId": value['activityId'],
            "startTime": start_time,
            "endTime": end_time,
            "prize": prize_str
        }

    return new_data


# 转换数据
converted_data = convert_data(data)

# 打印转换后的数据
print(json.dumps(converted_data, indent=2, ensure_ascii=False))
