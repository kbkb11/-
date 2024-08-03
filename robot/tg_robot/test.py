from robot.tg_robot.config.config import ServerConfig
from robot.tg_robot.utils.parseUrl import parseMessage
from robot.tg_robot.utils.readAndWrite import load_task_by_name

serverConfig = ServerConfig(5700)
# serverConfig.init_tasks()
# serverConfig.init_envs()
# serverConfig.updateJDSignIp()

message = """export jd_lzkj_lkFollowShop_url="https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&templateId=ac8b6564-aa35-4ba5-aa62-55b0ce61b5d01&activityId=1818587639804383233"""

temp = parseMessage(serverConfig,message)
print(temp)
print(temp['level'])
# task = load_task_by_name(temp[1])
# print(task)