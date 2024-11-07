'''Измайлов Михаил ИУ7-13Б
Программа для составления новой матрицы'''
# ввод первого массива
while True:
    a = list(map(int, input('Введите целочисленные элементы массива a через пробел: ').split()))
    if a != []: break
    print('Массив должен содержать элементы')
print()
# ввод второго массива
while True:
    b = list(map(int, input('Введите целочисленные элементы массива b через пробел: ').split()))
    if len(a) == len(b): break
    print('Повторите ввод массива b, так как массивы должны быть одномерными')

m = [] # переменная для хранения новой матрицы
s = [] # массив квадратов
for i in range(len(a)): # перебираем индексы строк матрицы
    m.append([])
    count = 0
    for j in range(len(a)): # перебираем индексы столбцов
        m[i].append(a[i]*b[j])
        if int((a[i]*b[j])**0.5)**2 == a[i]*b[j]: # проверка на квадрат
            count += 1
    s.append(count)

# вывод
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] < 0: 
            print(f'{m[i][j]:^4}', end = ' ')
        else:
            print(f' {m[i][j]:^3}', end = ' ')
    print(f' {s[i]:^3}', end = ' ')
    print()