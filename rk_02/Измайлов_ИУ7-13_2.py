# вариант 1
n = int(input('Введите порядок матрицы: '))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input('Введите {}-ый элемент {}-ой строки: '.format(j + 1, i + 1))))

levels = n//2
for level in range(levels):
    if level % 2 != 0:
        start = level
        last = n - level - 1
        for i in range(start, last):
            deffrence = i - start
            top = matrix[start][i]
            matrix[start][i] = matrix[last - deffrence][start]
            matrix[last - deffrence][start] = matrix[last][last - deffrence]
            matrix[last][last - deffrence] = matrix[i][last]
            matrix[i][last] = top
            
print('Новая матрица:')
for i in range(n):
    for j in range(n):
        if matrix[i][j] >= 0:
            print(' {:<3}'.format(matrix[i][j]), end = '')
        else:
            print('{:<4}'.format(matrix[i][j]), end = '')
    print()

max_count = 0
result_column = -1
for j in range(n):
    col_sum = 0
    for i in range(n):
        col_sum += matrix[i][j]
    count = 0
    for k in range(n):
        if k == j:
            continue  # Пропускаем текущий столбец
        other_sum = 0
        for l in range(n):
            other_sum += matrix[l][k]
        if other_sum == col_sum:
            count += 1
    if count > max_count:
        max_count = count
        result_column = j

print(f'Столбец {max_count} есть искомый столбец:')
for i in range(n):
    print(matrix[i][max_count], end = ' ')