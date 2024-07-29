import random
import re
import subprocess
import time
import xml.etree.ElementTree as ET


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


def swipe(start, end, duration):
    """在设备屏幕上执行滑动操作。"""
    adb_command(f'shell input swipe {start[0]} {start[1]} {end[0]} {end[1]} {int(duration * 1000)}')


def swipe_direction(num):
    """根据给定的数字执行相应的滑动操作。"""
    """1: 上滑, 2: 下滑, 3: 左滑, 4: 右滑"""
    if num == 1:
        swipe((606, 2370), (657, 1920), 0.3)
    elif num == 2:
        swipe((630, 47), (672, 273), 0.3)
    elif num == 3:
        swipe((1001, 993), (679, 1007), 0.3)
    elif num == 4:
        swipe((14, 1534), (408, 1534), 0.3)
    else:
        print("无效的滑动方向")

    time.sleep(1.34)


def open_app(package_name):
    """打开指定包名的应用"""
    subprocess.run(["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"])
    time.sleep(3.5)


def close_app(package_name):
    """关闭指定包名的应用"""
    subprocess.run(["adb", "shell", "am", "force-stop", package_name])
    time.sleep(1.15)


def wake_screen():
    """唤醒设备屏幕。"""
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_WAKEUP"])
    time.sleep(1.42)


def turn_off_screen():
    """熄灭屏幕"""
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_SLEEP"])
    time.sleep(1.09)


def get_page_source():
    """获取当前页面的源代码并解析为 XML 结构。"""
    xml_str = adb_command('shell uiautomator dump /dev/tty')
    xml_str = xml_str[xml_str.find('<?xml'):]  # 去除无效字符
    return ET.fromstring(xml_str)


def get_element_info(element):
    """获取元素的详细信息，包括坐标、文本、资源ID等。"""
    info = {
        'resource_id': element.attrib.get('resource-id', ''),
        'text': element.attrib.get('text', ''),
        'bounds': element.attrib.get('bounds', ''),
        'class': element.attrib.get('class', '')
    }
    info['center'] = get_center(info['bounds'])
    return info


def get_all_elements_info():
    """获取当前页面所有元素的详细信息。"""
    root = get_page_source()
    elements_info = [get_element_info(elem) for elem in root.iter('node')]
    return elements_info


def multi_tap(top_left_x, top_left_y, bottom_right_x, bottom_right_y, tap_count):
    """在指定区域内随机位置连点指定次数"""
    for _ in range(tap_count):
        x = random.randint(top_left_x, bottom_right_x)
        y = random.randint(top_left_y, bottom_right_y)
        tap(x, y)
        time.sleep(random.uniform(0.085, 0.15))  # 每次点击之间稍作等待，避免过快点击导致问题

