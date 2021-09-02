# множества
# set все тоже, что и список, но нет копий и нельзя обратиться по номеру


# data = {'London', 'Moscva', 'Berlin'}

# for element in data:
#   print(element)


# методы множетсв
# intersection = вычислить пересечение двух множетсв
# union = вычислить объединения двух множеств
# difference = вычислить разницу двух множеств

# data = set({'London', 'Moscow', 'Berlin'})

# towns = set(['Moscow','Paris','Magadan'])

# print(towns.intersection(data)) #попала Москва
# print(towns.union(data))# попало все кроме (дупликата) москвы
# print(towns.difference(data))


# словари

# набор ключей, к каждому из которых присвоено значение
# обращение по ключу к его значению

# marks = {'ivan': 4, 'Govno': 5, 'Psina': 6}

# print(marks)

# Методы словаря
# update = повзоляеи добавить в словарь пару ключ: значение('Ivan': 4)
# pop = удаляет ключ из словаря
# keys = позволяет получить все ключи из словаря
# values = позволяет получить все значения в словаре
# items = позволяет получить все пары(ключ, значение)

# another_marks = {'ivan': 4, 'Sveta': 5, 'Talant': 6}

# marks.update(another_marks)
# print(marks)

# marks.pop('ivan')

# print(marks)


# print(marks.keys())


# zadanie 1-5 zadanie 1

data = set()
n = int(input())
for i in range(n):
for element in data:
  print(element)

# zadanie 2


result = {}
c = int(0)
d = str()
N = int(input())

for i in range(N):
    data = str(input())
    number = i
    for line in data.split('\n'):
        language = line.strip().split()
        box =
        result[number, language]

for i in range(0, len(result.keys())):
    if result.keys[i][0] == result.keys[i + 1][0]:
        c = c + 1
        d = result.keys

print(c)
print(d)
