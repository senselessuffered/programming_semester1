'''Измайлов Михаил ИУ7-13Б
Программа для замены чисел на пробел все 4 показаны лаба 7'''
while True:
    a = input('Введите список: ').split() # ввод списка
    if a != []: break # проверка на наличие элементов в списке
    print('Повторите ввод')

for i in range(len(a)):
    new = '' # переменная для создания новой строки
    for letter in a[i]: # перебираем элементы в строке
        if letter.isdigit(): # проверяем что элемент строк это число
            new += ' ' # создаем новую строку
        else:
            new += letter # создаем новую строку
    a[i] = new # записываем новую строку
 
print(a) # выводим список