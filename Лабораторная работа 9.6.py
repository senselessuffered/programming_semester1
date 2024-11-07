'''Измайлов Михаил ИУ7-13Б
Программа для замены всеъ строчных латинских символов на заглавные и наоборот по определенным правилам'''
import string # импорт библиотеки с алфавитом

vowels = 'eyuioa' # переменная со всеми гласными
alphabet = string.ascii_lowercase # переменная со всем алфавитом
# создание матрицы
while True:
    n = int(input('Введите количество строк матрицы: '))
    m = int(input('Введите количество столбцов матрицы: '))
    if n > 0 and m > 0: # проверка на существование матрицы
        break
    print('Введенные значения недопустимы. Повторите ввод')
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: '))

# вывод
print('\nМатрица исходная:')
for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:^7}', end = ' ')
    print()

# преобразования через пробег по всем элементам
for i in range(n):
    for j in range(m):
        new = '' # переменная для перезаписи элемента
        for k in range(len(matrix[i][j])):
            if matrix[i][j][k].lower() in alphabet: # проверка на букву
                if matrix[i][j][k].lower() in vowels: # проверка на гласную
                    new += matrix[i][j][k].lower()
                else:
                    new += matrix[i][j][k].upper()
            else:
                new += matrix[i][j][k]
        matrix[i][j] = new # замена

# вывод
print('\nМатрица преобразованная:')
for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:^7}', end = ' ')
    print()
