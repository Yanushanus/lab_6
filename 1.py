#Тітов Іван 122-В
#За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
#наявність високосних років.
days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
    while True:
        try:
            d, m, y = int(input('Enter your day:')), \
            int(input('Enter your month:')), \
            int(input('Enter your year:'))
            break
        except ValueError:
            print('Only nums')
    if d in days and m in months and y in years: #for next day
                if m == 1or m == 3or m == 5or m == 7or m == 8or m == 10or m == 12:
                    if d == 31:
                        if m == 12:
                            d1 = 1
                            m1 = 1
                            y1 = y + 1
                            print(f'Date of the next day {d1}.{m1}.{y1}')
                        else:
                            d1 = 1
                            m1 = m + 1
                            y1 = y
                            print(f'Date of the next day {d1}.{m1}.{y1}')
                    else:
                        d1 = d+1
                        m1 = m
                        y1 = y
                        print(f'Date of the next day {d1}.{m1}.{y1}')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 0 < d < 31:
                        if d == 30:
                            d1 = 1
                            m1 = m + 1
                            y1 = y
                            print(f'Date of the next day {d1}.{m1}.{y1}')
                        else:
                            d1 = d+1
                            m1 = m
                            y1 = y
                            print(f'Date of the next day {d1}.{m1}.{y1}')
                    else:
                        print('Wrong proviso')
                elif m == 2:
                    if y % 4 == 0:
                        if 0 < d < 30:
                            if d == 29:
                                d1 = 1
                                m1 = 3
                                y1 = y
                                print(f'Date of the next day{d1}.{m1}.{y1}')
                            else:
                                d1 = d + 1
                                m1 = m
                                y1 = y
                                print(f'Date of the next day {d1}.{m1}.{y1}')
                        else:
                            print('Wrong proviso')
                    else:
                        if 1 <= d <= 28:
                            if d == 28:
                                d1 = 1
                                m1 = 3
                                y1 = y
                                print(f'Date of the next day {d1}.{m1}.{y1}')
                            else:
                                d1 = d + 1
                                m1 = m
                                y1 = y
                                print(f'Date of the next day {d1}.{m1}.{y1}')
                        else:
                            print('Wrong proviso')
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                    if d == 1:
                        if m == 1:
                            d1 = 31
                            m1 = 12
                            y1 = y - 1
                            print(f'Date of the previous day {d1}.{m1}.{y1}')
                        elif m == 8:
                            d1 = 31
                            m1 = 7
                            y1 = y
                            print(f'Date of the previous day {d1}.{m1}.{y1}')
                        elif m == 3:
                            if y % 4 == 0:
                                d1 = 29
                                m1 = 2
                                y1 = y
                                print(f'Date of the previous day {d1}.{m1}.{y1}')
                            else:
                                d1 = 28
                                m1 = 2
                                y1 = y
                                print(f'Date of the previous day {d1}.{m1}.{y1}')
                        else:
                            d1 = 30
                            m1 = m - 1
                            y1 = y
                            print(f'Date of the previous day {d1}.{m1}.{y1}')
                    else:
                        d1 = d - 1
                        m1 = m
                        y1 = y
                        print(f'Date of the previous day {d1}.{m1}.{y1}')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 0 < d < 31:
                        if d == 1:
                            d1 = 31
                            m1 = m - 1
                            y1 = y
                            print(f'Date of the previous day {d1}.{m1}.{y1}')
                        else:
                            d1 = d - 1
                            m1 = m
                            y1 = y
                            print(f'Date of the previous day {d1}.{m1}.{y1}')
                    else:
                        print('Wrong proviso')
                elif m == 2:
                    if y % 4 == 0:
                        if 0 < d < 30:
                            if d == 1:
                                d1 = 31
                                m1 = 1
                                y1 = y
                                print(f'Date of the previous day {d1}.{m1}.{y1}')
                            else:
                                d1 = d - 1
                                m1 = m
                                y1 = y
                                print(f'Date of the previous day {d1}.{m1}.{y1}')
                        else:
                            print('Wrong proviso')
                    else:
                        if 1 <= d <= 28:
                            if d == 1:
                                d1 = 31
                                m1 = 1
                                y1 = y
                                print(f'Date of the previous day{d1}.{m1}.{y1}')
                            else:
                                d1 = d - 1
                                m1 = m
                                y1 = y
                                print(f'Date of the previous day{d1}.{m1}.{y1}')
                        else:
                            print('Wrong proviso')
    answer = input("Retry one more time?If yes,press '1',if no,something else")
    if answer == '1':
        continue
    else:
        break