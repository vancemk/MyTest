import requests
from requests.exceptions import RequestException


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.ip138.com",
    "User-Agent":" Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }




def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code == 200:
            #print(response.text)
            print(response.encoding)
            print(response.apparent_encoding)
            r=response.text
            print(requests.utils.get_encodings_from_content(r)[0])
            print(r)
        return None
    except RequestException:
        return None

def main():
    url = 'https://www.ip.cn/'
    get_one_page(url)

if __name__=='__main__':
        main()
