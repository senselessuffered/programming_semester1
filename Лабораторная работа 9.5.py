'''Измайлов Михаил ИУ7-13Б
Программа вычисления произведения матриц'''
# функция для вычисления значения элементы матрицы C по правилам
def element(i, j):
    result = 0 # пременная для хранения суммы произведения элементов
    for index in range(n_A):
        result += matrix_A[i][index]*matrix_B[index][j]
    return result

# создание матрицы A
while True:
    n_A = int(input('Введите количество строк матрицы A: '))
    m_A = int(input('Введите количество столбцов матрицы A: '))
    if n_A > 0 and m_A > 0: # проверка на существование матрицы с введенным количеством строк
        break
    print('Введенные значения недопустимы. Повторите ввод')
matrix_A = []
for i in range(n_A):
    matrix_A.append([])
    for j in range(m_A):
        matrix_A[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: ')))
print()
# создание матрицы B
while True:
    n_B = int(input('Введите количество строк матрицы B: '))
    m_B = int(input('Введите количество столбцов матрицы B: '))
    if (n_A > 0 and m_A > 0) and m_A == n_B: # проверка на существование матрицы с введенным количеством строк
        break
    print('Введенные значения недопустимы. Обратите внимаение, что число столбцов матрицы A должно ровняться числу строк матрицы B. Повторите ввод')
matrix_B = []
for i in range(n_B):
    matrix_B.append([])
    for j in range(m_B):
        matrix_B[i].append(int(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки для матрицы B: ')))

matrix_C = [] # новая матрица
for i in range(n_A):
    matrix_C.append([])
    for j in range(m_B):
        matrix_C[i].append(element(i, j))

# вывод полученной матрицы
for i in range(n_A):
    for j in range(m_B):
        if matrix_C[i][j] < 0: 
            print(f'{matrix_C[i][j]:^4}', end = ' ')
        else:
            print(f' {matrix_C[i][j]:^3}', end = ' ')
    print()
