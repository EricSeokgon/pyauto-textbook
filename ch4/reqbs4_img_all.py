import os, time, requests, urllib
from bs4 import BeautifulSoup
from _MyPath import URL

# 저장 폴더 지정
save_dir = './output/reqbs4_img_all'
# 이미지를 가져올 웹사이트
target_url = URL


# 메인 처리
def download_images():
    # 페이지의 HTML 읽기
    html = requests.get(target_url).text
    # HTML을 분석해 이미지 URL 추출
    urls = get_url(html)
    # URL의 이미지 다운로드
    request_url(urls)


# 이미지 URL 추출
def get_url(html):
    # 뷰티풀 수프로 HTML 분석
    soup = BeautifulSoup(html, 'html5lib')
    res = []
    # img 태그에서 URL가져오기
    for img in soup.select('#gallery-section img'):
        # 상대 경로
        src = img['src']
        # URL을 절대 경로로 변환
        url = urllib.parse.urljoin(target_url, src)
        print('img.src=', url)
        res.append(url)
    return res


# 연속으로 이미지 다운로드
def request_url(urls):
    # 저장 폴더가 없으면 생성
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for url in urls:
        # 파일명 지정
        fname = os.path.basename(url)
        save_file = save_dir + '/' + fname
        # 이미지 다운로드
        r = requests.get(url)
        # 파일로 저장
        with open(save_file, 'wb') as fp:
            fp.write(r.content)
            print("save:", save_file)
        time.sleep(1)

if __name__ == '__main__':
    download_images()
