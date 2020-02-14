#Тітов Іван 122-В
#Робота світлофора для водіїв запрограмована таким чином: на початку кожної
#години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
#жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
#Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
#минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
#момент.
while True:
    while True:
        try:
            hour = int(input('Enter your time'))

            break
        except ValueError:
            print('Only nums')
    t = hour % 6
    if 1 <= t <= 3:
        print('Green signal')

    elif t == 4:
        print('Yellow signal')
    else:
        print('Red signal')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break