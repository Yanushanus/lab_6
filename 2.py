#Тітов Іван 122-В
#Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
#цієї ж суми в гривнях.
from enum import Enum
class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4
while True:
    while True:
        try:
            x = float(input('amount of money:'))
            p = int(input('currency:'))
            break
        except ValueError:
            print('Only nums')
    if p == converter.USD.value:
        print(x * 25.4)
    elif p == converter.EUR.value:
        print(x * 30)
    elif p == converter.CZK.value:
        print(x * 10)
    elif p == converter.PLN.value:
        print(x * 8)
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break