'''Измайлов Михаил ИУ7-13Б
Программа для поиска экстремума'''
while True:
    a = list(map(float, input('Введите элементы списка: ').split())) # ввод списка
    if a != []: break
    print('Список должен быть не пуст. Повторите ввод')
while True:
    k = int(input('Введите номер экстремума: ')) # ввод номера
    if 0 < k: break
    print('В введенном списке не может быть экстремума с таким номером. Повторите ввод')

# ищем экстремумы
count = 1 # переменная для подсчета номера экстремума
check = True # переменная для проверки вывода экстремума
for i in range(1, len(a) - 1): 
    if ((a[i] < a[i - 1]) and (a[i] < a[i + 1])) or ((a[i] > a[i - 1]) and (a[i] > a[i + 1])):
        if k == count: 
            print(f'{k}-ый экстремум: {a[i]}')
            check = False
            break
        count += 1
if check:
    print('Не найдено экстремумов с введенным номером')