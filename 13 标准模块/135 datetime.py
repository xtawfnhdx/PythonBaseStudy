import datetime
import calendar
import time
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)

da_str=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(da_str)
print(datetime.datetime.strptime(da_str,'%Y-%m-%d %H:%M:%S.%f'))
print(time.time())
time.sleep(3)
print(time.time())
print(calendar.timegm(datetime.datetime.utcnow().timetuple()))