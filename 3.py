#Тітов Іван 122-В
#За s-назвою місяця визначити відповідну пору року.
from enum import Enum
class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    while True:
        try:
            s = int(input('month:'))
            break
        except ValueError:
            print('Only nums')
    if s == month.January.value or s == month.February.value and s == month.December.value:
        print(season.Winter.name)

    elif s == month.March.value and s == month.April.value and s == month.May.value :
        print(season.Spring.name)

    elif s == month.June.value and s == month.July.value and s == month.August.value:
        print(season.Summer.name)

    elif s == month.September.value and s == month.October.value and s == month.November.value :
        print(season.Autumn.name)

    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break