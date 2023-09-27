def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

days = ['man', 'tir', 'ons', 'tor', 'fre', 'lør', 'søn']

def weekday_newyear(year):
    day = 0
    for i in range(1900, year):
        if is_leap_year(i) == True:
            day = (day + 366)%7
        else:
            day = (day + 365)%7
    return day

for j in range(1900, 1920):
    weekday = days[weekday_newyear(j)]
    print(j, weekday)
    