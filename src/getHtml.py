import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time


def getHTMLText(url):
    driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs')  # phantomjs的绝对路径
    time.sleep(2)
    driver.get(url)  # 获取网页
    time.sleep(2)
    return driver.page_source


def fillUnivlist(html):
    soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    tag = soup.find('p', attrs={'id': 'statusWanIP'}).get_text()
    return str(tag)


def main():
    url = 'http://www.liph.xyz:6789/index.html'  # 要访问的网址
    html = getHTMLText(url)  # 获取HTML
    return fillUnivlist(html)


if __name__ == '__main__':
    main()
