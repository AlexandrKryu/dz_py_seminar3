# Реализуйте алгоритм задания случайных чисел без
# использования встроенного генератора псевдослучайных чисел.

import time

def random(n):
    list = []
    for i in range(1, n + 1):
        list.append(round(i * (time.time() * 1000 % 100)))
    return list

list = random(5)
print(list)