# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите любое число: '))
b = ''
while num > 0:
    b = str(num % 2) + b
    num = num // 2
print(f'Двоичное значение = {b}')