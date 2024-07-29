import random
import re
import time

import easyocr
from PIL import Image

from tools.adb import tap, adb_command

# 定义全局变量，用于存储 OCR 读取器实例
_reader = None


def get_ocr_reader():
    """懒加载 OCR 读取器"""
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(['ch_sim', 'en'])
    return _reader


def take_screenshot(num_parts, part_index, device):
    """使用 adb 命令获取屏幕截图，并截取特定部分"""
    # 等待一段时间以确保截图操作完成
    time.sleep(1.89)

    # 使用 adb 命令获取屏幕截图，并保存到设备的存储中
    device.shell('screencap -p /sdcard/screenshot.png')
    # 将设备中的截图文件拉取到本地
    device.sync.pull('/sdcard/screenshot.png', f'data/{device.serial}/screenshot.png')

    # 打开本地保存的截图文件
    with Image.open(f'data/{device.serial}/screenshot.png') as img:
        # 获取截图的宽度和高度
        width, height = img.size
        # 计算每个部分的高度
        part_height = height // num_parts
        # 计算当前部分的顶部和底部位置
        top = part_height * (part_index - 1)
        bottom = top + part_height

        # 确保 bottom 不超过图片高度
        if bottom > height:
            bottom = height

        # 截取当前部分的图像
        part_img = img.crop((0, top, width, bottom))
        print(top, width, bottom)
        # 将截取的部分保存为新截图文件
        part_img.save(f'data/{device.serial}/screenshot_part.png')

    # 等待一段时间以确保截图操作完成
    time.sleep(1.14)


def get_text_center_from_screenshot(search_text, num_parts, part_index, device):
    """截取屏幕并查找指定文本的中心点。"""
    center = find_text_center_ocr(search_text, 2400, num_parts, part_index, device)
    return center


def get_text_data_from_screenshot(num_parts, part_index, device):
    """获取截图中的文本数据"""
    # 读取截图中的文本数据
    image_path = f'screenshot_part.png'
    text_data = analyze_screenshot(image_path, device)
    return text_data


def calculate_text_center(left, top, width, height, original_height, num_parts, part_index):
    """计算目标文本的中心坐标"""
    center_x = int(left + width / 2)
    center_y = int(top + height / 2)

    # 调整坐标，因截图只包含特定部分
    center_y += (part_index - 1) * (original_height // num_parts)

    return center_x, center_y


def find_text_center(text_data, target_text, original_height, num_parts, part_index):
    """在 text_data 中查找目标文本的中心坐标"""
    for i, text in enumerate(text_data['text']):
        if target_text in text:
            # # 找到目标文本在当前文本中的起始位置
            # start_index = text.index(target_text)
            #
            # # 计算文本参数，以便计算中心坐标
            # left = text_data['left'][i] + (text_data['width'][i] * start_index / len(text))
            # width = text_data['width'][i] * len(target_text) / len(text)

            left = text_data['left'][i]
            width = text_data['width'][i]
            top = text_data['top'][i]
            height = text_data['height'][i]

            return calculate_text_center(left, top, width, height, original_height, num_parts, part_index)

    return None


def find_text_center_ocr(target_text, original_height, num_parts, part_index, device):
    """使用 EasyOCR 查找目标文本的中心坐标"""
    image_path = f'data/{device.serial}/screenshot_part.png'

    reader = get_ocr_reader()
    results = reader.readtext(image_path)

    for bbox, text, _ in results:
        if target_text in text:
            # 计算中心坐标
            center_x = int((bbox[0][0] + bbox[2][0]) / 2)
            center_y = int((bbox[0][1] + bbox[2][1]) / 2)

            # 调整坐标，因截图只包含特定部分
            center_y += (part_index - 1) * (original_height // num_parts)

            return center_x, center_y
    return None


def analyze_screenshot(image_path, device):
    """分析截图中的文本并返回坐标。"""
    reader = get_ocr_reader()
    results = reader.readtext(f'data/{device.serial}/{image_path}')
    text_data = {'text': [], 'left': [], 'top': [], 'width': [], 'height': []}

    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        text_data['text'].append(text)
        text_data['left'].append(top_left[0])
        text_data['top'].append(top_left[1])
        text_data['width'].append(top_right[0] - top_left[0])
        text_data['height'].append(bottom_left[1] - top_left[1])

    return text_data


def random_offset(value, offset=30):
    """为给定值增加一个随机偏移量。"""
    return value + random.randint(-offset, offset)


def tap_text_center_on_screen(search_text, num_parts, part_index, device):
    """截取屏幕并查找指定文本的中心点，然后点击"""
    take_screenshot(num_parts, part_index, device)
    center = find_text_center_ocr(search_text, 2400, num_parts, part_index, device)
    if center:
        print(f"找到'{search_text}'按钮，位置: {center}")
        reward_x, reward_y = center
        tap(reward_x, reward_y)
        time.sleep(2.25)
    else:
        print(f"未找到'{search_text}'按钮")


def is_app_in_foreground(package_name):
    """检测指定包名的应用是否在前台运行。"""
    output = adb_command('shell dumpsys activity activities | grep mResumedActivity')
    return package_name in output


def get_current_package_name():
    """获取当前前台运行的应用包名。"""
    output = adb_command('shell dumpsys activity activities | grep mResumedActivity')
    match = re.search(r'(?<=u0\s)[^/]+', output)
    if match:
        return match.group(0)
    return None
