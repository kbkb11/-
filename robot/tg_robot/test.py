import time

from robot.tg_robot.config.config import ServerConfig
from robot.tg_robot.utils.parseUrl import parseMessage

start_time = time.time()

serverConfig = ServerConfig(5700)
# serverConfig.init_tasks()
# serverConfig.init_envs()
# serverConfig.updateJDSignIp()

message = """https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10024&templateId=20210518190900jgyl011&activityId=1818486005944868866"""

temp = parseMessage(serverConfig, message)

end_time = time.time()
print(end_time - start_time)
print(temp)
print(temp[4])
# task = load_task_by_name(temp[1])
# print(task)
