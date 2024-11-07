'''Измайлов Михаил ИУ7-13Б
Программа для поворота матрицы на 90 градусов'''
# ввод матрицы
while True:
    n = int(input('Введите порядок матрицы: '))
    if n > 2: # проверка на существование матрицы с введенными длинами сторон
        break
    print('Введенные значения недопустимы. Повторите ввод')
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))

levels = n // 2 # вычисление середины, т.к элементы после середины поменяются сами
for level in range(levels):
    first = level # первый индекс равен тому на котором мы стоим
    last = n - level - 1 # последний равен длина - 1 - индекс старта
    for i in range(first, last): # перебираем индексы в промежутке
        diffrence = i - first # вычисляем дельту 
        top = matrix[first][i] # запоминаем элемент старта
        matrix[first][i] = matrix[last - diffrence][first] # на место элемента старта ставис левый элемент
        matrix[last - diffrence][first] = matrix[last][last - diffrence] # ставим на место левого нижний элемент
        matrix[last][last - diffrence] = matrix[i][last] # на место нижнего элемента правый
        matrix[i][last] = top # на место правого первый элемент

# вывод матрицы
for i in range(n):
    for j in range(n):
        if matrix[i][j] < 0: 
            print(f'{matrix[i][j]:^4}', end = ' ')
        else:
            print(f' {matrix[i][j]:^3}', end = ' ')
    print()
print()

levels = n // 2 
for level in range(levels):
    first = level
    last = n - level - 1
    # все в обратном направлении
    for i in range(first, last):
        diffrence = i - first 
        top = matrix[first][i]
        matrix[first][i] = matrix[i][last] 
        matrix[i][last] = matrix[last][last - diffrence] 
        matrix[last][last - diffrence] = matrix[last - diffrence][first] 
        matrix[last - diffrence][first] = top 

# вывод матрицы
for i in range(n):
    for j in range(n):
        if matrix[i][j] < 0: 
            print(f'{matrix[i][j]:^4}', end = ' ')
        else:
            print(f' {matrix[i][j]:^3}', end = ' ')
    print()
