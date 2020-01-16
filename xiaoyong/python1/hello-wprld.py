from datetime import datetime
from datetime import timedelta

# keti
print(datetime.today())
days = 2
before=datetime.today() + timedelta(-days)
print(before)