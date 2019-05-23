import requests

r = requests.get('https://unsplash.com')
print(r.text)
