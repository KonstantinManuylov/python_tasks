# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

from colorsys import rgb_to_yiq


x = input('Введите номер четверти: ')

def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def coordinates(a):
    if a == 1:
        return 'Возможные координаты: X от 0 до +∞; Y = от 0 до +∞'
    elif a == 2:
        return 'Возможные координаты: X от 0 до -∞; Y = от 0 до +∞'
    elif a == 3:
        return 'Возможные координаты: X от 0 до -∞; Y = от 0 до -∞'
    else:
        return 'Возможные координаты: X от 0 до +∞; Y = от 0 до -∞'

# quarter = coordinates(x)

if isint(x) == False:
    print('Введенное значение не является числом.')
elif int(x) > 4 or int(x) < 1:
    print('Такой четверти нет.')
else: print(coordinates(x))