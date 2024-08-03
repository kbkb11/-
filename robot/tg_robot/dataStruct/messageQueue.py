import heapq
import re
import threading
import time

from robot.tg_robot.utils.qlOpenApi import calculateRunningTask, runCorn, createEnv, updateEnv
from robot.tg_robot.utils.readAndWrite import load_task_by_name, load_env_by_name, update_env_by_name


class PriorityQueue:
    def __init__(self):
        # 初始化优先队列和线程锁
        self.queue = []
        self.lock = threading.Lock()

    def put(self, item):
        # 将新项添加到优先队列中
        with self.lock:
            heapq.heappush(self.queue, item)

    def get(self):
        # 从优先队列中取出优先级最高的项
        with self.lock:
            if len(self.queue) == 0:
                return None
            return heapq.heappop(self.queue)

    def size(self):
        # 返回优先队列中项的数量
        with self.lock:
            return len(self.queue)


def consumeMessage(config, priorityQueue):
    while priorityQueue.size() > 0:
        # 从优先队列中取出优先级最高的任务再更新环境变量
        nextTask = priorityQueue.get()
        update_env_variable(config, nextTask[1], nextTask[2], nextTask[3], nextTask[0])

        # 检查当前运行的任务数量
        sum = calculateRunningTask(config)
        while sum > 0:
            # 如果有任务正在运行，等待一段时间后重新检查
            print(f"当前有 {sum} 个任务正在运行,进行等待")
            time.sleep(8)
            sum = calculateRunningTask(config)

        # 运行任务
        runCorn(config, nextTask[2])


def update_env_variable(config, name, variable_name, url, level):
    """
    更新指定的环境变量。

    参数:
        config (dict): 配置信息。
        name (str): 环境变量的名称。
        variable_name (str): 环境变量的描述信息。
        url (str): 新的URL值。
        level (str): 环境变量的等级。

    返回:
        json: 更新结果的描述信息。
    """
    print(f'开始更新: {variable_name} 变量')
    # 加载当前的环境变量值
    temp = load_env_by_name(name)

    if temp is None:
        createEnv(config, name, variable_name, url)
        config.init_envs()
        return variable_name

    temp['value'] = url
    # 更新环境变量
    res = update_env_by_name(name, temp)
    updateEnv(config, temp['id'], temp['name'], temp['remarks'], temp['value'])
    if res is True:
        print('更新成功')
        return {
            "variable_name": variable_name,
            "level": level,
        }
    else:
        print(f'更新失败,{res}')
        return None