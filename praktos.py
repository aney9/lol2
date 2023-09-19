import math
while True:
    try:
        deistvie = int (input('Какую операцию вы хотите выбрать? \n 1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление \n 5. Возведение в степень \n 6. Квадратный корень \n 7.Факториал \n 8. Синус \n 9. Косинус \n 10.Тангенс \n 11. Выход \n'))  
    except ValueError:
                print('ошыбка')
                continue
    if deistvie == 1: 
            try:
                a = float(input('Введите число: '))
                b = float(input('Введите число: '))
            except ValueError:
                print('ошыбка')
            else:
                print('Сумма = ', a + b)
            continue
    if deistvie == 2:
            try:
                a = float(input('Введите число: '))
                b = float(input('Введите число: '))
            except ValueError:
                print('ошыбка')
            else:
                print('Разность = ', a - b)
            continue
    if deistvie == 3:
            try:
                a = float(input('Введите число: '))
                b = float(input('Введите число: '))
            except ValueError:
                print('ошыбка')
            else:
                print('Произведение = ', a * b)
            continue
    if deistvie == 4:
            try:
                a = float(input('Введите число: '))
                b = float(input('Введите число: '))
            except ValueError:
                print('ошыбка')
            else:
                if (b != 0):
                    print('Частное = ', a/b)
                else:
                    print('На 0 делить можно, но не в этом калькуляторе')
            continue
    if deistvie == 5:
            try:
                a = float(input('Введите число: '))
                b = float(input('Введите число: '))
            except ValueError:
                print('ошыбка')
            else:
                print('Степень = ', a ** b)
            continue
    if deistvie == 6:
            try:
                 a = float(input('Введите число: '))
                 if a > 0:
                      print(math.sqrt(a)) 
                 else:
                      print('не то значение')
            except ValueError:
                print('ошыбка')
            continue
    if deistvie == 7:
        try:
                a = int(input('Введите число: '))
                if a > 0:
                    print(math.factorial(a))
                else: 
                     print('не то значение')
        except ValueError:
                print('ошыбка')
        continue
    if deistvie == 8:
        try:
            a = int(input('Введите число: '))
            print(math.sin(a))
        except ValueError:
                print('ошыбка')
    if deistvie == 9:
        try:
            a = int(input('Введите число: '))
            print(math.cos(a))
        except ValueError:
            print('ошыбка')
    if deistvie == 10:
        try:
            a = int(input('Введите число: '))
            print(math.tan(a))
        except ValueError:
            print('ошыбка')
    if deistvie == 11:
        break
