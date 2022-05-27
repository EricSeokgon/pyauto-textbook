# 날짜 시간 관련 처리를 하는 모듈
from datetime import datetime as dt

# 현재 시각 구하기
t = dt.now()
fmt = t.strftime('%Y년%m월%d일 %H시%M분%S초')
print(fmt)
