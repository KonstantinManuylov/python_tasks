# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a_x = input('Введите координату X точки A: ')
a_y = input('Введите координату Y точки A: ')
b_x = input('Введите координату X точки B: ')
b_y = input('Введите координату Y точки B: ')

def isint(a, b, c, d):
    try:
        int(a)
        int(b)
        int(c)
        int(d)
        return True
    except ValueError:
        return False

def find_gipotenusa(a, b, c, d):
    katet1 = a - c
    katet2 = b - d
    gipothenusa = round(((katet1 ** 2) + (katet2 ** 2)) ** 0.5, 3)
    return gipothenusa

# gipotenusa = find_gipotenusa(int(a_x), int(a_y), int(b_x), int(b_y))

if isint(a_x, a_y, b_x, b_y) == False:
    print('Одно или более введенных значений не число')
else: print(f'Расстояние между точками равно {find_gipotenusa(a_x, a_y, b_x, b_y)}')