a = '04.122005'
if '.' in a:
    seperator = '.'
elif '/' in a:
    seperator = '/'
elif '-' in a:
    seperator = '-'
day,month,year = a.split(seperator)

print(day)
print(month)
print(year)

