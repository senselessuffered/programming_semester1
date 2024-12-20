"""Измайлов Михаил ИУ7-13Б
Программа для проверки входимости вводимой точки в область."""
import math

x = float(input('Введите координату x: ')) # ввод x
y = float(input('Введите координату y: ')) # ввод y

# вычисление значений функций
y1 = -0.125 * (x + 9)**2 + 8
y2 = -0.125 * (x - 9)**2 + 8
y3 = 7 * (x + 8)**2 + 1
y4 = 7 * (x - 8)**2 + 1
y5 = 1 / 49 * (x + 1)**2
y6 = 1 / 49 * (x - 1)**2
y7 = -4 * x**2 + 2
y8 = 4 * x**2 - 6
y9 = -1 / 16 * x**2
y10 = -1 / 16 * x**2
y11 = 1 / 3 * (x + 5)**2 - 7
y12 = 1 / 3 * (x - 5)**2 - 7
y13 = -2 * (x + 1)**2 - 2
y14 = -2 * (x - 1)**2 - 2
y15 = 3 / 2 * x + 2
y16 = -3 / 2 * x + 2
x17 = 1
x18 = -1
is_bok = False # переменная для проверки принадлежности точки боку

# провека на принадлежность точки боку бабочки
if 0 <= y <= 2 and x == x17:
    is_bok = True
if -2 <= y <= 0 and x == x18:
    is_bok = True

if is_bok:
    print('\nТочка принадлежит области')
elif -2 <= x <= 0 and y == y16: # проверка на принадлежность точки левому усику
    print('\nТочка принадлежит области')
elif 0 <= x <= 2 and y == y15: # проверка на принадлежность точки правому усику
    print('\nТочка принадлежит области')
else:
    if -9 <= x < -1: # проверка на принадлежность точки левому крылу
        if x <= -8:
            if y <= y1 and y >= y3:
                print('\nТочка принадлежит области')
            else:
                print('\nТочка не лежит в области')
        if -8 < x <= -1:
            if (y <= y1 and y >= y9) or (y <= y5 and y >= y11 and y >= y13):
                print('\nТочка принадлежит области')
            else:
                print('\nТочка не лежит в области')
    elif -1 < x < 1: # проверка на принадлежность тоски телу
        if y <= y7 and y >= y8:
            print('\nТочка принадлежит области')
        else:
            print('\nТочка не принадлежит области')
    elif 1 < x <= 9: # проверка на принадлежность точки правому крылу
        if x >= 8:
            if y <= y2 and y >= y4:
                print('\nТочка принадлежит области')
            else:
                print('\nТочка не лежит в области')
        if 1 < x < 8:
            if (y <= y2 and y >= y6) or (y <= y10 and y >= y14 and y >= y12):
                print('\nТочка принадлежит области')
            else:
                print('\nТочка не принадлежит области')  
    else:
        print('\nТочка не принадлежит области')