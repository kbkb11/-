import zipfile
import os
import xml.etree.ElementTree as ET


def extract_saz(saz_file, output_folder):
    """
    解压 .saz 文件到指定文件夹
    """
    with zipfile.ZipFile(saz_file, 'r') as zip_ref:
        zip_ref.extractall(output_folder)


def parse_and_print_sessions(folder_path):
    """
    解析解压后的 XML 文件并打印所有会话
    """
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()

            print(f'Parsing file: {filename}')

            for session in root.findall('.//session'):
                request_url = session.find('.//request/url').text if session.find(
                    './/request/url') is not None else 'N/A'
                request_method = session.find('.//request/method').text if session.find(
                    './/request/method') is not None else 'N/A'
                response_status = session.find('.//response/status').text if session.find(
                    './/response/status') is not None else 'N/A'

                print(f'URL: {request_url}')
                print(f'Method: {request_method}')
                print(f'Response Status: {response_status}')
                print('-' * 40)


def main():
    saz_file = '1.saz'  # 修改为你的 .saz 文件路径
    output_folder = r'D:\begin\code\script\robot\jd_robot\jd_fiddler'  # 修改为你希望解压到的文件夹路径

    # 解压 .saz 文件
    extract_saz(saz_file, output_folder)

    # 解析并打印会话
    parse_and_print_sessions(output_folder)


if __name__ == "__main__":
    main()
