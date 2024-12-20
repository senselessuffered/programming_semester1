'Измайлов Михаил ИУ7-13Б. Реализация базы данных в байтовом формате'
import os
from termcolor import colored
from art import tprint
from sys import stdin
import string
import prettytable
import struct

# функция проверяет что в списке одиноковые типы данных


# представляет строку в байтовом виде


def uncode(line):
    length = struct.unpack('I', line[:4])[0]
    encoded_string = struct.unpack(f'{length}s', line[4:])[0]
    return encoded_string.decode('utf-8')

# представляет строку в байтовом виде


def code(line):
    encoded_string = line.encode('utf-8')
    return struct.pack(f'I{len(encoded_string)}s', len(encoded_string), encoded_string)

# функция, которая распределяет задачи взависимости от введенной программы


def editor(file, command):
    if command == 1:
        return choose_file(file)
    elif command == 2:
        file, e = work_with_database(file)
        os.system("cls")
        tprint('Work With Database')
        if e != None:
            print(colored(e, 'green', 'on_blue'))
        else:
            print(colored('Данные успешно занесены в файл', 'green', 'on_blue'))
        return file
    elif command == 3:
        display_as_table(file)
    elif command == 4:
        append_to_file(file)
    elif command == 5:
        search_in_file(file)
    elif command == 6:
        search_two_in_file(file)

# функция реализующая поиск по двум полям


def search_two_in_file(file):
    try:
        # проверка, что файл задан
        f = open(file)
        f.close()
        # ввод даных
        display_as_table(file)
        print('Введите данные для первого поля:')
        
        with open(file, 'rb') as f:
            headers = uncode(f.readline()).strip()
            delimeter = find_delimeter(headers)  # разделитель
            headers = headers.split(delimeter)
            
            # вывод меню для выбора поля
            for i, header in enumerate(headers):
                print(f'{i + 1} - {header}')
                
            field_index = int(input(colored('Введите номер поля, в котором производится поиск: ', 'green'))) - 1
            search_value = input(colored('Введите искомое значение: ', 'green'))
            
            print('Введите данные для второго поля:')
            for i, header in enumerate(headers):
                print(f'{i + 1} - {header}')
                
            field_index_1 = int(input(colored('Введите номер поля, в котором производится поиск: ', 'green'))) - 1
            search_value_1 = input(colored('Введите искомое значение: ', 'green'))
            
            os.system('cls')
            tprint('Work With Database')
            display_as_table(file)
            print()
            
            # проверка, что поиск возможен
            if field_index >= len(headers) or field_index_1 >= len(headers):
                raise Exception('Указанное значение поля не входит в заголовок')
            
            print(colored(f'Результаты поиска по полю {headers[field_index]} со значением {search_value} и по полю {headers[field_index_1]} со значением {search_value_1}:', 'blue'))
            
            # поиск совпадений
            for line in f:
                line = uncode(line)
                row = line.strip().split(delimeter)
                if row[field_index].lower() == search_value.lower() and row[field_index_1].lower() == search_value_1.lower():
                    print(colored(row, 'blue'))
    except FileNotFoundError:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Ошибка: файл не найден.', 'green', 'on_blue'))
    except Exception as e:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Произошла ошибка: {e}', 'green', 'on_blue'))

# функция реализующая поиск по одному полю


def search_in_file(file):
    try:
        # проверка, что файл задан
        f = open(file)
        f.close()
        # ввод данных
        display_as_table(file)
        with open(file, 'rb') as f:
            headers = uncode(f.readline()).strip()
            delimeter = find_delimeter(headers)  # разделитель
            headers = headers.split(delimeter)
            
            # вывод меню для выбора поля
            for i, header in enumerate(headers):
                print(f'{i + 1} - {header}')
                
            field_index = int(input(colored('Введите номер поля, в котором производится поиск: ', 'green'))) - 1
            search_value = input(colored('Введите искомое значение: ', 'green'))
            
            os.system('cls')
            tprint('Work With Database')
            display_as_table(file)
            print()
            
            # проверка, что поиск возможен
            if field_index >= len(headers):
                raise Exception('Указанное значение поля не входит в заголовок')
            
            print(colored(f'Результаты поиска по полю {headers[field_index]} со значением {search_value}:', 'blue'))
            
            # поиск совпадений
            for line in f:
                line = uncode(line)
                row = line.strip().split(delimeter)
                if row[field_index].lower() == search_value.lower():
                    print(colored(row, 'blue'))
    except FileNotFoundError:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Ошибка: файл не найден.', 'green', 'on_blue'))
    except Exception as e:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Произошла ошибка: {e}', 'green', 'on_blue'))

# функция вывода данных в таблицу


def display_as_table(file):
    try:
        with open(file, 'rb') as file:
            first_line = uncode(file.readline()).strip()
            delimeter = find_delimeter(first_line)
            headers = first_line.split(delimeter)
            table = prettytable.PrettyTable()
            table.field_names = headers
            for line in file:
                line1 = uncode(line)
                row = line1.strip().split(delimeter)
                table.add_row(row)
            os.system("cls")
            tprint('Work With Database')
            print(table)
    except FileNotFoundError:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Ошибка: файл не найден.', 'green', 'on_blue'))
    except Exception as e:
        os.system("cls")
        tprint('Work With Database')
        print(colored(f'Произошла ошибка: {e}', 'green', 'on_blue'))

# функция добавления новых строк в бд


def append_to_file(file):
    try:
        f = open(file)
        f.close()
        data = []

        display_as_table(file)

        print(colored('Введите данные, которые надо занести в базу данных (Для выхода используете ctrl+Z, а затем enter): ', 'green'))
        for line in stdin:
            data.append(line)

        with open(file, 'rb') as file1:
            headers = uncode(file1.readline()).strip()
            delimeter = find_delimeter(headers)
            length = len(headers.split(delimeter))
            existing_data = file1.readlines()

        if delimeter == 0:
            raise Exception('В заголовке нет разделителя')

        for line in data:
            if delimeter not in line or length != len(line.split(delimeter)):
                raise Exception('Новые строки не подходят для выбранной базы данных')

        # проверка на тип
        def get_data_type(value):
            try:
                int(value)
                return int
            except ValueError:
                try:
                    float(value)
                    return float
                except ValueError:
                    return str

        with open(file, 'rb') as file1:
            file1.readline()  # Skip headers
            for line in file1:
                row = uncode(line).strip().split(delimeter)
                for i, value in enumerate(row):
                    if get_data_type(value) != get_data_type(data[0].strip().split(delimeter)[i]):
                        raise Exception('Тип данных в новых строках не совпадает с существующими данными')

        insert_position = input(colored('Введите номер строки, куда занести данные (0 для добавления в конец): ', 'green'))
        insert_position = int(insert_position)

        if insert_position < 0 or insert_position > len(existing_data):
            raise Exception('Некорректный номер строки')

        with open(file, 'wb') as file:
            file.write(code(headers + '\n'))
            if insert_position == 0:
                file.writelines(existing_data)
                for line in data:
                    file.write(code(line))
            else:
                file.writelines(existing_data[:insert_position])
                for line in data:
                    file.write(code(line))
                file.writelines(existing_data[insert_position:])

        os.system('cls')
        tprint('Work With Database')
        print(colored(f'Данные успешно добавлены в файл', 'green', 'on_blue'))
    except Exception as e:
        os.system('cls')
        tprint('Work With Database')
        print(colored(f'Произошла ошибка при добавлении данных: {e}', 'green', 'on_blue'))

# функция задает рабочий файл


def choose_file(file):
    new_file = input(colored('Введите абсолютный путь до файла или none, чтобы перестать работать с файлом: ',
                     'green')).replace('\\', '/').strip('"')
    if new_file.lower() == 'none':
        os.system('cls')
        tprint('Work With Database')
        return None
    try:
        f = open(new_file)
        f.close()
        os.system('cls')
        tprint('Work With Database')
        return new_file
    except:
        os.system('cls')
        tprint('Work With Database')
        print(colored('Файл не найден', 'green', 'on_blue'))
        return file

# функция создает новую бд или перезаписывает рабочую


def work_with_database(file):
    errors = ['Неправильно введен путь до нового файла',
              'Разделитель не задан', 'Ошибка в данных', 'Тип данных в столбцах не совпадает']
    start_file = file

    try:
        f = open(file)
        f.close()
    except:
        name = input((colored('Введите абсолютный путь для файла: ', 'green'))).replace(
            '\\', '/').strip('"')
        if is_windows_absolute_path(name):
            file = name
        else:
            return file, errors[0]

    data = []

    print(colored('Введите данные, которые надо занести в базу данных (Для выхода используете ctrl+Z, а затем enter): ', 'green'))
    for line in stdin:
        data.append(line)

    is_note = True

    for line in data:
        if is_note:
            is_note = False
            delimeter = find_delimeter(line)
            length = len(line.split(delimeter))
            if delimeter == None:
                return start_file, errors[1]
        if delimeter not in line or length != len(line.split(delimeter)):
            return start_file, errors[2]

    # Проверка типов данных в столбцах
    def get_data_type(value):
        try:
            int(value)
            return int
        except ValueError:
            try:
                float(value)
                return float
            except ValueError:
                return str

    column_types = None
    for line in data[1:]:
        row = line.strip().split(delimeter)
        if column_types is None:
            column_types = [get_data_type(value) for value in row]
        else:
            for i, value in enumerate(row):
                if get_data_type(value) != column_types[i]:
                    return start_file, errors[3]

    with open(file, "wb") as file1:
        for line in data:
            file1.write(code(line))
    return file, None

# проверка, что строка является путем


def is_windows_absolute_path(path):
    if len(path) < 3 or path[1] != ':' or path[2] != '/':
        return False
    if not ('A' <= path[0].upper() <= 'Z'):
        return False
    forbidden_chars = set('\*?"<>|')
    for char in path:
        if char in forbidden_chars:
            return False
    return True

# функция ищет разделитель


def find_delimeter(line):
    punctuation = string.punctuation
    delimeter_counts = {}
    for sign in punctuation:
        delimeter_counts[sign] = line.count(sign)
    if max(delimeter_counts.values()) == 0:
        return None
    return max(delimeter_counts, key=delimeter_counts.get)

# основная функция


def main():
    menu = '''
    Меню:
    1 - выбрать файл для работы.
    2 - инициализировать базу данных.
    3 - вывести содержимое базы данных
    4 - добавить запись в базу данных
    5 - произвести поиск по одному полю
    6 - произвести поиск по двум полям
    Введите end для выхода из программы'''
    file_name = None  # путь до рабочего файла

    os.system('cls')
    print(colored('Добро пожаловать!!!', 'green', 'on_blue'))
    tprint('Work With Database')

    while True:
        print(colored(f'Рабочий файл:', 'green'), end=' ')
        if file_name == None:
            print(colored('файл не задан', 'red'))
        else:
            print(colored(file_name, 'red'))
        print(colored(menu, 'green'))

        try:
            command = input(colored('Введите цифру: ', 'red'))

            if command.lower() == 'end':
                break
            command = int(command)
            if not (0 < command < 7):
                raise Exception('Error: unsupported input')

            if 0 < command < 3:
                file_name = editor(file_name, command)
            elif 2 < command < 7:
                editor(file_name, command)
        except Exception as e:
            os.system('cls')
            tprint('Work With Database')
            print(colored(f'!!!Повторите ввод!!! Ошибка: {e}', 'red'))


if __name__ == '__main__':
    main()
