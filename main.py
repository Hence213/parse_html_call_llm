from common import write_text_to_file, get_url_name, read_file, extract_html_files, extract_num_from_file
from get_url import get_url
from parse_html import parse_news_page, parse_domain_page

domain_folder = 'd:\\work_space\\01_code\\data_process\\domain_htmls'
html_files = extract_html_files(domain_folder)
#1 读取网页域名信息内容，保存为txt文件
for domain_path in html_files:
    num_html = extract_num_from_file(domain_path)
    if not  (int(num_html) in [96]):
        continue
    txt_folder_name = num_html + '_txt'
    html = read_file(domain_path)
    urls = parse_domain_page(html)
    for url in urls:
        response = get_url(url)
        if response is not None:
            result = parse_news_page(response)
            txt_name = get_url_name(url) + '.txt'
            write_text_to_file(result, txt_folder_name, txt_name)
        
#2 读取txt文件，调用DeepSeek API

