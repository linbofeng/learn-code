from datetime import datetime
from datetime import timedelta

# 课题1
print(datetime.today())
days = 2
before = datetime.today() + timedelta(+days)
print (before)