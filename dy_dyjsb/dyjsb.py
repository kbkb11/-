import random
import time
from adbutils import adb
from tools.adb import wake_screen, swipe_direction, open_app, tap, swipe
from tools.layout import tap_text_center_on_screen, get_text_center_from_screenshot, take_screenshot

# 模块级别的广告等待时间全局变量
AD_WAIT_TIME = 37

# 设备对象
device = None


def dyjsb_init():
    """初始化设备和应用"""
    global device
    device = adb.device()  # 获取连接的设备

    # 唤醒设备
    wake_screen()

    # 向上滑动解锁屏幕
    swipe_direction(1)

    time.sleep(1.24)

    # 打开抖音极速版应用
    open_app("com.ss.android.ugc.aweme.lite")


def dyjsb_task_open_daily_box():
    """开宝箱任务"""
    # 点击“赚钱”按钮
    tap_text_center_on_screen("赚钱", 8, 8, device)
    # 点击“开宝箱得金币”按钮
    tap_text_center_on_screen("开宝箱得金币", 8, 8, device)
    # 点击“看广告视频再赚”按钮
    tap_text_center_on_screen("看广告视频再赚", 2, 2, device)

    # 执行广告相关操作
    dyjsb_advance()

    print("退出")


def dyjsb_task_advance():
    """看广告任务"""
    # 点击“赚钱”按钮
    tap_text_center_on_screen("赚钱", 8, 8, device)
    # 向上滑动屏幕
    swipe_direction(1)

    # 截取屏幕截图
    take_screenshot(1, 1, device)
    center = get_text_center_from_screenshot("领取奖励", 1, 1, device)
    if center:
        # 执行广告相关操作
        dyjsb_advance()

    # 向上滑动退出
    swipe_direction(4)
    print("退出")


def dyjsb_advance():
    """等待广告视频播放完成"""
    # 等待广告视频播放完成
    time.sleep(AD_WAIT_TIME)

    swipe_direction(4)
    time.sleep(4)

    swipe_direction(4)

    # 截取屏幕截图
    take_screenshot(1, 1, device)
    center = get_text_center_from_screenshot("领取奖励", 1, 1, device)
    while center:
        print("找到领取奖励")
        tap(center[0], center[1])

        # 等待广告视频播放完成
        time.sleep(AD_WAIT_TIME - 1)

        # 退出广告
        swipe_direction(4)
        time.sleep(6.6)
        swipe_direction(4)

        # 截取屏幕截图
        take_screenshot(1, 1, device)
        center = get_text_center_from_screenshot("领取奖励", 1, 1, device)

    # 点击“收下金币”按钮
    tap_text_center_on_screen("收下金币", 2, 2, device)

    # 返回主页
    swipe_direction(4)

    time.sleep(2.14)


def dyjsb_keep_account():
    """活跃账号任务"""
    # 点击直播间
    tap(125, 347)

    # 等待 13.5 到 15.5 分钟
    time_to_wait = random.uniform(15.5 * 60, 17.5 * 60)
    time.sleep(time_to_wait)

    # 退出直播间
    swipe_direction(4)


def dyjsb_keep_account_lookShortVideo(num):
    """养号操作:看短视频"""
    # # 进入精选页面
    # tap_text_center_on_screen("首页", 8, 8, device)

    max_swipes = int(num * (12.5 + 3 * random.uniform(1, 2.5)))
    print(f"执行养号操作, 本轮次数为:{max_swipes}")

    time.sleep(1.42)
    for i in range(max_swipes):
        swipe((646, 1425), (376, 347), random.uniform(0.3, 0.62))

        wait_time = random.uniform(10, 20)

        # 截取屏幕截图
        take_screenshot(4, 4, device)
        center = get_text_center_from_screenshot("广告", 4, 4, device)
        if center:
            # # 如果是广告，进行点赞操作
            # tap(1007,1360)
            # print("点赞操作")
            wait_time = random.uniform(40, 55) + 15

        time.sleep(wait_time)
        print(f"养号操作进度: {i + 1}/{max_swipes}  等待时间为: {wait_time}")

    print("养号操作结束")


def dyjsb_task_open_liveStream_box():
    """打开直播宝箱任务"""
    # 截取屏幕截图
    take_screenshot(2, 2, device)
    center = get_text_center_from_screenshot("领金币", 2, 2, device)
    if not center:
        print("未找到领金币")
        return

    print("找到领金币")
    tap(center[0], center[1])
    time.sleep(2.94)

    # 点击“开宝箱”按钮
    tap_text_center_on_screen("开宝箱", 2, 2, device)
    time.sleep(2.43)

    # 点击屏幕坐标(540, 1726)
    tap(540, 1726)
    # 等待1.14秒
    time.sleep(2.14)

    # 退出开宝箱
    swipe_direction(4)
    time.sleep(2.14)
    print("退出开宝箱")


def main():
    """主函数"""
    global device
    device = adb.device()  # 获取连接的设备

    # while True:
    #     # multi_tap(600, 600, 800, 800, 35)
    #     dyjsb_task_open_liveStream_box()
    #     # time.sleep(random.uniform(33,36))
    #     time.sleep(random.uniform(3.02, 3.2) * 60 )

    while True:
        dyjsb_keep_account_lookShortVideo(10)


if __name__ == "__main__":
    main()
