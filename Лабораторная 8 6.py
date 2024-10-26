'''Измайлов Михаил ИУ7-13Б
Программа для траспонирования матрицы'''

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

# меняем местами строку и столбец
for i in range(n):
    for j in range(i,n):
        a[i][j], a[j][i] = a[j][i], a[i][j]

# вывод матрицы
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < 0: 
            print(f'{a[i][j]:^4}', end = ' ')
        else:
            print(f' {a[i][j]:^3}', end = ' ')
    print()