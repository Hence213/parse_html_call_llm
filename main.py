
from get_url import get_url
url = "https://electrical-engineering-portal.com/connecting-generator-sets-low-voltage-system"
response = get_url(url)

if response is not None:
    from parse_html import parse_news_page
    result = parse_news_page(response)

    from common import write_text_to_file
    write_text_to_file(result, 'output2.txt')

