# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')

def isint(a, b, c):
    try:
        int(a)
        int(b)
        int(c)
        return True
    except ValueError:
        return False

def find_truth(a, b, c):
    if (int(a) + int(b) + int(c)) * -1 == (int(a) * -1) + (int(b) * -1) + (int(c) * -1):
        return True
    else: False

if isint(x, y, z) == False:
    print('Одно или более введенных значений не число')
else:
    print(find_truth(x, y, z))
