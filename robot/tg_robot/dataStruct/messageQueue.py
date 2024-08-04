import heapq
import threading
import time

# 从自定义模块导入所需的函数
from robot.tg_robot.utils.qlOpenApi import calculateRunningTask, runCorn, createEnv, updateEnv
from robot.tg_robot.utils.readAndWrite import load_task_by_name, load_env_by_name, update_env_by_name


class PriorityQueue:
    """
    自定义优先队列类，用于处理带有优先级的任务。
    队列中的项格式为：
    [level, name, variable_name, url]
    其中，level 是任务的优先级，name 是任务的名称，variable_name 是变量名称，url 是任务的相关 URL。
    """

    def __init__(self):
        # 初始化优先队列、哈希表和线程锁
        self.queue = []
        self.item_map = {}  # 哈希表用于跟踪已存在的项
        self.lock = threading.Lock()

    def put(self, item):
        """
        将新项添加到优先队列中。
        如果项已经存在，则不进行添加。

        参数:
            item (list): 包含 [level, name, variable_name, url] 的列表。
        """
        with self.lock:
            item_key = (item[1], item[2])  # 使用 (name, variable_name) 作为唯一标识
            if item_key not in self.item_map:
                # 添加项到优先队列和哈希表
                heapq.heappush(self.queue, item)
                self.item_map[item_key] = item

    def get(self):
        """
        从优先队列中取出优先级最高的项。

        返回:
            list: 优先级最高的项，如果队列为空，则返回 None。
        """
        with self.lock:
            if len(self.queue) == 0:
                return None
            item = heapq.heappop(self.queue)
            item_key = (item[1], item[2])  # 使用 (name, variable_name) 作为唯一标识
            # 从哈希表中删除已取出的项
            del self.item_map[item_key]
            return item

    def size(self):
        """
        返回优先队列中项的数量。

        返回:
            int: 优先队列中项的数量。
        """
        with self.lock:
            return len(self.queue)

    def contains(self, name, variable_name):
        """
        检查哈希表中是否已存在指定的项。

        参数:
            name (str): 任务的名称。
            variable_name (str): 任务的变量名称。

        返回:
            bool: 如果项存在，则返回 True，否则返回 False。
        """
        with self.lock:
            return (name, variable_name) in self.item_map


def consumePriorityQueueTasks(config, priorityQueue):
    """
    任务执行规则：
        1. 60分钟内最多执行15个任务。
        2. 在有任务执行时需要等待，直到当前运行的任务完成。

    执行步骤：
        1. 初始化任务执行时间戳列表 `execution_timestamps`，用于记录任务的执行时间。
        2. 循环检查优先队列是否有任务待处理：
            2.1 获取当前时间戳 `current_time`。
            2.2 清除超出60分钟时间窗口的过期时间戳。
            2.3 如果60分钟内已执行的任务数量达到最大限制 `max_tasks`：
                2.3.1 计算等待时间，并进行等待。
                2.3.2 等待时间为：`interval_seconds - (current_time - oldest_task_time)`。
            2.4 检查当前是否有任务正在运行：
                2.4.1 如果有任务正在运行，每8秒检查一次，直到没有任务在运行。
            2.5 从优先队列中取出优先级最高的任务：
        3. 更新环境变量，并准备执行任务：
            3.1 通过 `update_env_variable` 函数更新环境变量。
            3.2 从任务名称中加载任务 ID。
            3.3 执行任务准备操作：
                3.3.1 更新白名单。
                3.3.2 更新 JD 签名地址。
            3.4 运行任务。
        4. 记录当前任务的执行时间戳。
    """
    execution_timestamps = []  # 记录任务的执行时间戳，以跟踪任务执行情况
    max_tasks = 15  # 60分钟内允许的最大任务数
    interval_seconds = 3600  # 60分钟的秒数

    while priorityQueue.size() > 0:
        current_time = time.time()  # 获取当前时间戳

        # 清除超出60分钟时间窗口的过期时间戳
        execution_timestamps = [ts for ts in execution_timestamps if current_time - ts <= interval_seconds]

        if len(execution_timestamps) >= max_tasks:
            # 如果在60分钟内已执行的任务数量达到上限，计算等待时间
            oldest_task_time = execution_timestamps[0]
            wait_time = interval_seconds - (current_time - oldest_task_time)
            if wait_time > 0:
                print(f"达到最大任务数，等待 {wait_time} 秒")
                time.sleep(wait_time)  # 等待指定时间后再尝试

        # 检查当前是否有任务正在运行，如果有则等待
        while calculateRunningTask(config) > 0:
            print("当前有任务正在运行，进行等待")
            time.sleep(8)  # 每8秒检查一次

        # 从优先队列中取出优先级最高的任务
        nextTask = priorityQueue.get()

        # 更新环境变量
        update_env_variable(config, nextTask[1], nextTask[2], nextTask[3], nextTask[0])
        nextTaskId = load_task_by_name(nextTask[2])['id']

        # 运行任务准备
        # 更新白名单
        runCorn(config, 646)
        # 更新JD签名地址
        config.updateJDSignIp()
        # 确保准备完成
        time.sleep(0.8)

        # 运行任务
        runCorn(config, nextTaskId)

        # 记录当前任务的执行时间戳
        execution_timestamps.append(time.time())


def update_env_variable(config, name, variable_name, url, level):
    """
    更新指定的环境变量。

    参数:
        config (dict): 配置信息。
        name (str): 环境变量的名称。
        variable_name (str): 环境变量的描述信息。
        url (str): 新的 URL 值。
        level (str): 环境变量的等级。

    返回:
        dict: 更新结果的描述信息，如果更新失败返回 None。
    """
    print(f'开始更新: {variable_name} 变量')
    # 加载当前的环境变量值
    temp = load_env_by_name(name)

    if temp is None:
        # 如果环境变量不存在，则创建新的环境变量
        createEnv(config, name, variable_name, url)
        config.init_envs()
        return {
            "variable_name": variable_name,
            "level": level,
        }

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
        print(f'更新失败, {res}')
        return None
