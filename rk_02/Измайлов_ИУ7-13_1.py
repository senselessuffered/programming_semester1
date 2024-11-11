'''
Отладка программы - процесс выявления ошибок в программе и их исправление. 
Методы:
1) Проверка на разных входных данных
2) Попытка разобраться в ошибке которую выдает консоль
3) Пробежаться по коду глазами и выявить аналитически ошибку
4) Попросить нейросеть испаравить код
'''
# Вариант 1
a = list(map(int, input('Введите через пробел элементы первого массива: ').split()))
b = list(map(int, input('Введите через пробел элементы второго массива: ').split()))

c = []
last_a = 0
last_b = 0
while last_a < len(a) or last_b < len(b):
    if last_a < len(a) and last_b < len(b):
        if a[last_a] < b[last_b]:
            c.append(a[last_a])
            last_a += 1
        elif a[last_a] == b[last_b]:
            c.append(a[last_a])
            last_a += 1
            c.append(b[last_b])
            last_b += 1
        else:
            c.append(b[last_b])
            last_b += 1
    elif last_a < len(a):
        c.append(a[last_a])
        last_a += 1
    elif last_b < len(b):
        c.append(b[last_b])
        last_b += 1
print('Новый массив:', c)
ind_1 = 0 #  индекс минимальный четный
ind_2 = 0 #  индекс максимального нечетного
for i in range(len(c)):
    if (c[i] > c[ind_2] and c[i] % 2 != 0) or (c[i] % 2 != 0 and c[ind_2] % 2 == 0):
        ind_2 = i
    if (c[i] < c[ind_1] and c[i] % 2 == 0) or (c[i] % 2 == 0 and c[ind_1] % 2 != 0):
        ind_1 = i
if c[ind_1] % 2 == 0 and c[ind_2] % 2 != 0:
    c[ind_1], c[ind_2] = c[ind_2], c[ind_1]
    print('Измененный новый массив: ', c)
else:
    print('Нет подходящих элементов')

               
