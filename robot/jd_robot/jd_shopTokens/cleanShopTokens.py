import json
import re
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']


def read_file(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()


def parse_jsonp(jsonp_str):
    try:
        start_idx = jsonp_str.index('(') + 1
        end_idx = jsonp_str.rindex(')')
        if start_idx < end_idx:
            json_data = jsonp_str[start_idx:end_idx]
            return json.loads(json_data)
        else:
            raise ValueError("Invalid JSONP format: no data inside parentheses.")
    except ValueError as e:
        print(f"Error parsing JSONP string: {jsonp_str}")
        print(e)
        return None


def convert_to_target_format(data, index, shop_name):
    rules = []
    min_level = float('inf')
    max_level = float('-inf')

    for rule in data['data']['continuePrizeRuleList']:
        rule_info = {
            "days": rule['days'],
            "prize": [],
            "havePrize": rule['userPrizeRuleStatus'] == 1
        }

        for prize in rule['prizeList']:
            prize_info = f"{prize['discount']}京豆（共{int(prize['budgetNum'] / prize['discount'])}份{'已发完' if prize['userPirzeStatus'] != 1 else ''}）"
            rule_info['prize'].append(prize_info)

        rules.append(rule_info)

        if rule['days'] < min_level:
            min_level = rule['days']
        if rule['days'] > max_level:
            max_level = rule['days']

    parsed_data = {
        "index": index,
        "venderId": data['data']['venderId'],
        "shopName": shop_name,
        "activityId": data['data']['id'],
        "startTime": data['data']['startTime'],
        "endTime": data['data']['endTime'],
        "isValid": data['data']['activityStatus'] == 1,
        "rules": rules,
        "minLevel": min_level if min_level != float('inf') else 0,
        "maxLevel": max_level if max_level != float('-inf') else 3
    }

    return parsed_data


def extract_tokens():
    # 定义正则表达式模式
    pattern = r"token=([0-9A-Za-z]+)"

    # 读取文件内容
    content = read_file('data/shopToken.txt')

    # 搜索匹配
    matches = re.findall(pattern, content)

    # 打印所有匹配结果并将它们写入本地文件
    with open('data/matched_tokens.txt', 'w', encoding='utf-8') as output_file:
        for match in matches:
            output_file.write(match + '\n')

    return matches


def main():
    input_file = 'data/temp.json'
    output_file = 'data/parsed_data.json'
    shop_name = "悠采旗舰店"  # 假设的店铺名称，可以根据需要进行修改或从输入数据中提取
    index = 0  # 初始索引值，可以根据需要进行调整

    # 提取tokens
    shop_tokens = extract_tokens()

    # 读取temp.json文件内容
    jsonp_content = read_file(input_file)
    jsonp_lines = jsonp_content.splitlines()

    all_parsed_data = {}

    for x in range(0, len(jsonp_lines), 2):
        jsonp_str = jsonp_lines[x]
        data = parse_jsonp(jsonp_str)
        if data is not None:
            if index < len(shop_tokens):
                key = shop_tokens[index]
            else:
                key = " "
            all_parsed_data[key] = convert_to_target_format(data, index, shop_name)
            index += 1

    # 打印或保存解析后的数据
    parsed_json_str = json.dumps(all_parsed_data, ensure_ascii=False, indent=4)
    print(parsed_json_str)

    # 保存为文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(parsed_json_str)


if __name__ == "__main__":
    main()
