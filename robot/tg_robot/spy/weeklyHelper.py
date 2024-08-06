import asyncio
from telethon import TelegramClient
import robot.tg_robot.spyConfig.sqyConfig as spyConfig

# 机器人用户名
bot_username = '@chriszhuli_bot'


async def send_messages():
    client = TelegramClient(
        'session_name',
        spyConfig.api_id,
        spyConfig.api_hash,
        proxy=(spyConfig.proxy_type, spyConfig.proxy_host, spyConfig.proxy_port)  # 如果没有代理可以去掉这个参数
    )

    await client.start()  # 启动客户端并连接到 Telegram

    # 发送三条信息
    messages = [
        '/bean 47m36n7ro5gutjoimvtfqyp6fhqvmxnblrlzxii',
        '/farm 238105e50b6149a6a6eb824934e6998d',
        '/newfarm ycXdOaS1kk-ha0kXHoPTSCybS0GAek-0'
    ]

    for message in messages:
        await client.send_message(bot_username, message)
        print(f'消息发送成功: {message}')

    await client.disconnect()  # 断开连接


if __name__ == "__main__":
    asyncio.run(send_messages())  # 使用 asyncio.run() 运行异步函数
