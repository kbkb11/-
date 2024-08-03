import json
import re
import time
import requests

from robot.tg_robot.config.constant import cache_envs_data
from robot.tg_robot.utils.qlOpenApi import createEnv
from robot.tg_robot.utils.readAndWrite import load_json, update_env_by_name, load_env_by_name


# 使用多个子函数进行判断：加购、关注、抽奖、积分兑换
def parseMessage(config, message):
    """
    解析消息，判断消息类型并进行相应处理。

    参数:
        message (str): 接收到的消息字符串。

    返回:
        str: 如果消息属于特定类型，则返回对应的字符串描述；否则返回 None。
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

        # TODO: 添加其他类型判断，如关注、抽奖、积分兑换
        # 例如：res = followShop(url, envData)

    return None


def addToPurchase(config, url):
    """
    判断URL是否为加购有礼类型，并更新相应环境变量。

    参数:
        url (str): 提取到的URL。

    返回:
        str: 如果URL为加购有礼类型，则返回对应的字符串描述；否则返回 None。
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
                    return update_env_variable(config, 'jd_lzkj_cart_url', '加购有礼（超级无线）', url)

                # 加购有礼（超级会员）
                if keyword in keywords[1]:
                    return update_env_variable(config, 'jd_wxCollectionActivity_activityUrl',
                                               '加购有礼（超级无线/超级会员）', url)
    return None


# TODO: 实现其他判断函数，例如：
def followShop(config, url):
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
                    return update_env_variable(
                        config,
                        'jd_lzkj_followGoods_url',
                        '关注商品有礼（超级无线）',
                        url
                    )

                # 关注店铺有礼（超级无线/超级会员）
                if keyword in keywords[1]:
                    return update_env_variable(
                        config,
                        'jd_wxShopFollowActivity_activityUrl',
                        '关注店铺有礼（超级无线/超级会员）',
                        url
                    )

                # 关注店铺有礼（超级无线）
                if keyword in keywords[2]:
                    return update_env_variable(
                        config,
                        'jd_lzkj_lkFollowShop_url',
                        '关注店铺有礼（超级无线）',
                        url
                    )
    return None


def update_env_variable(config, name, variable_name, url):
    """
    更新指定的环境变量。

    参数:
        variable_name (str): 要更新的环境变量名。
        url (str): 新的URL值。

    返回:
        str: 更新结果的描述信息。
    """
    print(f'开始更新: {variable_name} 变量')
    # 加载当前的环境变量值
    temp = load_env_by_name(name)

    if temp is None:
        createEnv(config, name, variable_name, url)
        return None

    temp['value'] = url
    # 更新环境变量
    res = update_env_by_name(name, temp)
    if res['code'] == 200:
        print('更新成功')
        return variable_name
    else:
        print(f'更新失败,{res}')
        return None
