import json
import re
import time
import requests

from robot.tg_robot.config.constant import cache_envs_data
from robot.tg_robot.utils.qlOpenApi import createEnv, updateEnv
from robot.tg_robot.utils.readAndWrite import load_json, update_env_by_name, load_env_by_name


# 使用多个子函数进行判断：加购、关注、抽奖、积分兑换
def parseMessage(config, message):
    """
    解析消息，判断消息类型并进行相应处理。

    参数:
        config (dict): 配置信息。
        message (str): 接收到的消息字符串。

    返回:
        json: 如果消息属于特定类型，则返回对应的字符串描述；否则返回 None。
    """

    # 使用正则表达式从消息中提取URL
    url_pattern = r'http[s]?://[^\s"]+'
    match = re.search(url_pattern, message)
    url = match.group() if match else None

    if url:
        # 判断是否为加购类
        res = addToPurchase(config, url)
        if res:
            return res

        # 判断是否为关注类
        res = followShop(config, url)
        if res:
            return res

        # 判断是否为抽奖类
        res = lottery(config, url)
        if res:
            return res

        # 判断是否为积分兑换类
        res = exchangePoints(config, url)
        if res:
            return res

    return None


def addToPurchase(config, url):
    """
    判断URL是否为加购有礼类型，并更新相应环境变量。

    参数:
        config (dict): 配置信息。
        url (str): 提取到的URL。

    返回:
        json: 如果URL为加购有礼类型，则返回对应的字符串描述；否则返回 None。
    """
    # 关键词列表，用于判断URL类型
    keywords = [
        ['https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10024&templateId=',
         'https://lzkj-isv.isvjcloud.com/prod/cc/interaction/v1/index?activityType=10024&templateId='],

        ['https://lzkj-isv.isvjd.com/wxCollectionActivity/activity?activityId=',
         'https://cjhy-isv.isvjcloud.com/wxCollectionActivity/activity?activityId=',
         'https://lzkj-isv.isvjd.com/wxCollectionActivity/activity2/activity?activityId=',
         'https://cjhy-isv.isvjd.com/wxCollectionActivity/activity2/activity?activityId='
         ],
    ]

    # 检查URL是否包含在关键词列表中
    for keyword_list in keywords:
        for keyword in keyword_list:
            if keyword in url:
                # 加购有礼（超级无线）
                if keyword in keywords[0]:
                    return [
                        config,
                        'jd_lzkj_cart_url',
                        '加购有礼（超级无线）',
                        url,
                        1
                    ]

                # 加购有礼（超级会员）
                if keyword in keywords[1]:
                    return [
                        config,
                        'jd_wxCollectionActivity_activityUrl',
                        '加购有礼（超级无线/超级会员）',
                        url,
                        1
                    ]
    return None


def followShop(config, url):
    """
    判断URL是否为关注店铺类型，并更新相应环境变量。

    参数:
        config (dict): 配置信息。
        url (str): 提取到的URL。

    返回:
        json: 如果URL为关注店铺类型，则返回对应的字符串描述；否则返回 None。
    """
    # 关键词列表，用于判断URL类型
    keywords = [
        ['https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10053&templateId=',
         'https://lzkj-isv.isvjcloud.com/prod/cc/interaction/v1/index?activityType=10053&templateId='],

        ['https://cjhy-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=',
         'https://lzkj-isv.isvjcloud.com/wxShopFollowActivity/activity/activity?activityId=',
         ],

        ['https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&templateId=',
         'https://lzkj-isv.isvjcloud.com/prod/cc/interaction/v1/index?activityType=10069&templateId=',
         'https://lorealjdcampaign-rc.isvjcloud.com/interact/index?activityType=10069&templateId='
         ]
    ]

    # 检查URL是否包含在关键词列表中
    for keyword_list in keywords:
        for keyword in keyword_list:
            if keyword in url:
                # 关注商品有礼（超级无线）
                if keyword in keywords[0]:
                    return [
                        config,
                        'jd_lzkj_followGoods_url',
                        '关注商品有礼（超级无线）',
                        url,
                        2
                    ]

                # 关注店铺有礼（超级无线/超级会员）
                if keyword in keywords[1]:
                    return [
                        config,
                        'jd_wxShopFollowActivity_activityUrl',
                        '关注店铺有礼（超级无线/超级会员）',
                        url,
                        2
                    ]

                # 关注店铺有礼（超级无线）
                if keyword in keywords[2]:
                    return [
                        config,
                        'jd_lzkj_lkFollowShop_url',
                        '关注店铺有礼（超级无线）',
                        url,
                        2
                    ]
    return None


def lottery(config, url):
    """
    判断URL是否为抽奖类型，并更新相应环境变量。

    参数:
        config (dict): 配置信息。
        url (str): 提取到的URL。

    返回:
        json: 如果URL为抽奖类型，则返回对应的字符串描述；否则返回 None。
    """
    # 关键词列表，用于判断URL类型
    keywords = [
        ['https://lzkj-isv.isvjd.com/lzclient/<活动id>/cjwx/common/entry.html?activityId=',
         'https://lzkj-isv.isvjd.com/wxDrawActivity/activity/activity?activityId=',
         'https://cjhy-isv.isvjcloud.com/wxDrawActivity/activity/activity?activityId='
         ]
    ]
    for keyword_list in keywords:
        for keyword in keyword_list:
            if keyword in url:
                # 店铺抽奖（超级无线/超级会员）
                if keyword in keywords[0]:
                    return [
                        config,
                        'LUCK_DRAW_URL',
                        '店铺抽奖（超级无线/超级会员）',
                        url,
                        3
                    ]

    return None


# 积分兑换
def exchangePoints(config, url):
    """
    判断URL是否为积分兑换类型，并更新相应环境变量。

    参数:
        config (dict): 配置信息。
        url (str): 提取到的URL。

    返回:
        json: 如果URL为积分兑换类型，则返回对应的字符串描述；否则返回 None。
    """
    # 关键词列表，用于判断URL类型
    keywords = [
        ['https://cjhy-isv.isvjcloud.com/mc/wxPointShopView/pointExgBeans?venderId=',
         ]
    ]
    for keyword_list in keywords:
        for keyword in keyword_list:
            if keyword in url:
                # 积分兑换京豆（超级会员）
                if keyword in keywords[0]:
                    return [
                        config,
                        'jd_pointExgBeans_activityUrl',
                        '积分兑换京豆（超级会员）',
                        url,
                        4
                    ]

    return None