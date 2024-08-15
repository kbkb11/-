import time

from robot.tg_robot.dataStruct.qlClient import QLClient
from robot.tg_robot.dataStruct.messageQueue import PriorityQueue
from robot.tg_robot.utils.parseUrl import parseMessage
from robot.tg_robot.utils.readAndWrite import load_task_by_name

start_time = time.time()

# serverConfig = QLClient(5700)
# serverConfig.init_tasks()
# serverConfig.init_envs()
# serverConfig.updateJDSignIp()

temp = load_task_by_name("幸运抽奖（超级无线）","6dylan6_jdm")
print(temp)