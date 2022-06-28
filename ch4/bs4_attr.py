from bs4 import BeautifulSoup

hfile = 'server/templates/book_static.html'

# html 파일 읽기
with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

# beautifulsoup 객체 생성
soup = BeautifulSoup(html_str, 'html5lib')

# id가 b1인 .item 요소 찾기
print(soup.find(id='b1', class_='item'))
print(soup.find(name='div', attrs={'id': 'b1', 'class': 'item'}))
print(soup.find_all('div', class_='item', limit=1))
print(soup.select_one('div#b1.item'))
print('----------------')

# 책 제목으로 .title 요소 찾기
print(soup.find(string='도커, 컨테이너 빌드업!'))
print(soup.find('div', string='도커, 컨테이너 빌드업!'))
print('----------------')

# 책 제목이 나뉘어졌을 때 .title 요소 찾기
ele = soup.find(string='파이썬 머신러닝')
print(ele)
print(ele.parent)
print(ele.parent.parent)
