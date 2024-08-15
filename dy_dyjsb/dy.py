import random
import time
from adbutils import adb
from tools.adb import wake_screen, swipe_direction, open_app, close_app, turn_off_screen, tap, swipe
from tools.layout import tap_text_center_on_screen, get_text_center_from_screenshot, take_screenshot

# 模块级别的广告等待时间全局变量
AD_WAIT_TIME = 37

# 设备对象
device = None


def dy_init():
    """初始化设备和应用"""
    global device
    device = adb.device()  # 获取连接的设备
    print("设备已连接")

    # 唤醒设备
    wake_screen()
    print("设备已唤醒")

    # 向上滑动解锁屏幕
    swipe_direction(1)
    print("屏幕已解锁")

    time.sleep(1.24)

    # 打开抖音
    open_app("com.ss.android.ugc.aweme")
    print("抖音已打开")


def dy_task_open_daily_box():
    """开宝箱任务"""
    print("开始开宝箱任务")

    # 进入推荐页面
    tap(872, 196)
    print("进入推荐页面")
    time.sleep(1.14)

    # 进入开宝箱页面
    tap(117, 352)
    print("进入开宝箱页面")
    time.sleep(1.54)

    # 点击“开宝箱得金币”按钮
    tap_text_center_on_screen("开宝箱得金币", 8, 8, device)
    # 点击“看广告视频再赚”按钮
    tap_text_center_on_screen("看广告视频再赚", 2, 2, device)

    # 执行广告相关操作
    dy_advance()

    print("退出开宝箱任务")


def dy_task_advance():
    print("开始广告任务")

    # 截取屏幕截图查找“去看看”按钮
    take_screenshot(1, 1, device)
    print("截取屏幕截图")
    center = get_text_center_from_screenshot("去看看", 1, 1, device)
    while center is None:
        # 执行滑动操作，持续时间0.58秒
        swipe((646, 1625), (376, 347), random.uniform(0.3, 0.62))
        print("执行滑动操作")

        # 截取屏幕截图查找“去看看”按钮
        take_screenshot(1, 1, device)
        print("再次截取屏幕截图")
        center = get_text_center_from_screenshot("去看看", 1, 1, device)

    # 点击广告按钮
    tap(center[0], center[1])

    # 执行广告相关操作
    dy_advance()

    # 向上滑动退出
    swipe_direction(4)
    print("退出广告任务")


def dy_advance():
    """等待广告视频播放完成"""
    print("等待广告视频播放完成")
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


def dy_keep_account_liveStream(liveStream_time):
    """养号操作:看直播"""
    print("开始活跃账号任务")

    # 进入关注页面
    tap(594, 186)
    print("进入关注页面")
    time.sleep(1.54)

    # 点击直播间
    tap(125, 347)
    print("点击进入直播间")

    # 等待
    time.sleep(random.uniform(liveStream_time * 60, (liveStream_time + 2) * 60))

    # 退出直播间
    swipe_direction(4)
    print("养号操作结束")


def dy_keep_account_lookShortVideo(num):
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


def dy_task_open_liveStream_box():
    """打开直播宝箱任务"""
    print("开始打开直播宝箱任务")

    # 点击“领金币”按钮
    tap_text_center_on_screen("领金币", 2, 2, device)
    # 点击“开宝箱”按钮
    tap_text_center_on_screen("开宝箱", 2, 2, device)

    time.sleep(2.43)

    # 点击屏幕坐标(540, 1726)
    tap(540, 1726)
    print("点击开宝箱的坐标位置")

    # 等待1.14秒
    time.sleep(1.14)

    # 退出开宝箱
    swipe_direction(4)
    # time.sleep(1.14)
    # swipe_direction(4)
    print("退出开直播宝箱任务")


def main():
    """主函数"""
    global device
    device = adb.device()  # 获取连接的设备
    print("设备已连接")

    # dy_task_advance()

    while True:
        # dy_task_open_liveStream_box()
        # time.sleep(3*60+10)
        dy_keep_account_lookShortVideo(10)



if __name__ == "__main__":
    main()
