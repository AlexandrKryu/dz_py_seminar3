# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
argRnd1 = int(input('Введите начальное значение случайности: '))
argRnd2 = int(input('Введите конечное значение случайности: '))
argRnd3 = int(input('Количество случайностей: '))

newlist = [random.randint(argRnd1, argRnd2) for i in range(argRnd3)]

composition = []
lastindex = -1

for i in range(len(newlist)):
    if i < len(newlist) / 2:
        composition.append(newlist[i] * newlist[lastindex])
        lastindex = lastindex - 1
        ++i
print(f'Произведение сбилжающихся элементов по индексу {newlist} = {composition}')
