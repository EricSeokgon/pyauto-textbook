from datetime import datetime, timedelta

base_t = datetime(2025, 2, 27)
t = base_t + timedelta(days=3)
print(t.strftime('%Y/%m/%d'))
