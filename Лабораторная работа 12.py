"Измайлов Михаил ИУ7-13Б. Реализация текстового процессора"
# импорт библиотек
import os
from termcolor import colored


# функция вывода текста
def output(text, mode=1):
    print("~"*201)  # печатем гарницу
    # вывод текста при режиме выравнивания влево
    if mode == 1:
        for line in text:
            print(f"{line:<201}")
    # вывод текста при режиме выравнивание вправо
    elif mode == 2:
        for line in text:
            print(f"{line:>201}")
    # вывод текста при режиме выравнивание по ширине
    elif mode == 3:
        for line in text:
            words = line.split()
            if len(words) == 1:
                print(f"{line:<201}")
            else:
                total_length = sum(len(word) for word in words)
                spaces_needed = 201 - total_length
                amount = len(words) - 1
                min_space = spaces_needed // amount
                extra_space = spaces_needed % amount
                new_line = ""
                for i in range(len(words)):
                    new_line += words[i]
                    if i < amount:
                        new_line += ' ' * \
                            (min_space + (1 if i < extra_space else 0))
                print(new_line)
    print("~"*201)  # печатаем границу


# функция-распорядитель команд редактирования
def editor(text, command):
    if command == 4:
        return word_deletion(text)
    elif command == 5:
        return word_replacement(text)
    elif command == 6:
        math_operations(text)
    elif command == 7:
        start, end = find_max_sentence(text)
        if start[0] != len(text):  # проверка на наличие предложений в тексте
            # перезаписывание текста без найденного самого большого предложения
            new_text = []
            is_add = True
            for i in range(len(text)):
                new_line = ''
                for j in range(len(text[i].split())):
                    line = text[i].split()
                    if start[0] == i and start[1] == j:
                        is_add = False
                    if is_add:
                        new_line += line[j] + ' '
                    if end[0] == i and end[1] == j:
                        is_add = True
                if new_line != '':
                    new_text.append(new_line)
            return new_text
        else:
            print("В тексте нет предложений.")
            return text

# функция подсчитывает значение математических выражений


def math_operations(text):
    mathematical_expressions = []  # для хранения строк вида [0-9]*[!+%/]![0-9]*
    expression = ""  # переменная для хранения выражения

    for i in range(len(text)):
        for j in range(len(text[i])):
            # проверка что мы добавляем цифру и выражение не начинается со знака
            if text[i][j].isdigit() or (text[i][j] in ":/%+" and expression != ""):
                expression += text[i][j]
            elif text[i][j] != " ":  # игнорируем пробелы
                if expression != "":  # если не пустая строка то сохраняем
                    # удаляем все знаки в начале
                    while expression[-1] in ":/+%":
                        expression = expression[:-1]
                    mathematical_expressions.append(expression)
                    expression = ""

    if mathematical_expressions != []:  # проверка на наличие выражений в тексте
        for expression in mathematical_expressions:
            # разбиваем на те чати которые надо сложить
            new_expression = expression.split("+")
            if len(new_expression) > 1 or (":" in new_expression[0]) or ("/" in new_expression[0]) or ("%" in new_expression[0]):
                for i in range(len(new_expression)):
                    # части в которых есть знак деления делим и записываем их результат
                    new_expression[i] = new_expression[i].replace(
                        "%", "/").replace(":", "/")
                    if "/" in new_expression[i]:
                        new_expression_0 = new_expression[i].split("/")
                        del_0 = float(new_expression_0[0])
                        for element in new_expression_0[1:]:
                            del_0 /= float(element)
                        new_expression[i] = del_0

                # складываем части
                result = 0
                for element in new_expression:
                    result += float(element)

                print(expression, "=", f"{result:.7g}")
    else:
        print("Нужные выражения отсутствуют.")

# функция поиск максимального по количеству слов предложения


def find_max_sentence(text):
    longest = ""  # хранит максимальное предложение
    count_mx = 0  # максимальное количество слов
    count = 0  # количество слов в данном предложение
    sentence = ""  # данное предложение
    # списки для храниения индексов первого и последенего слова в макимальном предложении
    start = [len(text), 10]
    end = [len(text), 10]

    for i in range(len(text)):
        line = text[i].split()  # делим текст на строки
        for j in range(len(text[i].split())):
            if sentence == '':
                # храним индекс первого слова
                start_ind = str(i) + " " + str(j)
            sentence += line[j] + ' '  # добавляем остальные слова
            if line[j] not in '-+/*%':  # знаки не учитываем как слова
                count += 1
            if sentence[-2] in '!?.':  # проерка на конец предложения
                if count > count_mx:
                    count_mx = count
                    longest = sentence
                    start = list(map(int, start_ind.split()))
                    end = [i, j]
                count = 0
                sentence = ''

    print(colored("Предложение с наибольшим количеством слов:", "red", "on_green"))
    print(longest)
    return start, end

# функция замена слова


def word_replacement(text):
    word = input(
        colored("Введите какое слово в тексте стоит заменить: ", "red"))
    new_word = input(colored(
        "Введите на какое слово в тексте стоит заменить, раннее введенное слово: ", "red"))
    new_text = []  # список для нового варианта текста

    for line in text:
        words = line.split()
        new_line = ''
        for i in range(len(words)):
            count = 0
            for j in range(len(word)):
                if len(words[i]) >= len(word):
                    if word[j].lower() == words[i][j].lower():
                        count += 1
                else:
                    break
            if count == len(word):
                if len(words[i]) > len(word):
                    if not words[i][len(word)].isalpha():
                        new_line += new_word + words[i][len(word):] + ' '
                    else:
                        new_line += words[i] + ' '
                else:
                    new_line += new_word + ' '
            else:
                new_line += words[i] + ' '
        new_text.append(new_line[:-1])
    return new_text

# функция удвления слова


def word_deletion(text):
    word = input(
        colored("Введите какое слово в тексте стоит удалить: ", "red"))
    new_text = []  # список с новым вариантом текста

    for line in text:
        words = line.split()
        new_line = ''
        for i in range(len(words)):
            count = 0  # количество совпадений с буквами искомого слова
            for j in range(len(word)):
                if len(words[i]) >= len(word):
                    if word[j].lower() == words[i][j].lower():
                        count += 1
                else:
                    break
            if count == len(word):
                if len(words[i]) > len(word):
                    # проверка что слово не является чатью слова
                    if not words[i][len(word)].isalpha():
                        new_line += words[i][len(word):] + ' '
                    else:
                        new_line += words[i] + ' '
                else:
                    new_line += ''
            else:
                new_line += words[i] + ' '
        new_text.append(new_line[:-1])
    return new_text

# основная функция


def main():
    text = [
        "Понимаешь - сказал мне знакомый волшебник, п3* 1рикурив сигарету от лунного света - жизнь нельзя запихнуть даже в толстый учебник,",
        "ведь на каждый вопрос не напишешь ответа. Да ещё эта грань между “просто” и “сложно” почему-то практически неуловима - из всего, что нам хочется, хоть и возможно,",
        "но обычно сбывается лишь полов-7ина. Тут32/8 волшебная палочка, в общем-то, кстати - можешь стать королём. Или модным поэтом. И не жить как всегда от зарплаты к зарплате,",
        "И творить только то, что захочешь, при этом! Ну, ещё по одной? И, наверное, хватит Счастье, в принципе, людям нужнее, чем что-то. Почему кто-то жизнь так бессмысленно",
        "тратит? А не жалко, к//665/5+21огда в ней – тоска и+5 болото! Посмотри, что творится от века до века – нам всегда быть счастливыми что-то мешает",
        "вот скажи мне, зачем Бог слепил человека? - где народ создаёт, там толпа разруш5  +  3/3//:ает! Ты мне нравишься, парен молчишь и киваешь. Мир спасают не люди, спасают",
        "святые. А тебе не дано. Так о чём ты мечтаешь? Загадай, и стань тем, кем не станут другие. А “Тверская” пошла, сладко греет, зар-раза! Ну, ещё по",
        "чуть-чуть так сказать - отход52%52ную? И/ 23+23: 12-32// запомни… мечту не исполнить два раза, но одну я 5-2 и пьяным тебе наколдую.",
    ]

    menu = """Меню:
    1 - выровнять текст по левому краю.
    2 - выровнять текст по правому краю.
    3 - выровнять текст по ширине.
    4 - удаление всех вхождений заданного слова.
    5 - замена одного слова другим во всём тексте.
    6 - вычисление арифметических выражений над целыми числами внутри текста (деление и сложение).
    7 - Найти и затем удалить предложение с наибольшим количеством слов.
    Введите end, чтобы выйти из программы."""

    os.system("cls")
    print(colored(
        "Добро пожаловать в редактор!!! Текст по умолчанию выровнят по левому краю.", "red"))
    output(text)

    # приемник команд
    while True:
        print(colored(menu, "green"))
        try:
            command = input(colored("Введите цифру: ", "red"))
            if command.lower() == 'end':
                break
            command = int(command)
            if not (0 < command < 8):
                raise Exception("Error: unsupported input")
            os.system("cls")
            if 0 < command < 4:
                mode = command
            elif 3 < command < 6 or command == 7:
                if len(text) != 0:
                    text = editor(text, command)
                else:
                    print(colored("Весь текст удален", "red"))
            else:
                editor(text, command)
            if "mode" in locals():
                output(text, mode)
            else:
                output(text)
        except Exception as e:
            os.system("cls")
            print(colored(f"!!!Повторите ввод!!! Ошибка: {e}", "red"))
            if "mode" in locals():
                output(text, mode)
            else:
                output(text)


if __name__ == "__main__":
    main()
