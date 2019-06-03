from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as po

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def search():
    try:
        browser.get('https://www.jd.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next')))

        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'),
                                             str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList .gl-item')))
    html = browser.page_source
    doc = po(html)
    items = doc('#J_goodsList .gl-item').items()
    for item in items:
        product = {
            'image': item.find('.p-img .img').attr('src'),
            'price': item.find('.p-price').text(),
            'comment': item.find('.p-commit').text(),
            'name': item.find('.p-name').text(),
            'shop': item.find('.p-shop').text()
        }
    print(product)


def main():
    total = search()
    total = int(total)
    for i in range(2, total + 1):
        next_page(i)


if __name__ == '__main__':
    main()
