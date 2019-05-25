import urllib.request, urllib.parse

url = 'https://fanyi.baidu.com/v2transapi'
data = {}
data['from'] = 'en'
data['to'] = 'zh'
data['query'] = 'them'
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'
data['sign'] = '6855.326134'
data['token'] = 'c9b2f3ac016b7c60c1c3eddd5cdeb5ed'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

print(html)
