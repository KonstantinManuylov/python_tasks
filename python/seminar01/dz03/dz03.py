# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = input('Введите координату x: ')
y = input('Введите координату y: ')

def isint(a, b):
    try:
        int(a)
        int(b)
        return True
    except ValueError:
        return False

def check_quarter(a, b):
    if a < 0 and b > 0:
        return 2
    elif a > 0 and b > 0:
        return 1
    elif a < 0 and b < 0:
        return 3
    else:
        return 4

# quarter_number = check_quarter(x, y)

if isint(x, y) == False:
    print('Одно или более введенных значений не число. ')
elif x == 0 or y == 0:
    print('Координаты не должны быть равны нулю. ')
else:
    print(f'Точка находится в {check_quarter(x, y)} четверти. ')