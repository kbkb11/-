def merge_and_adjust_index(data1, data2):
    # 合并两个数据字典
    merged_data = {**data1, **data2}

    # 获取所有键，并按字典顺序排序
    sorted_keys = sorted(merged_data.keys())

    # 为每个项分配新的 index 值
    for new_index, key in enumerate(sorted_keys, start=1):
        merged_data[key]['index'] = new_index

    return merged_data

# 示例数据
data1 = {
    "8994B4032B1628DC66AAAAD25855908A": {
        "index": 1,
        "venderId": 46722,
        "shopName": "古越龙山旗舰店",
        "activityId": 12669776,
        "startTime": 1722528000000,
        "endTime": 1725119999000,
        "isValid": False,
        "rules": [
            {
                "days": 1,
                "prize": [
                    "10京豆（共1000份，已发完）",
                    "优惠券（共50000份）"
                ],
                "havePrize": False
            },
            {
                "days": 2,
                "prize": [
                    "10京豆（共2000份，已发完）",
                    "优惠券（共50000份）"
                ],
                "havePrize": False
            }
        ],
        "minLevel": 1,
        "maxLevel": 2
    },
    # 其他数据...
}

data2 = {
    "2DBC61200A9E08B6B88DB4B305F59A09": {
        "index": 2,
        "venderId": 10026448,
        "shopName": "CHUMS运动户外旗舰店",
        "activityId": 12675623,
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
                "days": 3,
                "prize": [
                    "优惠券（共1000份）",
                    "5京豆（共1000份）"
                ],
                "havePrize": True
            }
        ],
        "minLevel": 0,
        "maxLevel": 3
    },
    # 其他数据...
}

# 合并并调整 index
merged_data = merge_and_adjust_index(data1, data2)
print(merged_data)
