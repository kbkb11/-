import time
import random

from tools.adb import swipe, tap

AD_WAIT_TIME = 3
tap1 = False
sum_swipe = 0

while True:
    # 定义起始点和结束点
    end = (396, 347)
    start = (626, 1625)

    # 执行滑动操作，持续时间0.58秒
    swipe(start, end, random.uniform(0.2, 0.42))

    # # 随机数生成
    # rand_value = random
    # print(f"Random value: {rand_value:.2f}")

    time.sleep(1.34)
    # if tap1:
    #     # 根据随机数点击屏幕
    #     if rand_value > 0.75:
    #         print("Tap 1 time")
    #         tap(997, 1354)  # 点赞
    #     # elif rand_value > 0.3:
    #     #     print("Tap 2 times")
    #     #     tap(997, 1354)  # 点赞
    #     #     time.sleep(1.5)  # 两次点击之间的短暂延迟
    #     #     tap(997, 1354)  # 点赞

    # 随机等待3秒±1秒
    sleep_time = AD_WAIT_TIME + random.uniform(0, 2) * 2 - 1
    sum_swipe += 1
    print(f"Sleeping for {sleep_time:.2f} seconds, swipe {sum_swipe} times")
    time.sleep(sleep_time)
