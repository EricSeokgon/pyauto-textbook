# 더미 데이터
dummy_data = [
    ["이영희", 300],
    ["이영희", 600],
    ["이영희", 200],
    ["박철수", 300],
    ["박철수", 200],
]

# 데이터 분류하기
users = {}
for row in dummy_data:
    name = row[0]
    # 고객명이 처음 나왔다면 딕서너리에 추가
    if name not in users:
        users[name] = []
    # 리스트에 row 추가
    users[name].append(row)

# 고객별 집계
for name, rows in users.items():
    print(rows)
    total = 0
    for row in rows:
        total += row[1]
    print(name, total)
