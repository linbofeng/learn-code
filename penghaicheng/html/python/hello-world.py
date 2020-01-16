from datetime import datetime, timedelta

# 注释：打印教程
print(datetime.today())
days = 6
before = datetime.today() + timedelta(+days)
print(before)
