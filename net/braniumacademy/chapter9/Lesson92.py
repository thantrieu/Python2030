from datetime import timedelta, date
today = date.today()
print(today)

year2030 = today.replace(year=2030)
print(year2030)

date_format = '%d/%m/%Y'
print(today.strftime(date_format))

print(today.strftime('%B'))
full_date_format = '%A, %B %d %Y'
print(today.strftime(full_date_format))


# year = timedelta(days=365)
# another_year = timedelta(weeks=50, days=15)
#
# print(f'{year == another_year}')
# print(f'Seconds of year: {year.total_seconds()}')
#
# ten_year = year * 10
# nine_year = ten_year - year
# three_year = nine_year // 3
# print(ten_year)
# print(nine_year)
# print(three_year)
# print(f'3 years = {three_year.days} days.')
