import re
import requests
import json
import pandas as pd
import pymysql

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yhp0825sx',
    'database': 'busquerysystem'
}


def load_bus_names_from_db(dbName, rePattern):
    try:
        # 连接到数据库
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        cursor = connection.cursor()
        cursor.execute(f"SELECT routeName FROM {dbName}")
        bus_names = cursor.fetchall()

        # 正则表达式，用于匹配符合“数字+路”格式的线路名称
        pattern = re.compile(rePattern)

        # 过滤并返回匹配的“数字+路”部分
        valid_bus_names = []
        for name in bus_names:
            match = pattern.findall(name[0])
            if match:
                valid_bus_names.extend(match)

        return valid_bus_names

    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()


def Bus_inf(city, line):
    url = 'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=e522b9ecc3ab612e8e1299888a5ab313&jscode=a7c47146178d0b9f150ab8d2aecb98a2&output=json&city={}&offset=1&keywords={}&platform=JS'.format(
        city, line)
    try:
        r = requests.get(url).text
        rt = json.loads(r)
        if rt.get('buslines') and rt['buslines']:
            busline = rt['buslines'][0]
            dt = {
                'line_name': busline['name'],  # 公交线路名字
                'start_stop': busline['start_stop'],  # 始发站
                'end_stop': busline['end_stop'],  # 终点站
                'bounds': busline['bounds'],  # 行车区间
                'distance': busline['distance'],  # 全程长度
                'station_name': [],  # 沿途站点名
                'station_coords': [],  # 沿途站点坐标
                'station_sequence': [],  # 沿途站点第几站
            }

            # 获取沿途站点站名、对应坐标和“第几站”信息
            for st in busline['busstops']:
                dt['station_name'].append(st['name'])
                dt['station_coords'].append(st['location'])
                dt['station_sequence'].append(st['sequence'])

            # 将dt转换为DataFrame，并将索引设置为当前公交线的索引（从1开始计数）
            return pd.DataFrame([dt], index=[len(all_buslines) + 1])
        else:
            return pd.DataFrame()  # 没有找到公交线路信息，返回空DataFrame
    except Exception as e:
        print(f"Error fetching bus info for line {line}: {e}")
        return pd.DataFrame()  # 读取数据失败，返回空DataFrame


def insert_data_into_db(df, connection):
    cursor = connection.cursor()
    for index, row in df.iterrows():
        # 查找或插入 cityStops
        for stop_name in row['station_name']:
            cursor.execute("""
                INSERT IGNORE INTO cityStops (province, city, stopName)
                VALUES (%s, %s, %s)
            """, ('江西', city, stop_name))

        for stop_name, stop_order in zip(row['station_name'], row['station_sequence']):
            cursor.execute("""
                INSERT INTO routeStops (routeId, stopName, stopOrder)
                VALUES (%s, %s, %s)
            """, (index, stop_name, stop_order))

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    city = '萍乡'  # 需要查询公交信息的城市
    all_buslines = pd.DataFrame()

    # 从数据库加载公交线路名称
    bus_name = load_bus_names_from_db('cityRoutes', r'\d+路')

    for i in bus_name:
        df_line = Bus_inf(city, i.strip())  # 去除线路名两侧的空格
        if not df_line.empty:  # 如果DataFrame不为空（即成功获取了线路信息）
            all_buslines = pd.concat([all_buslines, df_line])

    # 想知道有效公交线路数，可以直接从all_buslines的索引长度获取
    effective_bus_num = len(all_buslines.index)
    print(f"有效公交线路数为：{effective_bus_num}个")

    # 打印每条线路的站点名称
    for index, row in all_buslines.iterrows():
        print(f"\n线路 {row['line_name']} 的途径站点名称如下：")
        for station_name in row['station_name']:
            print(station_name)

    # 将数据写入 MySQL 数据库
    try:
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        insert_data_into_db(all_buslines, connection)
    finally:
        connection.close()
