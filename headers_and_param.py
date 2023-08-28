import requests

url = "https://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0'}

pd = {'wd': '天线'}
response = requests.get(url, params=pd, headers=headers)
print(response.content.decode('utf-8'))
