def write_text_to_file(text, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"文本已成功写入 {file_path}")
    except Exception as e:
        print(f"写入文件时出现错误: {e}")