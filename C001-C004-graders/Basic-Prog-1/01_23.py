s = input()
month = s[:2]
day = s[2:4]
year_ad = int(s[4:])
year_be = year_ad + 543

if month == '01':
    month_abbr = 'JAN'
elif month == '02':
    month_abbr = 'FEB'
elif month == '03':
    month_abbr = 'MAR'
elif month == '04':
    month_abbr = 'APR'
elif month == '05':
    month_abbr = 'MAY'
elif month == '06':
    month_abbr = 'JUN'
elif month == '07':
    month_abbr = 'JUL'
elif month == '08':
    month_abbr = 'AUG'
elif month == '09':
    month_abbr = 'SEP'
elif month == '10':
    month_abbr = 'OCT'
elif month == '11':
    month_abbr = 'NOV'
elif month == '12':
    month_abbr = 'DEC'

result = day + '-' + month_abbr + '-' + str(year_be)
print(result)