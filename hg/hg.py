import random
import time

from adbutils import adb
from tools.adb import tap, swipe_direction, swipe, wake_screen, open_app, close_app, turn_off_screen
from tools.layout import get_text_center_from_screenshot, take_screenshot, tap_text_center_on_screen

# 模块级别的广告等待时间全局变量
AD_WAIT_TIME = 50

# 设备对象
device = None


def hg_task_open_daily_box():
    """开宝箱任务"""
    # 进入“福利”页面
    tap_text_center_on_screen("福利", 8, 8, device)
    # 等待1.5秒
    time.sleep(1.5)
    # 点击“开宝箱得金币”按钮
    tap_text_center_on_screen("开宝箱得金币", 8, 8, device)
    # 点击“看广告视频再赚”按钮
    tap_text_center_on_screen("看视频最高再", 2, 2, device)

    # 执行广告相关操作
    hg_advance()


def hg_task_advance():
    """看广告任务"""
    # 进入“福利”页面
    tap_text_center_on_screen("福利", 8, 8, device)

    print("开始执行操作")

    # 向上滑动屏幕
    swipe((500, 1500), (500, 500), 0.5)

    # 点击“立即领取”按钮
    tap_text_center_on_screen("立即领取", 1, 1, device)

    # 执行广告相关操作
    hg_advance()

    # 向上滑动退出
    swipe_direction(4)
    print("退出")


def hg_advance():
    """等待广告视频播放完成"""
    print("等待广告视频播放完成...")

    # 等待广告视频播放
    time.sleep(AD_WAIT_TIME)

    # 向右滑动退出
    swipe_direction(4)
    time.sleep(4)

    # 截取屏幕截图
    take_screenshot(8, 8, device)
    # 获取“领取奖励”按钮在截图中的中心坐标
    center = get_text_center_from_screenshot("福利", 8, 8, device)
    if center:
        time.sleep(1.28)
        return

    swipe_direction(4)

    print("检查是否显示'领取奖励'")

    # 截取屏幕截图
    take_screenshot(2, 2, device)
    # 获取“领取奖励”按钮在截图中的中心坐标
    center = get_text_center_from_screenshot("领取奖励", 2, 2, device)
    while center:
        print("找到'领取奖励'，点击")
        tap(center[0], center[1])

        # 等待广告视频播放
        time.sleep(AD_WAIT_TIME + 1.5)

        # 截取屏幕截图
        take_screenshot(3, 2, device)
        center = get_text_center_from_screenshot("领取奖励", 2, 2, device)

    # 向上滑动退出
    swipe_direction(4)
    print("退出广告页面")
    time.sleep(1.46)


def hg_init():
    """初始化设备和应用"""
    global device
    # 获取连接的设备
    device = adb.device()

    # 唤醒设备
    wake_screen()
    # 向上滑动解锁屏幕
    swipe_direction(1)
    # 等待1.24秒
    time.sleep(1.24)

    # 打开红果免费短剧情应用
    open_app("com.phoenix.read")

    # 进入“福利”页面
    tap_text_center_on_screen("福利", 8, 8, device)

    # 等待2秒
    time.sleep(2)


def hg_switch_card():
    """翻卡任务"""
    # 点击“立即翻卡”按钮
    take_screenshot(1, 1, device)
    center = get_text_center_from_screenshot("立即翻卡", 1, 1, device)
    tap(center[0], center[1])
    time.sleep(5)

    # 点击“看视频翻十位卡”按钮
    tap_text_center_on_screen("翻十位卡", 1, 1, device)
    time.sleep(AD_WAIT_TIME)
    swipe_direction(4)
    time.sleep(random.uniform(1.5, 2.3))
    swipe_direction(4)

    # 点击“立即翻卡”按钮
    time.sleep(5)
    tap(center[0], center[1])

    # 点击“看视频翻百位卡”按钮
    tap_text_center_on_screen("翻百位卡", 1, 1, device)
    time.sleep(AD_WAIT_TIME)
    swipe_direction(4)
    time.sleep(random.uniform(1.5, 2.3))
    swipe_direction(4)

    # 点击“立即翻卡”按钮
    time.sleep(5)
    tap(center[0], center[1])

    # 点击“看视频翻千位卡”按钮
    tap_text_center_on_screen("翻千位卡", 1, 1, device)
    tap(542, 1688)
    time.sleep(AD_WAIT_TIME)
    swipe_direction(4)
    time.sleep(random.uniform(1.5, 2.3))
    swipe_direction(4)

    # 点击“立即翻卡”按钮
    time.sleep(5)
    tap(center[0], center[1])

    # 点击“开心收下”按钮
    tap_text_center_on_screen("开心收下", 1, 1, device)


def hg_task_watchTv(watch_time):
    """观看剧集任务"""
    # 进入“福利”页面
    tap_text_center_on_screen("福利", 8, 8, device)

    # 前往“去看剧”页面
    tap_text_center_on_screen("去看剧", 1, 1, device)

    # 等待指定时间
    time.sleep(watch_time)

    # 返回“赚钱”页面
    tap(979, 1490)


def main():
    global device
    device = adb.device()  # 获取连接的设备

    # hg_init()
    while True:
        hg_switch_card()


# def main():
#     global device
#     device = adb.device()  # 获取连接的设备
#
#     while True:
#         hg_task_open_daily_box()
#
#         time.sleep(random.uniform(0.8, 1.2) * 5)
#
#         hg_task_advance()


if __name__ == "__main__":
    main()
