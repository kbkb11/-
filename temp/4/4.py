import time
import random
from adbutils import adb
import subprocess
import easyocr
from PIL import Image


from PIL import Image
import easyocr
import adbutils

def take_screenshot(num_parts, part_index):
    """使用 adb 命令获取屏幕截图，并截取特定部分"""
    device.shell('screencap -p /sdcard/screenshot.png')
    device.sync.pull('/sdcard/screenshot.png', 'screenshot.png')

    # 打开截图并截取特定部分
    with Image.open('screenshot.png') as img:
        width, height = img.size
        part_height = height // num_parts
        top = part_height * (part_index - 1)
        bottom = top + part_height
        part_img = img.crop((0, top, width, bottom))
        part_img.save('screenshot.png')

    return 'screenshot.png', height

def find_text_center_ocr(image_path, target_text, original_height, num_parts, part_index):
    """使用 EasyOCR 查找目标文本的中心坐标"""
    reader = easyocr.Reader(['ch_sim', 'en'])
    results = reader.readtext(image_path)

    for bbox, text, _ in results:
        if target_text in text:
            # 计算中心坐标
            center_x = int((bbox[0][0] + bbox[2][0]) / 2)
            center_y = int((bbox[0][1] + bbox[2][1]) / 2)

            # 调整坐标，因截图只包含特定部分
            center_y += (part_index - 1) * (original_height // num_parts)

            return (center_x, center_y)
    return None



def random_offset(coord, offset=5):
    """添加随机偏移量以模拟人类点击"""
    return coord + random.randint(-offset, offset)


def tap(x, y):
    """使用 adb 命令模拟点击操作"""
    device.shell(f'input tap {x} {y}')


def adb_command(command):
    """执行 adb 命令"""
    result = subprocess.run(['adb'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')


def swipe(start, end, duration):
    """模拟滑动操作"""
    x1, y1 = start
    x2, y2 = end
    adb_command(f'shell input swipe {x1} {y1} {x2} {y2} {int(duration * 1000)}')


def exit_advance():
    """退出"""
    swipe((14,1534),(408,1534), 0.3)

def perform_actions():
    """执行一系列自动化操作"""
    print("开始执行操作")
    swipe((500, 1500), (500, 500), 0.5)
    while True:
        # 点击立即领取
        print("获取截图...")
        screenshot, original_height = take_screenshot(2, 2)
        print("查找'立即领取'按钮...")
        center = find_text_center_ocr(screenshot, '立即领取', 2300, 2, 2)
        if center:
            print(f"找到'立即领取'按钮，位置: {center}")
            tap(*map(random_offset, center))
            time.sleep(random.uniform(0.5, 1.5))
        else:
            print("未找到'立即领取'按钮")
            return
        time.sleep(random.uniform(33.5, 35.5))

        # 退出
        print("执行退出操作")
        exit_advance()
        time.sleep(random.uniform(0.8, 1.2))

        while True:
            # 点击领取奖励
            print("获取截图...")
            screenshot, original_height = take_screenshot(2, 2)
            print("查找'领取奖励'按钮...")
            center = find_text_center_ocr(screenshot, '领取奖励', 2300, 2, 2)
            if center:
                print(f"找到'领取奖励'按钮，位置: {center}")
                tap(*map(random_offset, center))
                time.sleep(random.uniform(30.5, 32))

                # 退出
                print("执行退出操作")
                exit_advance()
                time.sleep(random.uniform(3.5, 5.5))
            else:
                print("未找到'领取奖励'按钮")
                break


def main():
    global device
    device = adb.device()  # 获取连接的设备
    perform_actions()


if __name__ == "__main__":
    main()
