from bs4 import BeautifulSoup

# HTML 파일 읽기
hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

# BeautifulSoup 객체
soup = BeautifulSoup(html_str, 'html5lib')
print(soup.prettify() + '\n')

# title 태그 확인하기
title = soup.title
print(title)
print(title.string + '\n')

# BS4 객체 타입
print(type(soup))
print(type(title))
print(type(title.string))
