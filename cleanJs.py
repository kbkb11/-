import jsbeautifier
import os
import io


def format_js_file(input_file_path, output_file_path):
    try:
        # 读取原始 JavaScript 文件
        with io.open(input_file_path, 'r', encoding='utf-8') as file:
            js_code = file.read()

        # 配置 jsbeautifier
        beautifier_options = jsbeautifier.default_options()
        beautifier_options.indent_size = 2
        beautifier_options.indent_with_tabs = False
        beautifier_options.max_preserve_newlines = 2

        # 格式化 JavaScript 代码
        formatted_js_code = jsbeautifier.beautify(js_code, beautifier_options)

        # 将格式化后的代码写入新文件
        with io.open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_js_code)

        print(f"文件已成功格式化并保存到: {output_file_path}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 输入文件路径和输出文件路径
    input_file_path = r'D:\application\wechat-applet-reverse-tool-master\小程序包解密\wxpack\wxab7430e6e8b9a4ab\app-service.js'
    output_file_path = r'D:\application\wechat-applet-reverse-tool-master\小程序包解密\wxpack\wxab7430e6e8b9a4ab\temp.js'

    # 检查输入路径是否有效
    if not os.path.isfile(input_file_path):
        print("输入的文件路径无效。")
    else:
        format_js_file(input_file_path, output_file_path)
