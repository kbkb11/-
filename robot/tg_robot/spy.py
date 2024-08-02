import asyncio
import logging
import subprocess
import python_socks
import socks
from telethon import TelegramClient, events

# 配置日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 配置
api_id = 13721161
api_hash = '406c2721e7070ecf32f7a160508745f6'

# 监听频道和关键字
# listen_channels = [-1001670294604, -1001651974395, -1001712811852, -1002161138187]
listen_channels = [-4226546044]
forward_keywords = ['export', 'http']

# tg转发群和青龙配置
log_channel_id = -4226546044
config_file_path = (r'\\wsl.localhost\docker-desktop-message\message\docker\volumes'
                    r'\b97a90379f53757dbef58f27791154e3db4afd5c98ba455a64a8a10f7d1bf64d\_message\config\config.sh')

# 创建 Telegram 客户端
client = TelegramClient('session_name', api_id, api_hash,
                        timeout=10,
                        proxy=(socks.SOCKS5, '127.0.0.1', 7897))


# 处理收到的消息
@client.on(events.NewMessage(chats=listen_channels))
async def handler(event):
    message_text = event.message.message
    logger.info(f"Received message: {message_text}")

    # 解析消息数据并检查是否包含关键字
    if any(keyword in message_text for keyword in forward_keywords):
        await update_qinglong_config(message_text)
        await execute_qinglong_task()


# 更新青龙配置文件的函数
async def update_qinglong_config(message):
    try:
        key, value = message.split('=')
        with open(config_file_path, 'a') as f:
            f.write(f'{key}={value}\n')
        logger.info("Updated QingLong configuration successfully.")
    except Exception as e:
        logger.error(f"Failed to update QingLong configuration: {e}")


# 执行青龙任务的函数
async def execute_qinglong_task():
    try:
        result = subprocess.run(['ql', 'task'], check=True, capture_output=True, text=True)
        logger.info(f"QingLong task executed successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to execute QingLong task: {e.stderr}")


# 主函数
async def main():
    async with client:
        await client.run_until_disconnected()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
