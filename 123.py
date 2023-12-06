import random as r

def stafka():
    global ochki
    if ochki < 1:
        return print('Вы проиграли')
    print('У вас', ochki,'очков. Сколько вы хотите поставить ?')
    sta = int(input())
    if sta > ochki:
        print('У вас нет такого кол-ва очков, выберите другое значение')
        stafka()
    else:
        print('Выберите действие 1)>7 2)<7 3)Загадать число')
        a = int(input())
        if a == 1 or a == 2 or a == 3:
            if a == 3:
                a = int(input())
                if a < 2 or a > 12:
                    print('от 2 до 12')
                    stafka()
        else:
            print('Не то значение!')
            stafka()
        b = r.randint(2, 12)
        if a == 1 and b > 7:
            ochki += sta
        elif a == 2 and b < 7:
            ochki += sta
        elif a == 3 and b == a:
            ochki += sta*4
        else:
            ochki -= sta
        print('Ваши очки', ochki)
        print('Хотите ещё поиграть? 1)Да 2)Нет')
        a = int(input())
        if a == 1:
            stafka()
        else:
            return ochki
ochki = 100
print(stafka())