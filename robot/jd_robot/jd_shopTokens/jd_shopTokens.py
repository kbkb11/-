import random
import time

from adbutils import adb

from tools.adb import tap
from tools.layout import take_screenshot, get_text_data_from_screenshot, calculate_text_center, \
    tap_text_center_on_screen

# 设备对象
device = None


def find_and_tap_http_links():
    """截屏，识别图像中的文本，找到以 http 开头的内容并点击"""
    # 截屏
    take_screenshot(1, 1, device)
    # 获取截图中的文本数据
    text_data = get_text_data_from_screenshot(1, 1, device)

    # 遍历文本数据，查找以 http 开头的内容并点击
    for i, text in enumerate(text_data['text']):
        if text.startswith('http'):
            # 计算目标文本的中心坐标
            left = text_data['left'][i]
            top = text_data['top'][i]
            width = text_data['width'][i]
            height = text_data['height'][i]

            center_x, center_y = calculate_text_center(left, top, width, height, 2400, 1, 1)

            print(f"找到坐标,{center_x},{center_y}")
            getToken(center_x, center_y)

            # # 点击目标文本的中心坐标
            # print(f"点击 http 链接: {text}, 位置: ({center_x}, {center_y})")
            # tap(center_x, center_y)
            # time.sleep(2.25)


def getToken(center_x, center_y):
    tap(center_x, center_y)
    time.sleep(random.uniform(0.6, 1.5))

    # 查看是否被风控，需要点击检测按钮
    tap_text_center_on_screen("快速验证", 1, 1, device)
    time.sleep(random.uniform(5.5, 7.5))

    tap_text_center_on_screen("签到有礼", 1, 1, device)
    time.sleep(random.uniform(4.5, 5.5))

    tap(59, 158)
    time.sleep(random.uniform(1.5, 2.5))
    print("退出该店铺签到任务")


if __name__ == '__main__':
    device = adb.device()  # 获取连接的设备

    find_and_tap_http_links()
