import subprocess
import random
import time
from PIL import Image
import easyocr


# 截屏函数
def adb_screenshot():
    # 在手机上截屏并保存到 /sdcard/screen.png
    adb_command('shell screencap -p /sdcard/screen.png')
    # 将截图拉取到本地
    adb_command('pull /sdcard/screen.png .')
    return 'screen.png'


# 执行 adb 命令的函数
def adb_command(command):
    result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


# 分析截图中的文本并返回坐标
def analyze_screenshot(image_path):
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


# 打印所有文本和其坐标的函数
def print_all_text_coords(text_data):
    for i, text in enumerate(text_data['text']):
        x_center = (text_data['left'][i] + text_data['left'][i] + text_data['width'][i]) // 2
        y_center = (text_data['top'][i] + text_data['top'][i] + text_data['height'][i]) // 2
        print(f"'{text}' at ({x_center}, {y_center})")


# 查找指定文本中心点的函数
def find_text_center(text_data, search_text):
    for i, text in enumerate(text_data['text']):
        if text == search_text:
            x = (text_data['left'][i] + text_data['left'][i] + text_data['width'][i]) // 2
            y = (text_data['top'][i] + text_data['top'][i] + text_data['height'][i]) // 2
            return x, y
    return None


# 随机偏移函数
def random_offset(value, offset=30):
    return value + random.randint(-offset, offset)


# 点击函数
def tap(x, y):
    adb_command(f'shell input tap {x} {y}')


# 主函数
def main():
    search_text = "赚钱"

    # 截屏
    screenshot_path = adb_screenshot()

    # 分析截图
    text_data = analyze_screenshot(screenshot_path)

    # 打印所有文本和其坐标
    print("所有文本和其坐标：")
    print_all_text_coords(text_data)

    # 查找指定文本中心点
    center = find_text_center(text_data, search_text)
    if center:
        x, y = center
        print(f"找到 '{search_text}' 在 ({x}, {y})")
    else:
        print(f"未找到文本 '{search_text}'")


if __name__ == "__main__":
    main()
