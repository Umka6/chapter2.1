year = int(input('Введите год '))

def year_is_leap(year):

    if year % 4 != 0:
        result = 'Год обычный'

    elif year % 100 == 0:
        if year % 400 == 0:
            result = 'Год високосный'
        else:
            result = 'Год обычный'
    else:
        result = 'Год високосный'
    return result
finish = year_is_leap(year)

print(finish)