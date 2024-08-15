import time
import random

from adbutils import adb

from tools.adb import swipe, tap, swipe_direction
from tools.layout import tap_text_center_on_screen, take_screenshot, get_text_center_from_screenshot

AD_WAIT_TIME = 3*60
tap1 = False
sum_swipe = 0

device = adb.device()  # 获取连接的设备

# while True:
#     # centers = [, [872, 702], [879, 901], [868, 1109], [870, 1302]]
#     centers = [[879, 901], [868, 1109], [870, 1302]]
#     for center in centers:
#         print("点击广告按钮：", center)
#         tap(center[0], center[1])
#
#         time.sleep(65)
#         tap(973,251)
#         print("退出广告")
#
#         time.sleep(3)
#         tap(561, 1712)
#         print("退出广告任务")
#
#         time.sleep(5)

time.sleep(1)

while True:
    # 定义起始点和结束点
    end = (396, 347)
    start = (626, 1625)

    # 执行滑动操作，持续时间0.58秒
    swipe(start, end, random.uniform(0.2, 0.42))

    time.sleep(1.34)

    # 随机等待3秒±1秒
    sleep_time = AD_WAIT_TIME + random.uniform(0, 2) * 2 - 1
    sum_swipe += 1
    print(f"Sleeping for {sleep_time:.2f} seconds, swipe {sum_swipe} times")
    time.sleep(sleep_time)
