import base64

import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    # 打开京东登录页面
    driver.get('https://my.m.jd.com/')
    time.sleep(2)

    # 等待并点击账号密码登录按钮
    try:
        account_password_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'J_ping') and contains(text(), '账号密码登录')]"))
        )
        account_password_login_button.click()
    except Exception as e:
        print(f"Error clicking account password login button: {e}")
    time.sleep(2)

    # 等待用户名输入框出现
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
    except Exception as e:
        print(f"Error locating username input field: {e}")
    time.sleep(2)

    # 输入用户名和密码
    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'pwd')

    # 替换为您的京东用户名和密码，并控制输入速度
    slow_typing(username, username_str, delay=0.1)
    slow_typing(password, password_str, delay=0.1)

    # 点击阅读协议
    try:
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'policy_tip-checkbox'))
        )
        checkbox.click()
    except Exception as e:
        print(f"Error clicking checkbox: {e}")
    time.sleep(2)

    # 点击登录按钮
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn') and contains(@class, 'btn-active')]"))
        )
        login_button.click()
    except Exception as e:
        print(f"Error clicking login button: {e}")
    time.sleep(2)

def handle_slider(driver):
    """处理滑块验证"""
    try:
        # 获取滑块验证码图片的src属性
        cpc_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'cpc_img'))
        )
        small_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'small_img'))
        )
        cpc_img_src = cpc_img.get_attribute('src')
        small_img_src = small_img.get_attribute('src')

        # 去掉前缀 'data:image/png;base64,'
        cpc_img_base64 = cpc_img_src.split(',')[1]
        small_img_base64 = small_img_src.split(',')[1]

        # 解码
        cpc_img_data = base64.b64decode(cpc_img_base64)
        small_img_data = base64.b64decode(small_img_base64)

        # 将解码后的数据保存为文件
        with open("cpc_img.png", "wb") as f:
            f.write(cpc_img_data)
        with open("small_img.png", "wb") as f:
            f.write(small_img_data)

        # 读取图片
        cpc_bg = cv2.imread('cpc_img.png', 0)  # 读取为灰度图
        small_bg = cv2.imread('small_img.png', 0)  # 读取为灰度图

        # 识别图片边缘
        cpc_edge = cv2.Canny(cpc_bg, 100, 200)
        small_edge = cv2.Canny(small_bg, 100, 200)

        # 转换图片格式
        full_bg = cv2.cvtColor(cpc_edge, cv2.COLOR_GRAY2RGB)
        template = cv2.cvtColor(small_edge, cv2.COLOR_GRAY2RGB)

        # 使用模板匹配找到小图片在大图片中的位置
        result = cv2.matchTemplate(full_bg, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 获取滑动距离
        x_offset = max_loc[0] + 8
        print("需要滑动的x坐标是：", x_offset)

        # 找到滑块元素
        slider = driver.find_element(By.CLASS_NAME, 'move-img')

        # 设置滑动总时间和步骤
        steps = 5  # 增加步骤数以实现平滑滑动
        step_distance = x_offset / steps

        # 创建ActionChains对象
        actions = ActionChains(driver)

        # 点击并按住滑块
        actions.click_and_hold(slider).perform()

        # 匀速滑动滑块
        for i in range(steps):
            actions.move_by_offset(step_distance, 0)
            actions.perform()

        # 释放滑块
        actions.release().perform()

        time.sleep(1000)
    except Exception as e:
        print(f"Error handling slider: {e}")


def get_cookies(driver):
    """获取Cookies"""
    try:
        cookies = driver.get_cookies()
        for cookie in cookies:
            print(f"{cookie['name']}={cookie['value']}")
    except Exception as e:
        print(f"Error getting cookies: {e}")


def main(username, password):
    # 初始化WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 可选，隐藏浏览器界面
    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_jd(driver, username, password)
        handle_slider(driver)
        get_cookies(driver)
    finally:
        # 关闭WebDriver
        driver.quit()


if __name__ == "__main__":
    # 在这里替换为您的京东用户名和密码
    username = 'your_jd_username'
    password = 'your_jd_password'
    main(username, password)
