import cloudscraper

# url = "这里替换为你要请求的实际URL"

def get_url(url):
    resoult = ""
    try:
    # 创建云爬虫对象
        scraper = cloudscraper.create_scraper()
    # 发起 GET 请求
        response = scraper.get(url)
    # 检查响应状态码
        response.raise_for_status()
        print("请求成功")
        resoult = response.text
    except cloudscraper.exceptions.CloudflareChallengeError as cce:
        print(f"遇到 Cloudflare 挑战错误: {cce}")
    except cloudscraper.exceptions.CloudflareCode1020 as cce1020:
        print(f"遇到 Cloudflare 1020 错误: {cce1020}")
    except cloudscraper.exceptions.CloudflareIUAMError as iuae:
        print(f"遇到 Cloudflare IUAM 错误: {iuae}")
    except cloudscraper.exceptions.CaptchaTimeout as cte:
        print(f"请求 Cloudflare 超时: {cte}")
    except cloudscraper.exceptions.CaptchaException as ce:
        print(f"遇到 Cloudflare 通用错误: {ce}")
    except Exception as e:
        print(f"发生未知错误: {e}")
        
    return resoult

# get_url(url)