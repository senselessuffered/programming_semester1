'''Измайлов Михаил ИУ7-13Б
Программа для среза массива'''
# ввод массива
x = 0
y = 0 
z = 0
array =[]
while not(x > 0 and y > 0 and z > 0):
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    z = int(input('Введите Z: '))
    if not(x > 0 and y > 0 and z > 0):
        print('Повторите ввод')
for i in range(x):
    array.append([])
    for j in range(y):
        array[i].append([])
        for k in range(z):
            array[i][j].append(input(f'Введите {k + 1}-ый элемент {j + 1}-ой строки d в {i + 1}-ом измерении: '))

shape = (x, y, z) # измерения
max_dimension = max(shape) # макимальное измерение
max_dimension_index = shape.index(max_dimension) # индекс макимального измерения
slice_index = shape[max_dimension_index] // 2 # вычисление индекса среза по условию
# срез взависимоти от измерения
if max_dimension_index == 0:
    sliced_array = [array[slice_index][y_0] for y_0 in range(y)]
elif max_dimension_index == 1:
    sliced_array = [array[x_0][slice_index] for x_0 in range(x)]
else:
    sliced_array = [array[x_0][y_0][slice_index] for x_0 in range(x) for y_0 in range(y)]

# Выводим исходный массив и срез
print(f"\nИсходный массив:")
print(array)
print(f"\nСрез массива по большему измерению {shape[slice_index]}:")
print(sliced_array)
