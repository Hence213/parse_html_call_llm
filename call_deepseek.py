# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from common import read_file
client = OpenAI(api_key="sk-xxxxxx", base_url="https://api.deepseek.com")
system_content = read_file("d:\\work_space\\01_code\\data_process\\promt_system_role.txt")

def call_deepseek(article):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": article},
        ],
        stream=False
    )

    return (response.choices[0].message.content)

import threading
class TimeoutException(Exception):
    pass
def timeout_handler(signum, frame):
    raise TimeoutException

def call_with_timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default
        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception as e:
                self.result = e
    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.is_alive():
        raise TimeoutException
    return it.result


from common import get_txt_files, write_text_to_file, extract_num_from_file, extract_txt_folder
import os
import time
if __name__ == '__main__':
    # 示例文件夹路径，你可以根据实际情况修改
    folder_txt_path = 'd:\\work_space\\01_code\\data_process'
    folder_paths = extract_txt_folder(folder_txt_path)
    for folder_path in folder_paths:
        output_num = extract_num_from_file(folder_path)
        if not  (int(output_num) in [96]):
            continue
        txt_files = get_txt_files(folder_path)
        resoults = ""
        for file_path in txt_files:
            article = read_file(file_path)
            file_name = os.path.basename(file_path)
            if len(file_name) < 30:
                file_name = file_name.rjust(30)
            else:
                file_name = file_name[:30]
            if len(article) < 50:
                resoults += f"{file_name}: 文本长度小于50，跳过\n"
                continue

            try:
                time.sleep(1)
                resoult = call_with_timeout(call_deepseek, args=(article,), timeout_duration=60)
                if isinstance(resoult, Exception):
                    raise resoult
            except TimeoutException:
                resoult = "调用超时，跳过"
                print(f"{file_name}: 调用超时")
            except Exception as e:
                resoult = f"调用出错: {e}"
                print(f"{file_name}: 调用出错: {e}")
            resoults += f"{file_name}: {resoult}\n"
        write_text_to_file(resoults, "output", f"{output_num}.txt")