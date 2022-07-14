""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и 
проверяет, является ли этот день выходным.

*Пример:*

- 6 -> да
- 7 -> да
- 1 -> нет """
import string

print('Введите число от 1 до 7: ')
day = input()

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

if isint(day) == False:
    print('Вы ввели не число.')
else:
    if int(day) > 5 and int(day) < 8:
        print('Выходоной')
    elif int(day) > 0 and int(day) < 6:
        print('Рабочий день.')
    else:
        print('Нет такого дня.')