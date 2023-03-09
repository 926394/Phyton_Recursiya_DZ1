'''
Возведение в степень
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8

'''

num = int(input('Введите число: '))
n = int(input('Введите степень числа: '))

def DegreeAandB(a, b):
    if b == 0:
        return 1
    else:
        return a * DegreeAandB(a, b-1)


print(DegreeAandB(num, n))