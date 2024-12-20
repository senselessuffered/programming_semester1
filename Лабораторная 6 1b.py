'''Измайлов Михаил ИУ7-13Б
Программа для добавления элемента в список по индексу алгоритмически'''
while True:
    a = list(map(float, input('Введите элементы списка: ').split())) # ввод списка
    if a != []: break
    print('Список должен быть не пуст. Повторите ввод')
element = input('Введите элемет, который хотите добавить: ') # ввод элемента
while True:
    index = int(input('Введите индекс места, куда хотите добавить элемент: ')) # ввод индекса
    if len(a)*(-1) <= index <= len(a): break
    print('Невозможно добавить элемент на это место. Повторите ввод')

a.append(None) # добавляем несуществующий элемент
for i in range(len(a) - 1, index - 1, -1): # перебираем индексы
    a[i] = a[i - 1] # обновляем индексы у элементов
a[i] = element # заменяем элемент

print(a) # вывод списка