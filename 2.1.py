#  как считыввать данные из файла
#
#
#  Функция open позволяет открыть и прочитать информацию из файла
#  Принемает на фход два аргумента, путь к файлу и режим использования
#
#
#
#
# (read) считывает весь фаул как одну большуб строку
#  (readlines) считывает файл как список, где каждый элменет списка одна строка
#  (write) позволяет записать текстовую перменную в файл
#  (close) закрывает файл
#
#  Режимы в котором можно отркыть  файл
#  Режим Обозначение
#  'r' открытие на чтение
#  'w' открытие на запись, содержимое файла удаляется, если файла не существует,
#  создается новый.
#  'x' открытие на запись, если файла не существует, иначе исключение
#  'a' открытие на дозапись, информация добавляется в конец файла
# 'b' открытие в бинарном режиме(документы Word и exel бинарные)
# 't' открытие в текстовом режиме(по умолчанию)
#  'r+' открытие на дозапись, изначально смотрим на начало файла


# import json
#
# with open("text/sample.json", "r") as read_file:
#     data = json.load(read_file)
#
# my_file = open("text/sample.txt", "r").readlines()
#
# print(my_file[0])
#
#
# ff = open('copy.txt', 'w')
# ff.write(my_file)
# ff.close()


# import json
#
# with open("text/sample.json", "r") as read_file:
#     data = json.load(read_file)
#
# my_file = open("text/sample.txt", "r").read()
# ff = open('copy.txt', 'x')
# # ff.write(my_file)
# # ff.close()
#
# ff.close()


# json.load() - метод считываеь файл в формате json и возращает объекты Python
#
# json.loads() - метод считывает строку в формате JSON и возращает объекты Python
#
# json.dump() - метод записывает объект Python в файл в формает JSON и
#
# json.dumps() - метод возращает строку в формате JSON и


#
# import json
#
# with open("text/sample.json", "r") as read_file:
#     data = json.load(read_file)
# print(data)
#
#
# json.dump(data,open('copy.json','x'))

# ff.close()


# import json


# функция которая принимает на вход путь к текстовому файлу и возвращает его содержимое

# zadanie 2 zadanie 2-1

def read_entire_file(path2file):
    text = open(path2file, "r").read()
    print(text)
    return 0


path2file = "text/sample.txt"
read_entire_file(path2file)

# zadanie 2 zadanie 2-2

# функция которая принимает на вход путь к текстовому файлу и число n и возвращает первые n строк
def read_first_n_lines(path2file, n):
    my_file = open(path2file, "r").readlines()
    for n in range(0,n,1):
        print(my_file[n])
    # чтение файла построчно и вывод каждой строки из первых n
    return 0


path2file = "text/sample.txt"
n = int(input())
read_first_n_lines(path2file, n)


# zadanie 2 zadanie 2-3


# функция которая принимает на вход путь к текстовому файлу и дописывает последней строкой
def add_end_to_file(path2file):
    this_file = open(path2file, 'a')  # откройте файл в том режиме, который нужен для дозаписи в файл
    this_file.write('\nEND OF FILE')  # дополните функцию write необходимым аргументом
    this_file.close()
    return 0


path2file = "text/sample.txt"

add_end_to_file(path2file)


# zadanie 2 zadanie 2-4

def text2list(path2file):
    lines = open(path2file, 'r').readlines()
    print(lines)
    return lines


path2file = "text/sample.txt"
text2list(path2file)


zadanie 2 zadanie 2-5

def longest_line(path2file):
    lines = open(path2file, 'r').readlines()

    print(max(lines, key=len))
    # запишите самую длинную строку в переменную и верните ее как результат
    return lines


path2file = "text/sample.txt"
longest_line(path2file)


# zadanie 2 zadanie 2-6


# основная функция
from collections import Counter


def add_info_to_file(path2file):
    file = open(path2file, 'r+')  # флаг r+ позволяет открыть файл для чтения и последующей записи
    text = file.read()  # прочитайте текст из файла
    text = text.replace('\n',
                        ' ')  # replace функция, которая позволяет заменить все вхождения первого символа в строку вторым
    words = tokenize(text)  # примените к text функцию tokenize
    words_count = len(words)  # посчитайте число слов
    diferent_count = len(Counter(text.split()))  # посчитайте число различных слов

    info = str('Количество слов в тексте: ' + str(words_count) + '\n' +
            'Количество уникальных слов в тексте: ' + str(diferent_count) + '\n')

    write_to_file(file, info)

    return 0


# превращает текст в список слов
def tokenize(text):
    words = text.split()  #
    return words


# записывает аргумент в файл на новой строке
def write_to_file(file, info):
    file.write('\n' + info)
    return file


path2file = "text/sample.txt"
add_info_to_file(path2file)





# zadanie 2 zadanie 2-7


import json
import ast


def get_names_from_json(path2file):
        file = open(path2file, "r")
        data = json.load(file)
        file.close()  # закройте файл
        names = json.dumps(data)  # запишите в переменную список имен из json
        c = ast.literal_eval(names)
        print(c.keys())
        return names


path2file = "text/sample.json"
get_names_from_json(path2file)

#
# zadanie 2 zadanie 2-8
import json


def convert_marks(path2file):
    file = open(path2file, 'r')  # откройте файл в режиме чтения
    data = json.load(file)  # c помощью json.loads прочитайте структуру из файла
    file.close()  # закройте файл

    a_dict = {"A": 5, 'B': 4, 'C': 3, 'D': 2}
    keys = data.keys()

    for key in keys:
        print(data[key])
    for key, value in a_dict.items():
        for key, value in data.items():
            if data[key] == 'A':
                data[key] = a_dict.get('A')
            elif data[key] == 'B':
                data[key] = a_dict.get('B')
            elif data[key] == 'C':
                data[key] = a_dict.get('C')
            elif data[key] == 'D':
                data[key] = a_dict.get('D')

        # реализуйте логику для замены букв на цифры
    f = open('digit_marks.json', 'w')  # откройте новый файл на запись ('w')
    json.dump(data, f)  # запишите с помощью json.dump в файл
    f.close()  # закройте открытый на запись файл
    return 0


path2file = "text/sample.json"
convert_marks(path2file)
