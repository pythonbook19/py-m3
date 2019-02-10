import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



from datetime import datetime as dt
ex = dt.now()
print(ex)
print("Месяц:", ex.month)
print("День:", ex.day)
print("Час:", ex.hour)
print("Минута:", ex.minute)
print("Секунда", ex.second)

d = dt.now() -  dt(year=1974, month=11, day=14)
print (d)
