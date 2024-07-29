import re
import time

import itchat


def extract_http_urls(text):
    # 定义正则表达式模式来匹配以 http: 或 https: 开头的 URL
    pattern = r'https?://[^\s"]+'
    # 使用正则表达式查找所有匹配的 URL
    urls = re.findall(pattern, text)
    return urls


def contains_keywords(text, keywords):
    # 检查文本是否包含任何一个关键词
    return any(keyword in text for keyword in keywords)


def get_user_name_by_wechat_id(wechat_id):
    # 获取好友列表
    friends = itchat.get_friends()
    # 查找匹配的好友
    for friend in friends:
        if friend['NickName'] == wechat_id or friend['RemarkName'] == wechat_id:
            return friend['UserName']
    return None


def get_chatroom_by_name(chatroom_name):
    # 获取群聊列表
    chatrooms = itchat.get_chatrooms()
    # 查找匹配的群聊
    for chatroom in chatrooms:
        if chatroom_name in chatroom['NickName']:
            return chatroom['UserName']
    return None


def handle_message(msg):
    # 提取 http 或 https 开头的 URL
    urls = extract_http_urls(msg['Text'])
    # 检查是否包含指定的关键词
    for i in range(len(urls)):
        if not contains_keywords(urls[i], keywords):
            # 推送消息
            response_message = f"检测到新线报: \n {urls[i]}"
            # 指定要发送的群聊名称
            target_chatroom_name = '京东'  # 替换为目标群聊名称
            chatroom_user_name = get_chatroom_by_name(target_chatroom_name)
            if chatroom_user_name:
                itchat.send(response_message, toUserName=chatroom_user_name)
            else:
                print(f"未找到名称为 '{target_chatroom_name}' 的群聊")


@itchat.msg_register(['Text'], isGroupChat=True)
def text_reply(msg):
    handle_message(msg)


# 关键词列表
keywords = ["https://u.jd.com", "https://3.cn"]

# 登录并开始监听
itchat.auto_login()
itchat.run()