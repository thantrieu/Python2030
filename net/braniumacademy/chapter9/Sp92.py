from datetime import date

today = date.today()
print(today)  # 2022-01-19

year2030 = today.replace(year=2030, month=12)
print(year2030)  # 2030-12-19

date_format = '%d/%m/%Y'
print(today.strftime(date_format))  # 19/01/2022

full_date_format = '%A, %B %d %Y'
print(f'Today is {today.strftime("%A")}')  # Today is Wednesday
print(f'Today is {today.strftime(full_date_format)}')
# Today is Wednesday, January 19 2022

# from datetime import timedelta
#
# year = timedelta(days=365)
# another_year = timedelta(weeks=50, days=15)
#
# print(f'{year == another_year}')  # True
# print(f'Seconds of year: {year.total_seconds()}')  # Seconds of year: 31536000.0
#
# ten_year = year * 10
# print(ten_year)  # 3650 days, 0:00:00
#
# nine_year = ten_year - year
# print(nine_year)  # 3285 days, 0:00:00
#
# three_year = nine_year // 3
# print(three_year)  # 1095 days, 0:00:00
# print(f'3 year = {three_year.days} days.')  # 3 year = 1095 days.
