'''Измайлов Михаил ИУ7-13Б
Программа считает количество элементов и выводит преобразованную матрицу B'''
# ввод матриц
while True:
    m = int(input('Введите количество столбцов матриц: ')) # количество столбцов
    if m > 0: # проверка на существование матрицы с введенным количеством столбцов
        break
    print('Введенные значения недопустимы. Повторите ввод')
# создание матрицы A
while True:
    n_A = int(input('Введите количество строк матрицы A: '))
    if n_A > 0: # проверка на существование матрицы с введенным количеством строк
        break
    print('Введенные значения недопустимы. Повторите ввод')
matrix_A = []
for i in range(n_A):
    matrix_A.append([])
    for j in range(m):
        matrix_A[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))
print()
# создание матрицы B
while True:
    n_B = int(input('Введите количество строк матрицы B: '))
    if n_B > 0: # проверка на существование матрицы с введенным количеством строк
        break
    print('Введенные значения недопустимы. Повторите ввод')
matrix_B = []
for i in range(n_B):
    matrix_B.append([])
    for j in range(m):
        matrix_B[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки для матрицы B: ')))

mean = [] # массив для хранения среднего арифметического для каждого столбца матрицы B
for j in range(m):
    sum_0 = 0 # переменная для храниния суммы чисел столбца
    for i in range(n_B):
        sum_0 += matrix_B[i][j]
    mean.append(sum_0/n_B)
coefficients = [] # массив для хранения количества подходящих чисел
for j in range(m):
    count = 0 # переменная для подсчета подходящих элементов в каждой строке
    for i in range(n_A):
        if matrix_A[i][j] > mean[j]:
            count += 1
    print(f'В столбце {j + 1} найдено {count} элементов')
    coefficients.append(count)
for j in range(m):
    count = 0
    for i in range(n_B):
        if coefficients[j] > 0:
            matrix_B[i][j] *= coefficients[j]

# вывод
for i in range(n_B):
    for j in range(m):
        if matrix_B[i][j] < 0: 
            print(f'{matrix_B[i][j]:^4}', end = ' ')
        else:
            print(f' {matrix_B[i][j]:^3}', end = ' ')
    print()
