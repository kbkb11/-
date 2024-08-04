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
            item_key = (item[1], item[2], item[3])  # 使用 (name, variable_name, url) 作为唯一标识
            if item_key not in self.item_map:
                # 添加项到优先队列和哈希表
                heapq.heappush(self.queue, item)
                self.item_map[item_key] = item
                print(f"添加任务：{item[2]}")
            else:
                print(f"任务已存在：{item[2]}")

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
            item_key = (item[1], item[2], item[3])  # 使用 (name, variable_name, url) 作为唯一标识
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


def update_env_variable(config, name, variable_name, url, level):
    """
    更新指定的环境变量。

    参数:
        spyConfig (dict): 配置信息。
        name (str): 环境变量的名称。
        variable_name (str): 环境变量的描述信息。
        url (str): 新的 URL 值。
        level (str): 环境变量的等级。

    返回:
        dict: 更新结果的描述信息，如果更新失败返回 None。
    """
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
        return {
            "variable_name": variable_name,
            "level": level,
        }
    else:
        print(f'更新失败, {res}')
        return None
