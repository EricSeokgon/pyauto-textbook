from datetime import datetime

# d-day 날짜를 지정
dday = datetime(2025, 4, 13)

# 오늘 날짜를 지정
now = datetime.now()

# 일수 계산
delta = dday - now

# 결과 출력

print('앞으로' + str(delta.days + 1) + '일 남았습니다.')
