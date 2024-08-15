# spyConfig.py
import socks

# Telegram API ID 和 API 哈希
api_id = 13721161
api_hash = '406c2721e7070ecf32f7a160508745f6'

# 监听频道和关键字
listen_channels = [
    -1001670294604,
    -1001651974395,
    -1001712811852,
    # -1002161138187, #动物那个频道
    -4226546044
]

# 代理配置
proxy_type = socks.SOCKS5
proxy_host = '127.0.0.1'
proxy_port = 7897

# 服务器配置端口
server_config_port = 5700

# 任务配置
max_tasks = 20  # 60分钟内允许的最大任务数
interval_seconds = 3600  # 60分钟的秒数

# 文件路径配置
root_file = r"D:\begin\code\script\robot\tg_robot"
cache_tasks_data = r"D:\begin\code\script\robot\tg_robot\cache_json\tasks_data.json"
cache_envs_data = r"D:\begin\code\script\robot\tg_robot\cache_json\envs_data.json"

# 客户端 ID 和客户端密钥
client_id = "h_EAL1JJV92j"
client_secret = "_UW_1DuQKE2eYtbJgfNMG_7H"
