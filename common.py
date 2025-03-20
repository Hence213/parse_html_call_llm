def write_text_to_file(text, folder_path, file_name):
    try:
        # 创建文件夹
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    except Exception as e:
        print(f"文件夹 {folder_path} 创建失败: {e}")
    try:
        with open(folder_path + '/' + file_name, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"文本已成功写入 {file_name}")
    except Exception as e:
        print(f"写入文件时出现错误: {e}")
        
# Extract the part of the URL after '//' and before the next '/'
import re


def get_url_name(url):
    result = url.split("//", 1)[1] if "//" in url else ""
    if result == "":
        print("URL 格式错误")
    else:
        result = result.replace('/', '_')
    return result

# 读取 HTML 文件
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
import os
def get_txt_files(folder_path):
    txt_files = []
    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件是否以 .txt 结尾
            if file.endswith('.txt'):
                # 拼接完整的文件路径
                txt_files.append(os.path.join(root, file))
    # 按文件修改时间排序
    txt_files.sort(key=lambda x: os.path.getmtime(x))
    return txt_files

import os
import re

def extract_html_files(directory):
    items = os.listdir(directory)
    # 筛选出文件
    html_files = [os.path.join(directory, item) for item in items if (os.path.isfile(os.path.join(directory, item)) and item.endswith('.html'))]
    return html_files

def extract_num_from_file(file_path):
    # 提取文件名
    file_name = os.path.basename(file_path)
    # 使用正则表达式提取文件名中的数字
    matches = re.findall(r'\d+', file_name)
    return matches[0] if matches else None

def extract_txt_folder(directory):
    items = os.listdir(directory)
    # 筛选出文件夹
    folders = [os.path.join(directory, item) for item in items if (os.path.isdir(os.path.join(directory, item)) and item.endswith('_txt'))]
    return folders