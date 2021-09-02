# #
# # zadanie 1-6 zadanie 1
def min4(a, b, c, d):
    m = int()
    m = min(a, b, c, d)
    return m


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))

# zadanie 1-6 zadanie 2

def mysum(a):                    # создаем функцию mysum
    res = 0
    for x in a:
        res = res + x
        print('x=', x, 'res=', res)
    return res
                                # конец функции mysum
a = map(int, input().split())   # читаем числа с клавиатуры
print('Сумма равна', mysum(a))  # вызываем функцию mysum

