# request 모듈 불러오기
import requests
from _MyPath import URL

# 현재 시각을 반환하는 서버에 요청 보내기
url = URL + 'today'
response = requests.get(url)

# 결과 출력
print(response.text)
