from datetime import datetime, timedelta, timezone, date

tz = timezone(timedelta(hours=7), name='Hà Nội')
now = datetime.now(tz=tz)
date_format = '%d/%m/%Y'
datetime_format = '%d/%m/%Y %H:%M:%S'
print(now.strftime(datetime_format))  # 20/01/2022 09:55:43
current_date = now.date()
current_time = now.time()
print(current_date.strftime(date_format))  # 20/01/2022
print(current_time.isoformat())  # 09:55:43.031169
print(f'Múi giờ: {now.tzinfo.tzname(now)}')  # Múi giờ: Hà Nội

# chuyển string thành đối tượng datetime
datetime_string = '25/03/2030 15:36:24'

my_datetime = datetime.strptime(datetime_string, datetime_format)
print(my_datetime.isoformat())  # 2030-03-25T15:36:24


# from datetime import time
#
# now = time(20, 37, 46)
# print(now)  # 20:37:46
# print(f'Giờ: {now.hour}')  # Giờ: 20
# print(f'Phút: {now.minute}')  # Phút: 37
# print(f'Giây: {now.second}')  # Giây: 46
