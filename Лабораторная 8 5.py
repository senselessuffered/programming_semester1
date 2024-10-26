'''Измайлов Михаил ИУ7-13Б
Программа для поиска макимального элемента над главной диагональю и минимального под побочной'''
import math

# ввод матрицы
while True:
    n = int(input('Введите порядок матрицы: '))
    if n > 2: # проверка на существование матрицы с введенными длинами сторон
        break
    print('Введенные значения недопустимы. Повторите ввод')
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))

mx = -math.inf # переменная для хранения максимального элемента
mn = math.inf # переменная для хранения минимального элемента
for i in range(n):
    for j in range(n):
        # сверяя индексы, понимаем где относительно диагонали находится элемент
        if j > i:
            if mx < a[i][j]:
                mx = a[i][j]
        if j > abs(i - 3):
            if mn > a[i][j]:
                mn = a[i][j]

# вывод
print(f'Максимальный элемент, располоденный над главной диагональю: {mx}')
print(f'Минимальный элемент, располоденный под побочной диагональю: {mn}')