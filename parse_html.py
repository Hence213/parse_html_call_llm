from bs4 import BeautifulSoup

def parse_news_page(html):
    """解析新闻页面核心函数"""
    soup = BeautifulSoup(html, 'lxml')
    result = ""

    try:
        # # 标题提取（优先找h1标签）
        # title = soup.find('h1', class_=lambda x: x and 'title' in x.lower())
        # if not title:
        #     title = soup.find('h1')
        # result['title'] = title.get_text(strip=True) if title else ''

        # 正文提取（定位内容容器）
        content_div = soup.find('div', class_=lambda x: x and 'main-content' in x.lower())
        if not content_div:
            content_div = soup.find('article') or soup.find('main')

        if content_div:
            
            # # 清理无关元素
            # for element in content_div(['img', 'style', 'iframe', 'nav', 
            #                           'footer', 'aside', 'button', 'form']):
            #     element.decompose()
            
            
            # 提取文本内容
            for p in content_div.find_all(['p', 'h1', 'h2', 'h3', 'h4']):
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
