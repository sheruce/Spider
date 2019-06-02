import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookies': 'SUV=00FFA503ABDD86615CE3A45242D40837; IPLOC=CN5101; SUID=6186DDAB3020910A000000005CE91F0D; SNUID=D3441D14C0BA35A54DCF2B83C0AEE869; ld=Rkllllllll2tfSD2lllllV8sCHklllll$dLpYyllllGlllll4klll5@@@@@@@@@@; LSTMV=529%2C186; LCLKINT=1376; ABTEST=7|1559463424|v1; weixinIndexVisited=1; JSESSIONID=aaaLO3eZbbSa_ei39OgRw; ppinf=5|1559464625|1560674225|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3OlVuaWNvcm58Y3J0OjEwOjE1NTk0NjQ2MjV8cmVmbmljazo3OlVuaWNvcm58dXNlcmlkOjQ0Om85dDJsdUwyVHlab1F6UG1sdzA1WHdhdkpHNU1Ad2VpeGluLnNvaHUuY29tfA; pprdig=QvRyo-iINTc6s9h8cWj3B1jQkjoiv7IdVAqITkbteVYPKO9gAn5IZaLNhexKveNDhC6AB6Gh4h12CeH4mn8EFAeaCL3hOEqcRoOrdI_Z3mGjXMfEuHl1l1E8DOBBreYOa94k0E21gwaMV4Flzg2NDaIzWzfiIa6rLnsTtmoIRSM; sgid=00-37231263-AVzziarHa9FBDDXgd8gozsCw; ppmdig=155946462600000037bbc99c14de0faf540e6e8adc8f05a5; sct=5',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
keyword = '风景'


def get_index(keyword, page):
    data = {
        'type': 2,
        'query': keyword,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print('302')
    except ConnectionError:
        return get_html(url)


def main():
    for page in range(1, 101):
        html=get_index(keyword, page)
        print(html)


if __name__ == '__main__':
    main()
