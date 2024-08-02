import itchat
import requests
import json
import os

# QingLong API配置
QL_URL = "http://localhost:5700"
CLIENT_ID = "qatFPpS-_0X3"
CLIENT_SECRET = "w0zWIBi5bDWvNRBez_9Lsd1x"

CK_FILE = "user_ck.json"


# 获取青龙API的访问Token
def get_ql_token():
    url = f"{QL_URL}/open/auth/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("message").get("token")
    else:
        print(f"获取Token失败: {response.json()}")
        return None


def get_existing_envs(token):
    url = f"{QL_URL}/open/envs"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("message", [])
    else:
        print(f"获取现有环境变量失败: {response.json()}")
        return []


def validate_ck_format(ck):
    # 检查是否包含两个分号
    parts = ck.split(';')
    if len(parts) != 3:
        return False

    # 检查pt_key和pt_pin的存在及长度
    pt_key = parts[0].strip()
    pt_pin = parts[1].strip()

    if not pt_key.startswith('pt_key=') or not pt_pin.startswith('pt_pin='):
        return False

    if len(pt_key) < 10 or len(pt_pin) < 10:
        return False

    return True


def load_user_cks():
    if os.path.exists(CK_FILE):
        with open(CK_FILE, "r") as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
    return {}


def save_user_cks(user_cks):
    with open(CK_FILE, "w") as file:
        json.dump(user_cks, file, indent=4)


def get_existing_envs(token):
    url = f"{QL_URL}/open/envs"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("message", [])
    else:
        print(f"获取现有环境变量失败: {response.json()}")
        return []


def add_or_update_env_to_ql(ck, toUserName):
    token = get_ql_token()
    if not token:
        itchat.send("获取Token失败", toUserName=toUserName)
        return

    existing_envs = get_existing_envs(token)
    env_name = "JD_COOKIE"
    new_ck = ck + "&"

    for env in existing_envs:
        if env['name'] == env_name and new_ck in env['value']:
            itchat.send("CK已存在", toUserName=toUserName)
            return

    for env in existing_envs:
        if env['name'] == env_name:
            updated_value = env['value'] + "\n" + new_ck
            url = f"{QL_URL}/open/envs"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            update_env = {
                "id": env['id'],
                "name": env_name,
                "value": updated_value,
                "remarks": env.get("remarks", "")
            }

            response = requests.put(url, json=update_env, headers=headers)
            if response.status_code == 200:
                itchat.send("CK添加成功", toUserName=toUserName)
            else:
                itchat.send(f"添加CK失败: {response.json()}", toUserName=toUserName)
            return

    itchat.send("未找到JD_COOKIE环境变量", toUserName=toUserName)


# 获取用户的CK数目和pt_pin
def get_user_ck_info(user_id):
    user_cks = load_user_cks()
    if user_id in user_cks:
        cks = user_cks[user_id]
        ck_count = len(cks)
        ck_info = []
        for ck in cks:
            parts = ck.split(';')
            pt_pin = parts[1].strip().replace("pt_pin=", "")
            ck_info.append(f"pt_pin={pt_pin}")
        return ck_count, ck_info
    return 0, []


# 执行脚本
def execute_script(ck):
    # 替换成实际需要执行的脚本
    print(f"执行脚本，使用CK: {ck}")


# 微信消息处理
@itchat.msg_register(['Text'])
def text_reply(msg):
    reply = msg['Text']
    user_cks = load_user_cks()
    user_id = msg['FromUserName']

    if reply == '菜单':
        itchat.send("这是一个菜单列表", toUserName=msg['FromUserName'])
    elif reply.startswith("/ck"):
        ck = reply[4:]
        if validate_ck_format(ck):
            if user_id not in user_cks:
                user_cks[user_id] = []
            user_cks[user_id].append(ck)
            save_user_cks(user_cks)
            add_or_update_env_to_ql(ck, msg['FromUserName'])
        else:
            itchat.send("CK格式错误", toUserName=msg['FromUserName'])
    elif reply.startswith("/执行"):
        if user_id in user_cks:
            for ck in user_cks[user_id]:
                execute_script(ck)
        else:
            itchat.send("你还没有提交CK", toUserName=msg['FromUserName'])
    elif reply == "/look":
        ck_count, ck_info = get_user_ck_info(user_id)
        if ck_count > 0:
            ck_info_str = "\n".join(ck_info)
            itchat.send(f"你当前有{ck_count}个CK:\n{ck_info_str}", toUserName=msg['FromUserName'])
        else:
            itchat.send("你当前没有CK", toUserName=msg['FromUserName'])
    else:
        print(reply)


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
