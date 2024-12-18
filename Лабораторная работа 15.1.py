'Измайлов Михаил ИУ7-13Б. Удаление всех нечетных элементов.'
import struct

# функция удаления нечетных чисел
def remove_numbers(filename):
    with open(filename, 'rb+') as file:
        position = 0
        while byte := file.read(4):
            number = struct.unpack('i', byte)[0]
            old_position = file.tell()
            if number % 2 == 0:
                old_position = file.tell()
                file.seek(position)
                file.write(struct.pack('i', number))
                position += 4
                file.seek(old_position)
        file.truncate(position)

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

def main():
    filename = 'Файл для лабораторной 15.txt' # имя файла
    numbers = list(map(int, input('Введите через пробел числа: ').split()))

    print('Исходные числа:', numbers)
    
    write_to_file(filename, numbers)
    remove_numbers(filename)

    print('Результат:', read_from_file(filename))

if __name__ == '__main__':
    main()
