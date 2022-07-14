# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
import random

# list_numbers = [1, 4, 8, 5, 7]
list_numbers = []
for i in range(5):
    list_numbers.append(random.randint(1, 100))
print(list_numbers)
max_number = list_numbers[0]
for item in list_numbers:
    if max_number < item:
        max_number = item

print(f'Минимальное число {max_number}')