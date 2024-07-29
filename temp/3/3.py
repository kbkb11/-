import yaml
import time
import random
import subprocess
import re
import xml.etree.ElementTree as ET
from appium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
import easyocr  # 添加了 easyocr 依赖

# 全局变量
driver = None


def adb_command(command):
    """执行 adb 命令并返回其输出。"""
    result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def tap(x, y):
    """在设备屏幕上的指定坐标处执行点击操作。"""
    adb_command(f'shell input tap {x} {y}')


def get_center(bounds):
    """计算并返回一个元素的中心点坐标。"""
    match = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', bounds)
    if match:
        left, top, right, bottom = map(int, match.groups())
        return (left + right) // 2, (top + bottom) // 2
    return None


def get_layout():
    """获取当前页面的 XML 布局。"""
    global driver
    try:
        return driver.page_source
    except InvalidSessionIdException as e:
        print("会话已终止或未启动:", e)
        return None


def analyze_screenshot(image_path):
    """分析截图中的文本并返回坐标。"""
    reader = easyocr.Reader(['ch_sim', 'en'])  # 初始化 OCR 读取器
    results = reader.readtext(image_path)
    text_data = {'text': [], 'left': [], 'top': [], 'width': [], 'height': []}

    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        text_data['text'].append(text)
        text_data['left'].append(top_left[0])
        text_data['top'].append(top_left[1])
        text_data['width'].append(top_right[0] - top_left[0])
        text_data['height'].append(bottom_left[1] - top_left[1])

    return text_data


def find_text_center_ocr(text_data, search_text):
    """查找指定文本中心点的函数。"""
    for i, text in enumerate(text_data['text']):
        if text == search_text:
            x = (text_data['left'][i] + text_data['left'][i] + text_data['width'][i]) // 2
            y = (text_data['top'][i] + text_data['top'][i] + text_data['height'][i]) // 2
            return x, y
    return None


def get_text_center_from_screenshot(search_text):
    """截取屏幕并查找指定文本的中心点。"""
    screenshot_path = "screenshot.png"  # 需要提供截图路径
    adb_command(f'shell screencap -p /sdcard/{screenshot_path}')
    adb_command(f'pull /sdcard/{screenshot_path} .')
    text_data = analyze_screenshot(screenshot_path)
    center = find_text_center_ocr(text_data, search_text)
    return center


def find_text_center_appium(text, retries=2, delay=2):
    """使用 Appium 查找指定文本的中心点，重试指定次数并在每次之间延迟。"""
    for attempt in range(retries):
        layout_str = get_layout()
        if not layout_str:
            time.sleep(delay)
            continue
        try:
            root = ET.fromstring(layout_str)
        except ET.ParseError:
            time.sleep(delay)
            continue
        for elem in root.iter():
            if 'text' in elem.attrib and elem.attrib['text'] == text:
                if 'bounds' in elem.attrib:
                    return get_center(elem.attrib['bounds'])
        time.sleep(delay)
    return None


def find_text_tap(text, use_ocr=False):
    """查找指定文本并在其位置执行点击操作。"""
    if use_ocr:
        center = get_text_center_from_screenshot(text)
    else:
        center = find_text_center_appium(text)

    if center:
        tap(*map(random_offset, center))
    time.sleep(random.uniform(1, 1.2))


def random_offset(value, offset=30):
    """为给定值增加一个随机偏移量。"""
    return value + random.randint(-offset, offset)


def swipe(start, end, duration):
    """在设备屏幕上执行滑动操作。"""
    adb_command(f'shell input swipe {start[0]} {start[1]} {end[0]} {end[1]} {int(duration * 1000)}')


def setup_driver():
    global driver

    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    """设置并返回 Appium 驱动程序。"""
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': config['platformVersion'],
        'deviceName': 'device1',
        'automationName': 'UiAutomator2',
        'unicodeKeyboard': True,
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    time.sleep(2.46)


def init():
    """初始化应用状态。"""
    for _ in range(2):
        swipe((500, 1000), (500, 2000), 0.58)
    time.sleep(1.5)
    swipe((500, 1500), (500, 500), 0.58)
    swipe((500, 1500), (500, 500), 0.58)


def live_stream():
    """处理直播操作。"""
    print("进入直播页面")
    time.sleep(random.uniform(35, 37.5))
    tap(1017, 157)

    reward_text = "领取奖励"
    center = find_text_center_appium(reward_text)
    if center:
        reward_x, reward_y = center
        tap(random_offset(reward_x), random_offset(reward_y))
        print(f"点击 '{reward_text}' 在 ({reward_x}, {reward_y})")
        time.sleep(random.uniform(65, 68))
        tap(1017, 157)
        print("进入直播点击右上角的关闭按钮")

    find_text_tap("放弃奖励", use_ocr=True)
    find_text_tap("退出直播间", use_ocr=True)
    tap(531, 1448)


def keep_account(num):
    """养号操作。"""
    max_swipes = int(num * (15 + 3 * random.uniform(1, 2.5) - 0.5))
    print(f"执行养号操作, 本轮次数为:{max_swipes}")

    tap(94, 2336)
    time.sleep(1.42)
    for i in range(max_swipes):
        swipe((646, 2025), (376, 347), 0.58)
        time.sleep(4 + random.uniform(0.5, 1.5))
        print(f"养号操作进度: {i + 1}/{max_swipes}")

    tap(750, 2333)
    time.sleep(1.23)
    print("返回赚钱页面")


def perform_actions():
    setup_driver()

    while True:
        tap(903, 999)
        time.sleep(random.uniform(30.5, 32))
        # 退出
        tap(999, 134)
        time.sleep(random.uniform(0.8, 1.2))

        # 点击领取奖励
        center = find_text_center_appium("领取奖励")
        if center:
            tap(*map(random_offset, center))
            time.sleep(random.uniform(30.5, 32))

        #退出
        tap(999, 134)
        time.sleep(random.uniform(3.5, 5.5))


def main():
    init()
    perform_actions()


if __name__ == "__main__":
    main()
