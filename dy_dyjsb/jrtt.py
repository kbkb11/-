import random
import time
from adbutils import adb
from tools.adb import wake_screen, swipe_direction, open_app, tap, swipe
from tools.layout import tap_text_center_on_screen, get_text_center_from_screenshot, take_screenshot, \
    get_text_data_from_screenshot, find_text_center

# 模块级别的广告等待时间全局变量
AD_WAIT_TIME = 5

# 设备对象
device = None


def jrtt_readHotPaper():
    # 点击阅读
    tap(191, 672)
    time.sleep(random.uniform(1.42, 1.96))

    # 阅读
    jrtt_read(5)

    # 退出
    swipe_direction(4)
    time.sleep(random.uniform(1.42, 1.96))

    # 下移
    swipe((500, 1500), (500, 1300), random.uniform(1.42, 1.96))
    time.sleep(random.uniform(2.2, 2.96))


def jrtt_read(times):
    # 随机次数
    times = random.randint(times - 1, times + 3)

    for i in range(times):
        print(f"正在阅读第{i + 1}次")
        # 下移
        swipe((random.uniform(458, 512), random.uniform(1500, 1620)),
              (random.uniform(777, 888), random.uniform(600, 800)),
              random.uniform(1.42, 1.96)
              )

        time.sleep(random.uniform(7.42, 9.96))


def jrtt_advance():
    """看广告任务"""
    now_times = 1
    while True:
        start_time = time.time()

        wait_time = AD_WAIT_TIME * random.uniform(1.01, 1.15)
        time.sleep(wait_time)
        print(f"正在执行第{now_times}次广告任务,,等待时间{wait_time}秒")

        take_screenshot(1, 1, device)
        text_data = get_text_data_from_screenshot(1, 1, device)

        center = find_text_center(text_data, "广告", 2400, 1, 1)
        if center:
            print(f"处于广告页面,再次等待{wait_time+15}秒")
            time.sleep(wait_time+15)

        print(text_data)

        text = ["点击", "领取"]
        for i in range(len(text)):
            center = find_text_center(text_data, text[i], 2400, 1, 1)
            if center:
                print("找到点击领取,坐标为：", center)
                tap(center[0], center[1])
                time.sleep(random.uniform(1.42, 1.96))

                # 点击好的
                tap(569, 1408)
                time.sleep(random.uniform(1.42, 1.96))

                break

        # 截取屏幕截图
        take_screenshot(4, 1, device)
        center = get_text_center_from_screenshot("更多直播", 4, 1, device)
        if center:
            swipe_direction(4)
            time.sleep(random.uniform(1.42, 1.96))
            print("发现进入直播，返回视频页面")

        swipe((425, 1315), (425, 681), random.uniform(0.3, 0.5))
        print(f"进入下一次广告任务，本次花费{time.time() - start_time}秒")

def jrtt_readRandomPaper():
    '''随机搜'''
    # 点击“随即搜”按钮
    tap_text_center_on_screen("随机搜", 2, 2, device)

    for i in range(30):
        print(f"正在阅读第{i + 1}次")
        for j in range(6):
            # 下移
            swipe((random.uniform(458, 512), random.uniform(1500, 1620)),
                  (random.uniform(777, 888), random.uniform(600, 800)),
                  random.uniform(0.42, 0.96)
                  )
            time.sleep(random.uniform(4.42, 4.96))

        time.sleep(random.uniform(2.42, 5.96))

        swipe_direction(4)
        time.sleep(random.uniform(1.42, 1.96))

        # 点击“随即搜”按钮
        tap_text_center_on_screen("随机搜", 2, 2, device)




def main():
    """主函数"""
    global device
    device = adb.device()  # 获取连接的设备

    while True:
        # jrtt_readRandomPaper()
        jrtt_advance()


if __name__ == "__main__":
    main()
