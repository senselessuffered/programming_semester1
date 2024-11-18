'''Измайлов Михаил ИУ7-13Б
Программа для вычисления интегралла способами правых прямоугольников и 3/8. Определить какой метод более точен'''
import math

# функция для вычисления значения в точке
def f(x):
    return math.log(x)

# функция для вычисления первообразной в точке
def F(x):
    return x*(math.log(x) - 1)

# метод правых прямоугольников
def integral_method_right_rectangles(a, b, n):
    h = (b - a) / n # вычисление высоты
    integral = 0 # создаем переменную для хранения интегралла
    for i in range(1, n + 1):
        integral += f(a + i * h)
    integral *= h
    return integral

# метод 3/8
def integral_method_three_eighths(a, b, n):
    if n % 3 != 0:
        return None  # метод 3/8 требует, чтобы n было кратно 3
    h = (b - a) / n # вычисление шага   
    integral = f(a) + f(b) # перерменная для хранения интегралла
    for i in range(1, n):
        if i % 3 == 0: # проверяем что в промежутке набралось 4 числа
            integral += 2 * f(a + i * h) # дублируем число так как оно являеся началом и концом промежутков
        else:
            integral += 3 * f(a + i * h) # прибавляем по формуле
    integral *= (3 * h / 8)
    return integral

# функция для вычисления абсолютной и относительной погрешности
def calculate_errors(I_n, true_value):
    absolute = abs(I_n - true_value)
    relative = absolute / abs(true_value) if true_value != 0 else math.inf
    return absolute, relative

def main():
    # Ввод данных
    while True:
        try:
            if 'a' not in locals() or 'b' not in locals():
                a = float(input('Введите начало отрезка интегрирования: '))
                try:
                    f(a)
                    F(a)
                except Exception as ex:
                    del a
                    raise Exception(ex)
                b = float(input('Введите конец отрезка интегрирования: '))
                try:
                    f(b)
                    F(b)
                except Exception as ex:
                    del b
                    raise Exception(ex)
                if a >= b:
                    del a
                    del b
                    raise Exception('Error: a must be less than b')
            if 'n1' not in locals():
                n1 = int(input('Введите количество участков разбиения n1: '))
                if n1 <= 0:
                    del n1
                    raise Exception('Error: n1 must be positive')
            if 'n2' not in locals():
                n2 = int(input('Введите количество участков разбиения n2: '))
                if n2 <= 0:
                    del n2
                    raise Exception('Error: n2 must be positive')
            if 'delta_const' not in locals():
                delta_const = float(input('Введите заданную точность: '))
                if delta_const <= 0:
                    del delta_const
                    raise Exception('Error: accuracy must be positive')
            break
        except Exception as ex:
            print('Данные введены некорретно. Ошибка:', ex)
            print('Повторите ввод')

    # Вычисления для первого метода
    i1 = integral_method_right_rectangles(a, b, n1)
    i2 = integral_method_right_rectangles(a, b, n2)
    # Вычисления для второго метода
    i3 = integral_method_three_eighths(a, b, n1)
    i4 = integral_method_three_eighths(a, b, n2)

    # Вывод результатов в виде таблицы
    print('\nТаблица:')
    print('-'*31)
    print('|', ' '*7,'|n1' + ' '*6,'|n2' + ' '*6,'|')
    print(f'|{'Метод 1':<9}|{i1:<9.7g}|{i2:<9.7g}|')
    if i3 == None:
        print(f'|{'Метод 2':<9}|{'-':<9}|', end = '')
    else:
        print(f'|{'Метод 2':<9}|{i3:<9.7g}|', end  = '')
    if i4 == None:
        print(f'{'-':<9}|')
    else:
        print(f'{i4:<9.7g}|')
    print('-'*31)

    # Подсчет погрешности и вывод
    correct_value = F(b) - F(a)
    print()
    abs_err_i1, rel_err_i1 = calculate_errors(i1, correct_value)
    print('Вычисление 1')
    print(f'Абсолютная погрешность: {abs_err_i1:.7g}, Относительная погрешность: {rel_err_i1:.7g}')
    abs_err_i2, rel_err_i2 = calculate_errors(i2, correct_value)
    print('Вычисление 2')
    print(f'Абсолютная погрешность: {abs_err_i2:.7g}, Относительная погрешность: {rel_err_i2:.7g}')
    abs_err_i3, rel_err_i3 = calculate_errors(i3, correct_value) if i3 is not None else (math.inf, math.inf)
    print('Вычисление 3')
    if i3 != None:
        print(f'Абсолютная погрешность: {abs_err_i3:.7g}, Относительная погрешность: {rel_err_i3:.7g}')
    else:
        print('Неопределено')
    abs_err_i4, rel_err_i4 = calculate_errors(i4, correct_value) if i4 is not None else (math.inf, math.inf)
    print('Вычисление 4')
    if i4 != None:
        print(f'Абсолютная погрешность: {abs_err_i4:.7g}, Относительная погрешность: {rel_err_i4:.7g}')
    else:
        print('Неопределено')

    # Определение более точного метода подсчета
    answer = None
    best = math.inf
    if abs_err_i1 < best:
        answer = 'Метод правых прямоугольников с n1'
        best = abs_err_i1
    if abs_err_i2 < best:
        answer = 'Метод правых прямоугольников с n2'
        best = abs_err_i2
    if abs_err_i3 is not None and abs_err_i3 < best:
        answer = 'Метод 3/8 с n1'
        best = abs_err_i3
    if abs_err_i4 is not None and abs_err_i4 < best:
        answer = 'Метод 3/8 с n2'
        best = abs_err_i4

    # Вывод более точного метода
    print(f'\nНаиболее точный метод: {answer}')

    # вычисление количества разбиенния для менее точного метода
    worth = 'Метод правых прямоугольников' if 'Метод 3/8' in answer else 'Метод 3/8'
    if worth == 'Метод правых прямоугольников':
        if abs_err_i1 < abs_err_i2:
            n = n1
        else:
            n = n2
    else:
        if abs_err_i3 < abs_err_i4:
            n = n1
        else:
            n = n2
    while True:
        if worth == 'Метод правых прямоугольников':
            i_n = integral_method_right_rectangles(a, b, n)
            i_2n = integral_method_right_rectangles(a, b, 2*n)
        else:
            i_n = integral_method_three_eighths(a, b, n)
            i_2n = integral_method_three_eighths(a, b, 2*n)
        if (i_n != None) and (i_2n != None):
            if abs(i_n - i_2n) < delta_const:
                break
        n *= 2
        
    # вывод
    print(f'\nДля метода {worth} требуется {n} участков разбиения для достижения заданной точности')
    print(f'Приближенное значение интеграла: {i_n:.7g}')
    
if __name__ == "__main__":
    main()
