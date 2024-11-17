'''Измайлов Михаил ИУ7-13Б
Программа для вычисления интегралла способами правых прямоугольников и 3/8. Определить какой метод более точен'''
import math

# функция для вычисления значения в точке
def f(x):
    return x**2 

# функция для вычисления первообразной в точке
def F(x):
    return x**3/3

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
            a = float(input('Введите начало отрезка интегрирования: '))
            b = float(input('Введите конец отрезка интегрирования: '))
            N1 = int(input('Введите количество участков разбиения N1: '))
            N2 = int(input('Введите количество участков разбиения N2: '))
            delta_const = float(input('Введите заданную точность: '))
            if a < b and N1 > 0 and N2 > 0 and delta_const > 0: break
            print('Повторите ввод')
        except Exception as ex:
            print('Данные введены некорретно. Ошибка:', ex)
            print('Повторите ввод')

    # Вычисления для первого метода
    I1 = integral_method_right_rectangles(a, b, N1)
    I2 = integral_method_right_rectangles(a, b, N2)
    # Вычисления для второго метода
    I3 = integral_method_three_eighths(a, b, N1)
    I4 = integral_method_three_eighths(a, b, N2)

    # Вывод результатов в виде таблицы
    print('\nТаблица:')
    print('-'*31)
    print('|', ' '*7,'|N1' + ' '*6,'|N2' + ' '*6,'|')
    print(f'|{'Метод 1':<9}|{I1:<9.7g}|{I2:<9.7g}|')
    if I3 == None:
        print(f'|{'Метод 2':<9}|{'-':<9}|', end = '')
    else:
        print(f'|{'Метод 2':<9}|{I3:<9.7g}|', end  = '')
    if I4 == None:
        print(f'{'-':<9}|')
    else:
        print(f'{I4:<9.7g}|')
    print('-'*31)

    # Подсчет погрешности и вывод
    correct_value = F(b) - F(a)
    print()
    abs_err_I1, rel_err_I1 = calculate_errors(I1, correct_value)
    print('Вычисление 1')
    print(f'Абсолютная погрешность: {abs_err_I1:.7g}, Относительная погрешность: {rel_err_I1:.7g}')
    abs_err_I2, rel_err_I2 = calculate_errors(I2, correct_value)
    print('Вычисление 2')
    print(f'Абсолютная погрешность: {abs_err_I2:.7g}, Относительная погрешность: {rel_err_I2:.7g}')
    abs_err_I3, rel_err_I3 = calculate_errors(I3, correct_value) if I3 is not None else (math.inf, math.inf)
    print('Вычисление 3')
    if I3 != None:
        print(f'Абсолютная погрешность: {abs_err_I3:.7g}, Относительная погрешность: {rel_err_I3:.7g}')
    else:
        print('Неопределено')
    abs_err_I4, rel_err_I4 = calculate_errors(I4, correct_value) if I4 is not None else (math.inf, math.inf)
    print('Вычисление 4')
    if I4 != None:
        print(f'Абсолютная погрешность: {abs_err_I4:.7g}, Относительная погрешность: {rel_err_I4:.7g}')
    else:
        print('Неопределено')

    # Определение более точного метода подсчета
    answer = None
    best = math.inf
    if abs_err_I1 < best:
        answer = 'Метод правых прямоугольников с N1'
        best = abs_err_I1
    if abs_err_I2 < best:
        answer = 'Метод правых прямоугольников с N2'
        best = abs_err_I2
    if abs_err_I3 is not None and abs_err_I3 < best:
        answer = 'Метод 3/8 с N1'
        best = abs_err_I3
    if abs_err_I4 is not None and abs_err_I4 < best:
        answer = 'Метод 3/8 с N2'
        best = abs_err_I4

    # Вывод более точного метода
    print(f'\nНаиболее точный метод: {answer}')

    # вычисление количества разбиенния для менее точного метода
    worth = 'Метод правых прямоугольников' if 'Метод 3/8' in answer else 'Метод 3/8'
    if worth == 'Метод правых прямоугольников':
        if abs_err_I1 < abs_err_I2:
            N = N1
        else:
            N = N2
    else:
        if abs_err_I3 < abs_err_I4:
            N = N1
        else:
            N = N2
    while True:
        if worth == 'Метод правых прямоугольников':
            I_N = integral_method_right_rectangles(a, b, N)
            I_2N = integral_method_right_rectangles(a, b, 2 * N)
        else:
            I_N = integral_method_three_eighths(a, b, N)
            I_2N = integral_method_three_eighths(a, b, 2 * N)
        if abs(I_N - I_2N) < delta_const:
            break
        N *= 2
    
    # вывод
    print(f'\nДля метода {worth} требуется {N} участков разбиения для достижения заданной точности')
    print(f'Приближенное значение интеграла: {I_N:7g}')
    
if __name__ == "__main__":
    main()
