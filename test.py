from datetime import date
# email = 'alli.r@ru.is'

# try:
#     atsymble = email.index('@')
#     dot = email.index('.', atsymble)
#     print('Rétt')
# except ValueError:
#     print('Rangur innsláttur')

date1 = '23.4.18'
date2 = '27.4.18'

day1, month1, year1 = date1.split('.')
day2, month2, year2 = date2.split('.')
date3 = date(int(year1), int(month1), int(day1))
date4 = date(int(year2), int(month2), int(day2))
time_period = date4 - date3
print(time_period.days)