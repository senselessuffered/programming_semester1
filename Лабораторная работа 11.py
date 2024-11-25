'''Измайлов Михаил ИУ7-13Б
Быстрая сортировка'''
import time
import random

# алгоритм быстрой сортировки
def quicksort(arr, start = 0, end = None):
    global steps
    if len(arr) == 0:
        return arr
    base_index = random.randint(start, end - 1)
    base_element = arr[base_index]
    center = [x for x in arr if x == base_element]
    left = [x for x in arr if x < base_element]
    right = [x for x in arr if x > base_element]
    steps = steps + (len(right) + len(left))
    return quicksort(left, 0, len(left)) + center + quicksort(right, 0, len(right))
    
# ввод списка
while True:    
    try:
        a = list(map(int, input('Введите элементы массива через пробел: ').split()))
        if a == []:
            raise Exception('The list must contain elements')
        break
    except Exception as e:
        print('Повторите ввод. Ошибка:', e)

# вывод отсортированного списка
steps = 0
print('Отсортированный список: ', quicksort(a, 0, len(a)))

# ввод данных о размерностях
while True:
    try:
        if 'n1' not in locals():
            n1 = int(input('Введите первую длину массива: '))
            if n1 <= 0:
                del n1
                raise Exception('The step must be positive')
        if 'n2' not in locals():
            n2 = int(input('Введите вторую длину массива: '))
            if n2 <= 0:
                del n2
                raise Exception('The step must be positive')
        if 'n3' not in locals():
            n3 = int(input('Введите третью длину массива: '))
            if n3 <= 0:
                del n3
                raise Exception('The step must be positive')
        break
    except Exception as e:
        print('Повторите ввод. Ошибка:', e)
n = [n1, n2, n3]

#вывод легенды
print('-'*118)
print('|', ' '*12, '|', f'{'N1':^31}', '|', f'{'N2':^31}', '|', f'{'N3':^31}', '|')
print('-'*118)
print('|', ' '*12, '|', end = '')
for _ in range(3):
    print(f'{' время':<17}', '|', f'{'перестановки'}', '|', end = '')
print()
print('-'*118)

# вывод данных об упорядоченном списке
print('| Упорядоченный', end = '| ')
for i in range(3):
    a = []
    for _ in range(n[i]):
        a.append(random.randint(-100_000, 100_000))
    a = sorted(a)
    start = time.time()
    steps = 0
    quicksort(a, 0, len(a))
    delta = time.time() - start
    print(f'{delta:<16.5g}', '|', f'{steps:<12.7g}', '|', end = ' ')
print()
print('|', f'{'список':<12}', end = ' |')
for _ in range(3):
    print(f'{'':<17}', '|', f'{'':<12}', '|', end = '')
print()
print('-'*118)

# вывод данных о случайном списке
print('|', f'{'Случайный':<12}', end = ' | ')
for _ in range(3):
    a = []
    for _ in range(n[i]):
        a.append(random.randint(-100_000, 100_000))
    start = time.time()
    steps = 0
    quicksort(a, 0, len(a))
    delta = time.time() - start
    print(f'{delta:<16.5g}', '|', f'{steps:<12.7g}', '|', end = ' ')
print()
print('|', f'{'список':<12}', end = ' |')
for _ in range(3):
    print(f'{'':<17}', '|', f'{'':<12}', '|', end = '')
print()

# вывод данных о случайном списке
print('-'*118)
print('|', f'{'Реверсивный':<12}', end = ' | ')
for _ in range(3):
    a = []
    for _ in range(n[i]):
        a.append(random.randint(-100_000, 100_000))
    a = sorted(a)[::-1]
    start = time.time()
    steps = 0
    quicksort(a, 0, len(a))
    delta = time.time() - start
    print(f'{delta:<16.5g}', '|', f'{steps:<12.7g}', '|', end = ' ')
print()
print('|', f'{'список':<12}', end = ' |')
for _ in range(3):
    print(f'{'':<17}', '|', f'{'':<12}', '|', end = '')
print()
print('-'*118)
