'''Измайлов Михаил ИУ7-13Б
Программа для поиска максимума и среднего арифметического по условию'''
# ввод массива
while True:
    I = list(map(int, input('Введите целочисленные элементы массива I через пробел: ').split()))
    if I != []: break
    print('Массив должен содержать элементы')
print()
# создание матрицы
while True:
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: ')) # количество столбцов
    if m > 0 and n > 0: # проверка на существование матрицы
        break
    print('Введенные значения недопустимы. Повторите ввод')
D = []
for i in range(n):
    D.append([])
    for j in range(m):
        D[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))

R = [] # массив для хранения максимальных элементов в строке
for n_0 in I: # пребираем индексы нужных строк
    if n_0 < n: # проверяем на существование строки
        R.append(max(D[n_0])) # добавляем в массив максимум
averege = sum(R) / len(R)

# вывод
print('\nМатрица D:')
for i in range(n):
    for j in range(m):
        if D[i][j] < 0: 
            print(f'{D[i][j]:^4}', end = ' ')
        else:
            print(f' {D[i][j]:^3}', end = ' ')
    print()
print('Массив I:')
for i in range(len(I)):
    if I[i] < 0: 
        print(f'{I[i]:^4}', end = ' ')
    else:
        print(f' {I[i]:^3}', end = ' ')
print('\nМассив R:')
for i in range(len(R)):
    if R[i] < 0: 
        print(f'{R[i]:^4}', end = ' ')
    else:
        print(f' {R[i]:^3}', end = ' ')
print(f'\nСреднее арифмитическое: {averege}')
