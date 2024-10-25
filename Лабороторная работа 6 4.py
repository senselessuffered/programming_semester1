'''Измайлов Михаил ИУ7-13Б
Программа для поиска последовательности'''
while True:
    a = list(map(int, input('Введите элементы списка: ').split())) # ввод списка
    if a != []: break
    print('Список должен быть не пуст. Повторите ввод')

# решето эратосфена
n = abs(max(a, key = abs))
primes = [True for _ in range(n + 1)]
for k in range(2, int(n**0.5) + 1):
    if primes[k]:
        for i in range(k**2, n + 1, k):
            primes[i] = False
primes[1] = False

longest_start = 0
longest_end = 0
current_start = 0
current_end = 0
for i in range(len(a)): # перебираем числа
    if a[i] < 0 and primes[abs(a[i])]: # проверка подходит ли число под условие
        if (current_end == current_start) or a[i] < a[current_end]: # проверка можно ли число добавить в последовательность
            current_end += 1 # добавляем число в последовательность
        else:
            if (current_end - current_start) > (longest_end - longest_start): # проверка на максимум длины последовательности
                longest_start = current_start
                longest_end = current_end
            current_start += i # создаем новую последовательность
            current_end = i + 1
    else:
        if (current_end - current_start) > (longest_end - longest_start): # проверка на максимум длины последовательности
            longest_start = current_start
            longest_end = current_end
        current_start = i # создаем новую последовательность
        current_end = i
if (current_end - current_start) > (longest_end - longest_start): # проверка на максимум длины последовательности
    longest_start = current_start
    longest_end = current_end

# вывод
if longest_end == longest_start == 0:
    print('Такой последовательности нет в введенном списке')
else:
    print('Последовательность:', a[longest_start + 1:longest_end + 1])
    print('Длина:', longest_end - longest_start)