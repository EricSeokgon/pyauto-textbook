from bs4 import BeautifulSoup

hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
    html_str = fp.read()

# BeautifulSoup 객체
soup = BeautifulSoup(html_str, 'html5lib')

# head의 조상 확인하기
head = soup.head
print('head의 부모:', head.parent.name)
print('head의 부모의 부모:', head.parent.parent.name)

# head의 자식 확인하기
print('head의 자식')
for e in head.contents:
    print('[{0}]{1}'.format(type(e), e.name))

