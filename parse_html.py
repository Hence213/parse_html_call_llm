from bs4 import BeautifulSoup

def parse_news_page(html):
    """解析新闻页面核心函数"""
    soup = BeautifulSoup(html, 'lxml')
    result = ""

    try:
        # 提取标题和文本内容
        for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4']):
            text = p.get_text(separator=' ',strip=True)
            if text and len(text) > 5:  # 过滤短文本（可能是广告）
                result += text + '\n'
        # # 作者信息提取
        # author_tag = soup.find(class_=lambda x: x and 'author' in x.lower())
        # if author_tag:
        #     result['author'] = author_tag.get_text(strip=True).replace('作者：', '')

        # # 发布时间提取
        # time_tag = soup.find('time') or soup.find(class_=lambda x: x and 'date' in x.lower())
        # if time_tag:
        #     result['publish_time'] = time_tag.get('datetime') or time_tag.get_text(strip=True)

    except Exception as e:
        print(f"解析错误：{str(e)}")
    
    return result

# 使用示例
# 读取 HTML 文件
# with open('d:\\work_space\\01_code\\data_process\\output.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()
#     parse_news_page(html_content)

def parse_domain_page(html):
    """解析新闻页面核心函数"""
    soup = BeautifulSoup(html, 'lxml')
    result = []
    try:
        result = [a['href'] for a in soup.find_all('a', href=True)]
    except Exception as e:
        print(f"解析错误：{str(e)}")
    
    return result

if __name__ == '__main__':
    from common import read_file
    html = read_file('d:\\work_space\\01_code\\data_process\\domain1.html')
    resoult = parse_domain_page(html)
    print(resoult)