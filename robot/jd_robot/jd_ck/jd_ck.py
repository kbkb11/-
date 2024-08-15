import base64
import json
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 设置ChromeDriver路径
driver_path = r'D:\begin\tools\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)


def slow_typing(element, text, delay=0.1):
    """模拟慢速输入"""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


def login_jd(driver, username_str, password_str):
    """进入登录页面并输入用户名和密码"""
    driver.get('https://my.m.jd.com/')
    time.sleep(2)

    try:
        account_password_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'J_ping') and contains(text(), '账号密码登录')]"))
        )
        account_password_login_button.click()
    except Exception as e:
        print(f"Error clicking account password login button: {e}")
    time.sleep(2)

    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
    except Exception as e:
        print(f"Error locating username input field: {e}")
    time.sleep(2)

    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'pwd')

    slow_typing(username, username_str, delay=0.1)
    slow_typing(password, password_str, delay=0.1)

    try:
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'policy_tip-checkbox'))
        )
        checkbox.click()
    except Exception as e:
        print(f"Error clicking checkbox: {e}")
    time.sleep(2)

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn') and contains(@class, 'btn-active')]"))
        )
        login_button.click()
    except Exception as e:
        print(f"Error clicking login button: {e}")
    time.sleep(2)


def process_slider_images(driver):
    """处理滑块验证的图片，返回需要滑动的距离
    :param driver: WebDriver对象
    :return: 需要滑动的距离
    """
    try:
        # 等待滑块验证图片加载
        cpc_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'cpc_img'))
        )
        small_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'small_img'))
        )
        # 获取滑块验证图片的base64数据
        cpc_img_src = cpc_img.get_attribute('src')
        small_img_src = small_img.get_attribute('src')

        cpc_img_base64 = cpc_img_src.split(',')[1]
        small_img_base64 = small_img_src.split(',')[1]

        # 将base64数据解码并保存为图片文件
        cpc_img_data = base64.b64decode(cpc_img_base64)
        small_img_data = base64.b64decode(small_img_base64)

        with open("img/cpc_img.png", "wb") as f:
            f.write(cpc_img_data)
        with open("img/small_img.png", "wb") as f:
            f.write(small_img_data)

        # 读取图片并转换为灰度图
        cpc_bg = cv2.imread('img/cpc_img.png', 0)
        small_bg = cv2.imread('img/small_img.png', 0)

        # 对图片进行边缘检测
        cpc_edge = cv2.Canny(cpc_bg, 100, 200)
        small_edge = cv2.Canny(small_bg, 100, 200)

        # 将灰度图转换为RGB图
        full_bg = cv2.cvtColor(cpc_edge, cv2.COLOR_GRAY2RGB)
        template = cv2.cvtColor(small_edge, cv2.COLOR_GRAY2RGB)

        # 匹配模板，找到最佳匹配位置
        result = cv2.matchTemplate(full_bg, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 计算需要滑动的距离
        x_offset = max_loc[0] + 27
        print("需要滑动的x坐标是：", x_offset)

        return x_offset

    except Exception as e:
        print(f"Error processing slider images: {e}")
        return None


def get_track(distance):
    """
        根据偏移量和手动操作模拟计算移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 时间间隔
    t = 0.2
    # 初始速度
    v = 0

    while current < distance:
        if current < mid:
            a = random.uniform(2, 5)
        else:
            a = -(random.uniform(12.5, 13.5))
        v0 = v
        v = v0 + a * t
        x = v0 * t + 1 / 2 * a * t * t
        current += x

        if 0.6 < current - distance < 1:
            x = x - 0.53
            tracks.append(round(x, 2))

        elif 1 < current - distance < 1.5:
            x = x - 1.4
            tracks.append(round(x, 2))
        elif 1.5 < current - distance < 3:
            x = x - 1.8
            tracks.append(round(x, 2))

        else:
            tracks.append(round(x, 2))

    print(sum(tracks))
    return tracks


def move_slider(driver, x_offset):
    """按住并移动滑块到指定位置
    :param driver: WebDriver对象
    :param x_offset: 需要滑动的距离
    """
    try:
        # 找到滑块元素
        slider = driver.find_element(By.CLASS_NAME, 'move-img')

        # 获取滑动轨迹
        tracks = get_track(x_offset)

        # 执行滑动操作
        actions = ActionChains(driver, 50)
        actions.click_and_hold(slider).perform()

        for track in tracks:
            actions.move_by_offset(track, 0).perform()

        actions.move_by_offset(-3, 0).perform()
        time.sleep(random.uniform(0.5, 0.7))
        actions.move_by_offset(3, 0).perform()
        time.sleep(random.uniform(0.5, 0.7))

        actions.release().perform()

        time.sleep(3)  # 等待验证结果
    except Exception as e:
        print(f"Error moving slider: {e}")


def handle_slider(driver):
    """处理滑块验证
    :param driver: WebDriver对象
    """
    x_offset = process_slider_images(driver)
    if x_offset is not None:
        move_slider(driver, x_offset)


def get_cookies(driver, username):
    """获取Cookies并保存到本地文件"""
    try:
        cookies = driver.get_cookies()
        filename = f'{username}_cookies.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(cookies, file, ensure_ascii=False, indent=4)
        print(f"Cookies have been saved to {filename}")
    except Exception as e:
        print(f"Error getting cookies: {e}")


def main():
    # 从文件中读取账号和密码
    with open('accounts.json', 'r', encoding='utf-8') as file:
        accounts = json.load(file)

    sum = 0
    for account in accounts:
        sum += 1
        if sum != 1:
            continue
        username = account['username']
        password = account['password']

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        try:
            login_jd(driver, username, password)
            time.sleep(3)  # 确保页面加载完成
            # handle_slider(driver)
            # get_cookies(driver, username)
            time.sleep(2000)
        finally:
            driver.quit()


if __name__ == "__main__":
    main()
    # print(get_track(150))