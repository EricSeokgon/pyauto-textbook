import requests, urllib, os, time, re, shutil
from bs4 import BeautifulSoup

# 저장 위치
save_dir = './output/pydoc'
# 기준 URL
pydoc_url = 'https://docs.python.org/ko/3/tutorial/'
# 다운로드한 페이지를 저장할 딕셔너리
visited = {}


def download_pydoc(input_url):
    down_url = prepro_URL(input_url)
    if not down_url: return
    print('===', down_url, '탐색===')
    # 페이지 텍스트 가져오기
    res = requests.get(down_url)
    res.encoding = res.apparent_encoding
    html = res.text
    # HTML 파일 다운로드
    save_file(down_url, html)
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html, 'html5lib')
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        a_url = urllib.parse.urljoin(down_url, href)
        download_pydoc(a_url)


# URL 검사 및 폴더 생성
def prepro_URL(before_url):
    # URL 전처리
    pResult = urllib.parse.urlparse(before_url)
    path = pResult.path
    if os.path.basename(path) == '':
        path += 'index.html'
    after_url = urllib.parse.urljoin(before_url, path)
    # URL 검사
    checkResult = check_URL(after_url)
    if not checkResult: return False
    # 폴더 만들기
    dirname = save_dir + os.path.dirname(path)
    if not os.path.exists(dirname):
        print('[폴더 생성]', dirname)
        os.makedirs(dirname)
    return after_url


# 다운로드할 URL인지 확인
def check_URL(url):
    # 형식 검사
    if pydoc_url not in url: return False
    # 중복 검사
    if url in visited: return False
    # 방문처리
    visited[url] = True
    return True


# 파일 다운로드
def save_file(url, text):
    # 파일 경로 결정
    fname = save_dir + urllib.parse.urlparse(url).path
    # 파일저장
    with open(fname, 'wt', encoding='utf-8') as f:
        f.write(text)
    print('[파일 저장] ::', fname)
    time.sleep(1)


if __name__ == '__main__':
    download_pydoc(pydoc_url)
