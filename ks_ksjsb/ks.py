import random
import time
from adbutils import adb
from tools.adb import wake_screen, swipe_direction, open_app, close_app, turn_off_screen, tap, swipe, multi_tap
from tools.layout import tap_text_center_on_screen, get_text_center_from_screenshot, take_screenshot, \
    get_text_data_from_screenshot, find_text_center

# 模块级别的广告等待时间全局变量
AD_WAIT_TIME = 47

# 设备对象
device = None


def ks_init():
    """初始化设备和应用"""
    global device
    device = adb.device()  # 获取连接的设备

    # 唤醒设备
    wake_screen()

    # 向上滑动解锁屏幕
    swipe_direction(1)

    time.sleep(1.24)

    # 打开快手极速版应用
    open_app("com.smile.gifmaker")


def ks_task_open_daily_box():
    """开宝箱任务"""
    # 点击“开宝箱”按钮
    tap_text_center_on_screen("领福利", 1, 1, device)
    # 执行广告相关操作
    ks_advance()

    print("退出")


def ks_task_advance():
    # 点击领福利
    take_screenshot(1, 1, device)
    center = get_text_center_from_screenshot("领福利", 1, 1, device)
    if center:
        tap(center[0], center[1])
    else:
        tap_text_center_on_screen("去赚钱", 1, 1, device)
        tap_text_center_on_screen("领福利", 1, 1, device)
    # 执行广告相关操作
    ks_advance()

    print("退出")


def ks_advance():
    """等待广告视频播放完成"""
    print("开始处理广告")
    # 等待广告视频播放完成
    time.sleep(AD_WAIT_TIME)
    print("广告播放完成，等待广告类型处理")
    # 处理广告类型
    ks_advance_check()
    swipe_direction(4)
    time.sleep(random.uniform(1.5, 2.5))

    take_screenshot(2, 2, device)
    center = get_text_center_from_screenshot("领取奖励", 2, 2, device)
    while center:
        print("找到领取奖励按钮")
        print(center[0], center[1])
        tap(center[0], center[1])

        # 等待广告视频播放完成
        time.sleep(AD_WAIT_TIME)
        print("广告播放完成，等待广告类型处理")
        # 处理广告类型
        ks_advance_check()
        swipe_direction(4)
        time.sleep(random.uniform(1.5, 2.5))

        take_screenshot(2, 2, device)
        center = get_text_center_from_screenshot("领取奖励", 2, 2, device)
    print("广告处理完成")

    # swipe_direction(4)
    print("退出广告任务")


def ks_advance_check():
    """处理广告类型"""
    print("检查广告类型")
    take_screenshot(2, 2, device)
    text_data = get_text_data_from_screenshot(2, 2, device)

    # print(text_data)

    text = ["打开", "下载", "直播", "了解", "额外"]
    for i in range(len(text)):
        center = find_text_center(text_data, text[i], 2400, 2, 2)
        if center:
            print(center[0], center[1])
            if i == 0:
                print(f"点击打开按钮: {text[i]}")
                tap(center[0], center[1])
                time.sleep(random.uniform(1.8, 2.6))
                tap(797, 2200)
                time.sleep(random.uniform(25, 34))
                open_app("com.smile.gifmaker")
                return
            if i == 1:
                print("点击下载上方的应用详细")
                tap(558, 1423)
                time.sleep(random.uniform(25, 34))
                swipe_direction(4)
                return
            if i == 2:
                print("点击直播按钮")
                tap(558, 1642)
                time.sleep(random.uniform(1.2, 1.8) * 60)
                swipe_direction(4)
                return
            if i == 3:
                print("点击了解按钮")
                tap(559, 1918)
                time.sleep(random.uniform(25, 34))
                swipe_direction(4)
                return
            if i == 4:
                print("点击额外获取金币按钮")
                tap(center[0], center[1])
                time.sleep(random.uniform(1.8, 2.6))
                tap(797, 2200)
                time.sleep(random.uniform(25, 34))
                open_app("com.smile.gifmaker")
                return
    # print("滑动以继续")
    # swipe_direction(4)


def ks_keep_account():
    """活跃账号任务"""
    print("开始活跃账号任务")
    # 点击直播间
    tap(125, 347)
    print("进入直播间")

    # 等待 13.5 到 15.5 分钟
    time_to_wait = random.uniform(15.5 * 60, 17.5 * 60)
    print(f"等待时间: {time_to_wait / 60} 分钟")
    time.sleep(time_to_wait)

    # 退出直播间
    swipe_direction(4)
    print("退出直播间")


def ks_keep_account_lookShortVideo(num):
    """养号操作1:看短视频"""
    # 进入精选页面
    tap_text_center_on_screen("精选", 8, 8, device)

    max_swipes = int(num * (15 + 3 * random.uniform(1, 2.5) - 0.5))
    print(f"执行养号操作, 本轮次数为:{max_swipes}")

    time.sleep(1.42)
    for i in range(max_swipes):
        swipe((646, 1425), (376, 347), random.uniform(0.3, 0.62))

        wait_time = random.uniform(10, 20)

        # 截取屏幕截图
        take_screenshot(4, 4, device)
        center = get_text_center_from_screenshot("广告", 4, 4, device)
        if center:
            wait_time = random.uniform(30, 40) + 15

        time.sleep(wait_time)
        print(f"养号操作进度: {i + 1}/{max_swipes}  等待时间为: {wait_time}")

    tap(111, 384)
    time.sleep(1.23)
    print("返回赚钱页面")


def ks_food_duck(sum):
    for i in range(sum):
        tap(559, 1896)
        time.sleep(random.uniform(10, 12))
        print(f"喂养第{i+1}次")
    print("喂养结束")


def main():
    """主函数"""
    global device
    device = adb.device()  # 获取连接的设备
    while True:
        # ks_task_advance()
        ks_keep_account_lookShortVideo(10)
        time.sleep(random.uniform(1.5, 2.5))

    # while True:
    #     tap(564,1329)
    #     time.sleep(random.uniform(5.5, 10.5))

    # while True:
    #     multi_tap(750, 750, 800, 800, 60)
    #     time.sleep(random.uniform(3, 4) * 60 * random.uniform(1.1, 1.2))


if __name__ == "__main__":
    main()
