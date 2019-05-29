import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
print(r.cookies)
for k, v in r.cookies.items():
    print(k + '=' + v)
