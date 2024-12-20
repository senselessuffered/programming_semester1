'Изиайлов Михаил ИУ7-13Б. Добавить удвоенный положительный элемент.'
import struct

# функция для удваивания четных чисел


def double_numbers(filename):
    add_count = 0
    with open(filename,'rb+') as f:
        while True:
            num = f.read(struct.calcsize('i'))
            if not num:
                break
            number = struct.unpack('i', num)[0]
            if number > 0:
                add_count += 1
        if add_count == 0:
            return
        f.seek(0,2)
        a = 1
        null_byte = struct.pack('i', a)

        for _ in range(add_count):
            f.write(null_byte)
       
        seek_one = -struct.calcsize('i')*(add_count+1)  
        seek_two = -struct.calcsize('i')  
        adds = 0

  
        while adds < add_count:
            f.seek(seek_one,2) 
            num = f.read(struct.calcsize('i'))
            if not num:
                break
            unpack_num = struct.unpack('i',num)
            number = unpack_num[0]
            if number <= 0:
                f.seek(seek_two,2)
                f.write(struct.pack('i',number))
                seek_one -= struct.calcsize('i')
                seek_two -= struct.calcsize('i')
            else:
                f.seek(seek_two,2)
                f.write(struct.pack('i',number*2))
                seek_two -= struct.calcsize('i')
                f.seek(seek_two,2) 
                f.write(struct.pack('i',number))
                seek_one -= struct.calcsize('i')
                seek_two -= struct.calcsize('i')
                adds += 1
                

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
