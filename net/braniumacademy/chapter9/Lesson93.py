from datetime import time, datetime, timezone, timedelta
#
# now = time(11, 30, 26)
# print(now)
# print(f'Giờ: {now.hour}')
# print(f'Phút: {now.minute}')
# print(f'Giây: {now.second}')
tz = timezone(timedelta(hours=7), name='Hà Nội')
now = datetime.now(tz=tz)
date_format = '%d/%m/%Y'
datetime_format = '%A %d/%m/%Y %H:%M:%S'
print(now.strftime(datetime_format))
print(f'Múi giờ: {now.tzinfo.tzname(now)}')

current_date = now.date()
current_time = now.time()
print(current_date.strftime(date_format))
print(current_time.isoformat())

datetime_string = '25/03/2030 15:36:24'
my_datetime_format = '%d/%m/%Y %H:%M:%S'
my_datetime = datetime.strptime(datetime_string, my_datetime_format)
print(my_datetime.isoformat())
