import time
from random import random

from adbutils import adb

from tools.adb import get_all_elements_info, swipe, tap, swipe_direction

device = adb.device()  # 获取连接的设备

# # 原始滑动操作，滑动 10000 次
# for i in range(10000):
#     swipe((158, 720), (920, 720), 0.1)  # 滑动 从 720 1280 滑动到 720 950 用 100 毫秒
#     print(f"Iteration: {i}")
#     time.sleep(0.05)

# tap_text_center_on_screen("立即翻卡", 1, 1, device)
# tap_text_center_on_screen("看视频翻十位卡", 1, 1, device)
# hg_advance()
# tap_text_center_on_screen("立即翻卡", 1, 1, device)
# tap_text_center_on_screen("看视频翻百位卡", 1, 1, device)
# hg_advance()
# tap_text_center_on_screen("立即翻卡", 1, 1, device)
# tap_text_center_on_screen("看视频翻千位卡", 1, 1, device)
# hg_advance()


while True:
    tap(930,1078)

    time.sleep(0.95)

    for i in range(6):
        # 定义起始点和结束点
        end = (376, 347)
        start = (646, 2025)

        # 执行滑动操作，持续时间0.58秒
        swipe(start, end, 0.58)

        # 随机等待3秒±1秒
        sleep_time = 3 + random() * 2 - 1
        print(f"Sleeping for {sleep_time:.2f} seconds")
        time.sleep(sleep_time)

    swipe_direction(4)

    time.sleep(0.95)

    tap(930,1078)

    time.sleep(0.95)

