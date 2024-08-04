import asyncio
import time

from telethon import TelegramClient, events

from robot.tg_robot.dataStruct.qlClient import QLClient
from robot.tg_robot.dataStruct.messageQueue import PriorityQueue, update_env_variable
from robot.tg_robot.utils.parseUrl import parseMessage
from robot.tg_robot.utils.qlOpenApi import calculateRunningTask, runCorn
from robot.tg_robot.utils.readAndWrite import load_task_by_name
import robot.tg_robot.spyConfig.sqyConfig as spyConfig

# 创建 Telegram 客户端
client = TelegramClient(
    'session_name',
    spyConfig.api_id,
    spyConfig.api_hash,
    proxy=(spyConfig.proxy_type, spyConfig.proxy_host, spyConfig.proxy_port)
)

# 配置和优先队列
config = QLClient(spyConfig.server_config_port)
priorityQueue = PriorityQueue()


# 处理收到的消息
@client.on(events.NewMessage(chats=spyConfig.listen_channels))
async def handler(event):
    message_text = event.message.message
    print(f"Received message:\n {message_text}")

    temp = parseMessage(config, message_text)
    if temp is not None:
        priorityQueue.put([temp[4], temp[1], temp[2], temp[3]])


async def consumePriorityQueueTasks():
    execution_timestamps = []  # 记录任务的执行时间戳，以跟踪任务执行情况
    max_tasks = 20  # 60分钟内允许的最大任务数
    interval_seconds = 3600  # 60分钟的秒数

    while True:
        if priorityQueue.size() > 0:
            print(f"开始执行任务, 优先队列中有{priorityQueue.size()}个任务待处理")

            current_time = time.time()  # 获取当前时间戳

            # 清除超出60分钟时间窗口的过期时间戳
            execution_timestamps = [ts for ts in execution_timestamps if current_time - ts <= interval_seconds]

            if len(execution_timestamps) >= max_tasks:
                # 如果在60分钟内已执行的任务数量达到上限，计算等待时间
                oldest_task_time = execution_timestamps[0]
                wait_time = interval_seconds - (current_time - oldest_task_time)
                if wait_time > 0:
                    print(f"达到最大任务数，等待 {wait_time} 秒")
                    await asyncio.sleep(wait_time)  # 使用 asyncio.sleep 等待指定时间

            # 检查当前是否有任务正在运行，如果有则等待
            while calculateRunningTask(config) > 0:
                print("当前有任务正在运行，进行等待")
                await asyncio.sleep(8)  # 每8秒检查一次

            # 从优先队列中取出优先级最高的任务
            nextTask = priorityQueue.get()

            print("完成准备操作")

            # 更新环境变量
            update_env_variable(config, nextTask[1], nextTask[2], nextTask[3], nextTask[0])
            nextTaskId = load_task_by_name(nextTask[2])['id']
            # 更新白名单
            runCorn(config, 646)
            print("代理白名单更新完成")
            # 更新JD签名地址
            config.updateJDSignIp()
            # 确保准备完成
            await asyncio.sleep(0.8)

            print(f"开始启动任务，任务ID：{nextTaskId}")

            # 运行任务
            runCorn(config, nextTaskId)
            print("任务启动完成")

            # 记录当前任务的执行时间戳
            execution_timestamps.append(time.time())
        else:
            # 如果队列为空，稍等后再检查
            await asyncio.sleep(5)


# 主函数
async def main():
    asyncio.create_task(consumePriorityQueueTasks())  # 启动异步任务
    async with client:
        await client.run_until_disconnected()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
