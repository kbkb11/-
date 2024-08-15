from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pymysql
import time

# 设置ChromeDriver路径
driver_path = r'D:\begin\tools\chromedriver-win64\chromedriver.exe'

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yhp0825sx',
    'database': 'busquerysystem'
}


class BusLineScraper:
    def __init__(self):
        # 设置ChromeDriver路径
        self.service = Service(driver_path)
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
        # 连接数据库
        self.conn = pymysql.connect(**db_config)
        self.cursor = self.conn.cursor()

    def get_allBus_lines(self, url):
        try:
            # 初始化浏览器
            self.driver = webdriver.Chrome(service=self.service, options=self.options)

            # 访问页面
            self.driver.get(url)

            # 获取页面内容
            html_content = self.driver.page_source

            # 使用BeautifulSoup解析页面内容
            soup = BeautifulSoup(html_content, 'html.parser')

            # 查找<div class="list"><ul class="f-cb">中的数据
            list_div = soup.find('div', class_='list')
            bus_lines = []

            if list_div:
                ul = list_div.find('ul', class_='f-cb')
                if ul:
                    # 获取每个<li>元素中的<a>标签
                    lines = ul.find_all('li')
                    for line in lines:
                        a_tag = line.find('a')
                        if a_tag:
                            # 提取超链接和文本内容
                            link = a_tag['href']
                            name = a_tag.get_text(strip=True)
                            bus_lines.append({'name': name, 'link': link})
                else:
                    print("未找到<ul class='f-cb'>")
            else:
                print("未找到<div class='list'>")

            return bus_lines
        finally:
            # 关闭浏览器
            self.driver.quit()

    def get_oneBuss_line(self, url):
        try:
            # 初始化浏览器
            self.driver = webdriver.Chrome(service=self.service, options=self.options)

            # 访问页面
            self.driver.get(url)

            # 获取页面内容
            html_content = self.driver.page_source

            # 使用BeautifulSoup解析页面内容
            soup = BeautifulSoup(html_content, 'html.parser')

            # 查找<div class="gj01_line_site"><ul class="gj01_line_img JS-up clearfix">中的数据
            list_div = soup.find('div', class_='gj01_line_site')
            bus_lines = []

            if list_div:
                ul = list_div.find('ul', class_='gj01_line_img JS-up clearfix')
                if ul:
                    # 获取每个<li>元素
                    lines = ul.find_all('li')
                    for line in lines:
                        # 获取<li>中的文本内容并添加到列表
                        bus_lines.append(line.get_text(strip=True))
                else:
                    print("未找到<ul class='gj01_line_img JS-up clearfix'>")
            else:
                print("未找到<div class='gj01_line_site'>")

            return bus_lines
        finally:
            # 关闭浏览器
            self.driver.quit()

    def insert_bus_line(self, province, city, name, link):
        try:
            query = "INSERT INTO cityRoutes (province, city, routeName, link) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (province, city, name, link))
            self.conn.commit()
            return self.cursor.lastrowid
        except pymysql.MySQLError as err:
            print(f"Error: {err}")
            return None

    def insert_route_stops(self, route_id, stops):
        try:
            query = "INSERT INTO routeStops (routeId, stopName, stopOrder) VALUES (%s, %s, %s)"
            for order, stop in enumerate(stops, start=1):
                self.cursor.execute(query, (route_id, stop, order))
            self.conn.commit()
        except pymysql.MySQLError as err:
            print(f"Error: {err}")

    def insert_city_stop(self, province, city, stop_name):
        try:
            query = "INSERT IGNORE INTO cityStops (province, city, stopName) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (province, city, stop_name))
            self.conn.commit()
        except pymysql.MySQLError as err:
            print(f"Error: {err}")

    def close(self):
        self.cursor.close()
        self.conn.close()


# 使用示例
if __name__ == "__main__":
    # 创建爬虫实例
    scraper = BusLineScraper()

    # 目标URL
    url = 'http://pingxiang.gongjiao.com/lines_all.html'

    # 获取公交线路信息及其链接
    bus_lines = scraper.get_allBus_lines(url)

    # 省份和城市信息
    province = '江西省'
    city = '萍乡市'

    for line in bus_lines:
        print(f"线路名称: {line['name']}, 链接: {line['link']}")
        route_id = scraper.insert_bus_line(province, city, line['name'], line['link'])
        if route_id:
            # 获取线路详情
            bus_lines_details = scraper.get_oneBuss_line(line['link'])
            print(bus_lines_details)
            # 插入站点信息
            scraper.insert_route_stops(route_id, bus_lines_details)
            for stop in bus_lines_details:
                scraper.insert_city_stop(province, city, stop)
        print()

    # 关闭数据库连接
    scraper.close()
