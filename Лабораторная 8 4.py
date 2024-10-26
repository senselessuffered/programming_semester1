'''Измайлов Михаил ИУ7-13Б
Программа переставляет местами столбцы с большей и меньшей суммой'''
import math

# ввод матрицы
while True:
    n = int(input('Введите количество строк матрицы: '))
    m = int(input('Введите количество столбцов матрицы: '))
    if n > 0 and m > 0: # проверка на существование матрицы с введенными длинами сторон
        break
    print('Введенные значения недопустимы. Повторите ввод')
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))

summa_mx = 0 # пременная хранит максимальную сумму элементов столбца
summa_mn = math.inf # пременная хранит минимальную сумму элементов столбца
index_mx = 0 # индекс столбца  с максимальной суммой
index_mn = 0 # индекс столбца с минимальной суммой
for j in range(m): 
    summa_0 = 0 # переменная для вычисления суммы элементов столбца
    for i in range(n):
        summa_0 += a[i][j]
    if summa_0 > summa_mx:
        summa_mx = summa_0
        index_mx = j
    if summa_0 < summa_mn:
        summa_mn = summa_0 
        index_mn = j
# меняем местами столбцы
for i in range(n):
    a[i][index_mn], a[i][index_mx] = a[i][index_mx], a[i][index_mn]

# вывод матрицы
if summa_mn != math.inf: # проверка на наличие строк с отрицательными элементами в списке
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] < 0: 
                print(f'{a[i][j]:^4}', end = ' ')
            else:
                print(f' {a[i][j]:^3}', end = ' ')
        print()
else:
    print('Желаемых строк не найдено')
    