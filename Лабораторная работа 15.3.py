'Измайлов Михаил ИУ7-13Б. Быстрая сортировка.'
import struct

# функция для сортировки
def part(file, low, high):
    with open(file, 'rb+') as f:
        f.seek(high * 4)
        pivot = struct.unpack('i', f.read(4))[0]

        i = low - 1
        for j in range(low, high):
            f.seek(j * 4)
            num = struct.unpack('i', f.read(4))[0]

            if num < pivot:
                i += 1
                f.seek(i * 4)
                num_i = struct.unpack('i', f.read(4))[0]
                f.seek(j * 4)
                f.write(struct.pack('i', num_i))

                f.seek(i * 4)
                f.write(struct.pack('i', num))
        f.seek((i + 1) * 4)
        num_i1 = struct.unpack('i', f.read(4))[0]
        f.seek(high * 4)
        f.write(struct.pack('i', num_i1))

        f.seek((i + 1) * 4)
        f.write(struct.pack('i', pivot))

    return i + 1

def quicksort(file, low, high):
    if low < high:
        pi = part(file, low, high)
        quicksort(file, low, pi - 1)
        quicksort(file, pi + 1, high)

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
    quicksort(filename, 0, len(numbers) - 1)

    print('Результат:', read_from_file(filename))

if __name__ == '__main__':
    main()
