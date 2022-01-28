# Входные данные (1): число X
# Требуется написать алгоритм на любом языке программирования, вычисляющий сумму всех простых чисел, не превышающих число X.
# Справка: простым числом называют целое положительное число, которое имеет только два различных натуральных делителя – единица и само число.
# Примеры простых чисел: 2, 3, 5, 7, 11, …
import time
class NumberCheck(Exception):
    '''Обработка исключений'''
    def __init__(self, number):
        Exception.__init__(self)
        self.number = number
try:
    x = int(input('Введите x->'))
    if x <= 1:
        raise NumberCheck(x)
    mylist = []
    buf = 0
    sum = 0
    for i in range(2, x + 1):
        for j in range(2, i):
            if i % j == 0:
                buf += 1
        if buf == 0:
            mylist.append(i)
        buf = 0
    for i in mylist:
        sum += i
    print('Сумма всех простых чисел не превышающих x = {0} равна S = {1} '.format(x, sum))
except ValueError:
    print('Перезапустите программу и введите натуральное число.')
except NumberCheck as ex:
    print(f"Вы ввели некорректное число. Ваше число {x} не удовлетворяет условиям задачи.")
print('Консоль закроется через 5 сек...')
time.sleep(5)
