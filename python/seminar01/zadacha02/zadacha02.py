# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number_n = int(input("Введите число: "))
if number_n > 0:
    number_m = number_n * -1
else: number_n = number_n * -1
while number_m <= number_n:
    print(f'{number_m} ')
    number_m = number_m + 1