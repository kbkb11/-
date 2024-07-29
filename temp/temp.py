# 点击“赚钱”按钮
import random
import time

from adbutils import adb

from tools.adb import swipe_direction, open_app, close_app, wake_screen, tap
from tools.layout import tap_text_center_on_screen, get_text_center_from_screenshot

device = adb.device()  # 获取连接的设备

sum = 1

# while True:
#     print("Start,now is", sum)
#     sum += 1
#     tap(1010, 729)
#     time.sleep(1)
#     tap(625, 1740)
#     # time.sleep(1)
#     # tap(573, 2134)
#     time.sleep(3 * 60)

while True:
    tap(575, 2145)
    time.sleep(12.5)
