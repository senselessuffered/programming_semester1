'''Измайлов Михаил ИУ7-13Б
Программа для поиска элемента в списке строк'''
while True:
    a = input('Введите список: ').split() # ввод списка
    if a != []: break # проверка на наличие элементов в списке
    print('Повторите ввод')

max_string = '' # переменная для хранения максимальной строки
for string in a:
    if not any(letter.isdigit() for letter in string): # проверка на наличие цифр в строке
        if len(string) > len(max_string): # сравниваем длину строки с длиной ранее найденной максимальной строки
            max_string = string # перезаписываем строку
if max_string == '':
    print('Строка не найдена')
else:
    print(max_string) # вывод найденной строки