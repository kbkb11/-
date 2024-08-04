import json

from robot.tg_robot.spyConfig.sqyConfig import cache_envs_data, cache_tasks_data


def load_json(file_path):
    """
    读取现有的json数据

    参数:
    file_path (str): 文件的路径

    返回:
    dict: 读取到的任务数据
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return None
    except json.JSONDecodeError:
        print(f"文件 {file_path} 不是有效的 JSON 格式。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None


def write_json(file_path, data):
    """
    将数据写入json文件

    参数:
    file_path (str): 文件的路径
    data (dict): 要写入的数据

    返回:
    bool: 写入是否成功
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"写入文件时发生错误: {e}")
        return False


def load_task_by_name(task_name):
    """
    根据任务名称从 JSON 文件中读取任务信息。

    :param task_name: 任务名称
    :return: 任务信息字典，如果未找到任务则返回 None
    """
    try:
        with open(cache_tasks_data, 'r', encoding='utf-8') as f:
            tasks = json.load(f)

        for task in tasks:
            if task.get("name") == task_name:
                return task

        print(f"未找到名称为 {task_name} 的任务")
        return None

    except FileNotFoundError:
        print(f"文件 {cache_tasks_data} 未找到")
        return None
    except json.JSONDecodeError:
        print(f"文件 {cache_tasks_data} 不是有效的 JSON 格式")
        return None


def load_env_by_name(env_name):
    """
    根据环境变量名称从 JSON 文件中读取环境变量信息。

    :param env_name: 环境变量名称
    :return: 环境变量信息字典，如果未找到环境变量则返回 None
    """
    try:
        with open(cache_envs_data, 'r', encoding='utf-8') as f:
            envs = json.load(f)

        for env in envs:
            if env.get("name") == env_name:
                return env

        print(f"未找到名称为 {env_name} 的环境变量")
        return None

    except FileNotFoundError:
        print(f"文件 {cache_envs_data} 未找到")
        return None
    except json.JSONDecodeError:
        print(f"文件 {cache_envs_data} 不是有效的 JSON 格式")
        return None


def update_task_by_name(task_name, updated_data):
    """
    根据任务名称更新 JSON 文件中的任务信息。

    :param task_name: 任务名称
    :param updated_data: 更新后的任务数据，字典格式
    :return: 更新是否成功的布尔值
    """
    try:
        # 读取现有的任务数据
        tasks = load_json(cache_tasks_data)

        # 查找并更新任务
        task_found = False
        for task in tasks:
            if task.get("name") == task_name:
                task.update(updated_data)
                task_found = True
                break

        if not task_found:
            print(f"未找到名称为 {task_name} 的任务")
            return False

        # 写回更新后的数据
        write_json(cache_tasks_data, tasks)

        print(f"任务 {task_name} 更新成功")
        return True

    except FileNotFoundError:
        print(f"文件 {cache_tasks_data} 未找到")
        return False
    except json.JSONDecodeError:
        print(f"文件 {cache_tasks_data} 不是有效的 JSON 格式")
        return False


def update_env_by_name(env_name, updated_data):
    """
    根据环境变量名称更新 JSON 文件中的环境变量信息。

    :param env_name: 环境变量名称
    :param updated_data: 更新后的环境变量数据，字典格式
    :return: 更新是否成功的布尔值
    """
    try:
        # 读取现有的环境变量数据
        envs = load_json(cache_envs_data)

        # 查找并更新环境变量
        env_found = False
        for env in envs:
            if env.get("name") == env_name:
                env.update(updated_data)
                env_found = True
                break

        if not env_found:
            print(f"未找到名称为 {env_name} 的环境变量")
            return False

        # 写回更新后的数据
        write_json(cache_envs_data, envs)

        print(f"环境变量 {env_name} 更新成功")
        return True

    except FileNotFoundError:
        print(f"文件 {cache_envs_data} 未找到")
        return False
    except json.JSONDecodeError:
        print(f"文件 {cache_envs_data} 不是有效的 JSON 格式")
        return False
