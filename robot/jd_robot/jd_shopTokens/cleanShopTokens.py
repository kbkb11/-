import re

# 定义正则表达式模式
pattern = r"token=([0-9A-Za-z]+)"

# 读取文件内容
with open('shopToken.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 搜索匹配
matches = re.findall(pattern, content)

# 打印所有匹配结果并将它们写入本地文件
with open('matched_tokens.txt', 'w', encoding='utf-8') as output_file:
    for match in matches:
        output_file.write(match + '\n')

