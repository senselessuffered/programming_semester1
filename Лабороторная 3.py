"""Измайлов Михаил ИУ7-13Б
Программа для вычисления медианы, сторон и расстояния до точки у треугольника."""
import math

# ввод координат точек
x1 = float(input('Введите координату x точки 1: '))
y1 = float(input('Введите координату y точки 1: '))
x2 = float(input('Введите координату x точки 2: '))
y2 = float(input('Введите координату y точки 2: '))
x3 = float(input('Введите координату x точки 3: '))
y3 = float(input('Введите координату y точки 3: '))

# вычисление расстояний между точками(стороны треугольника)
side_a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
side_b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
side_c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
# проверка на существование треугольника
if (side_b + side_a > side_c and side_c + side_a > side_b and side_b + side_c > side_a 
    and not(math.isclose(side_b + side_a, side_c) or math.isclose(side_b + side_c, side_a) or math.isclose(side_c + side_a, side_b))):
    side_mx = max(side_a, side_b, side_c) # поиск длины самой большой стороны
    median = 0.5 * (2 * side_a**2 + 2 * side_c**2 + 2 * side_b**2 - 3 * side_mx**2)**0.5 # вычисление медианы

    # вывод сторон треугольника, медианы и проверка на равнобедренность
    print(f'\nСторона 1 треугольника: {side_a:.7g}')
    print(f'Сторона 2 треугольника: {side_b:.7g}')
    print(f'Сторона 3 треугольника: {side_c:.7g}')
    print(f'Длина медианы из большего угла: {median:.7g}')
    if ((math.isclose(side_a, side_b) and (not math.isclose(side_b,side_c))) 
        or ((not math.isclose(side_b, side_a)) and math.isclose(side_b, side_c)) 
        or ((not math.isclose(side_b, side_a)) and math.isclose(side_a, side_c))):
        print('Треугольник является равнобедренным')
    else:
        print('Треугольник не является равнобедренным')

    # ввод координат проверяемой точки
    x = float(input('\nВведите координату x: '))
    y = float(input('Введите координату y: '))

    # вычисление расстояний от введенной точки до вершин треугольника
    newside_a = ((x1 - x)**2 + (y1 - y)**2)**0.5
    newside_b = ((x2 - x)**2 + (y2 - y)**2)**0.5
    newside_c = ((x - x3)**2 + (y - y3)**2)**0.5
    p1 = 0.5*(newside_a + newside_b + side_a) # подсчет полупериметра
    s1 = (p1*(p1 - newside_a)*(p1 - newside_b)*(p1 - side_a))**0.5 # расчет площади по формуле герона
    p2 = 0.5*(newside_a + newside_c + side_c) # подсчет полупериметра
    s2 = (p2*(p2 - newside_c)*(p2 - newside_a)*(p2 - side_c))**0.5 # расчет площади по формуле герона
    p3 = 0.5*(newside_c + newside_b + side_b) # подсчет полупериметра
    s3 = (p3*(p3 - newside_c)*(p3 - newside_b)*(p3 - side_b))**0.5 # расчет площади по формуле герона
    new_s = s1 + s2 + s3 # подсчет суммы площадей треугольников с вершинами в вводимой точке
    p_original = 0.5*(side_a + side_b + side_c) # подсчет полупериметра
    s_original = (p_original*(p_original - side_a)*(p_original - side_b)*(p_original - side_c))**0.5 # расчет площади по формуле герона
    if math.isclose(new_s, s_original): # проверка на принадлежность точки области треугольника
        print('\nТочка принадлежит треугольнику') # вывод информации о принадлежности точки треугольнику
        # вычисления расстояний от точки до сторон треугольника
        h_a = s1*2/side_a
        h_b = s3*2/side_b
        h_c = s2*2/side_c
        h = min(h_a, h_b, h_c) # поиск минимального расстояния
        print(f'Кратчайшее расстояние от точки до стороны треугольника: {h:.7g}') # вывод минимального расстояния
    else:
        print('\nТочка вне треугольника') # вывод информации о принадлежности точки треугольнику
else:
    print('Такого треугольника не существует') # вывод информации, что треугольника с такими координатами не существует