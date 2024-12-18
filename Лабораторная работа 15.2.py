'Изиайлов Михаил ИУ7-13Б. Добавить удвоенный положительный элемент.'
import struct
import os

# def double_numbers(filename):
#     temp_filename = filename + '.tmp'
#     with open(filename, 'rb') as input_file, open(temp_filename, 'wb') as output_file:
#         while True:
#             data = input_file.read(4)
#             if not data:
#                 break
#             number = struct.unpack('i', data)[0]
#             output_file.write(struct.pack('i', number))
#             if number > 0:
#                 doubled_value = number * 2
#                 output_file.write(struct.pack('i', doubled_value))

#     os.replace(temp_filename, filename)

# функция для удваивания четных чисел
def double_numbers(filename):
    with open(filename, 'r+b') as file:
        position = 0
        while True:
            file.seek(position)
            data = file.read(4)
            if not data:
                break

            number = struct.unpack('i', data)[0]
            position += 4
            if number > 0:
                doubled_value = number * 2
                file.seek(position)
                rest_of_file = file.read()
                file.seek(position)
                file.write(struct.pack('i', doubled_value))
                file.write(rest_of_file)
                position += 4


# функция для записи данных в файл
def write_to_file(filename, numbers):
    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(struct.pack('i', number))

# чтение из файла
def read_from_file(filename):
    numbers = []
    with open(filename, 'rb') as file:
        while byte := file.read(4):
            numbers.append(struct.unpack('i', byte)[0])
    return numbers

# основная функция
def main():
    filename = 'Файл для лабораторной 15.txt' # имя файла
    numbers = list(map(int, input('Введите через пробел числа: ').split()))

    print('Исходные числа:', numbers)
    
    write_to_file(filename, numbers)
    double_numbers(filename)

    print('Результат', read_from_file(filename))

if __name__ == '__main__':
    main()
