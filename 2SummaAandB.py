'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4

'''

num = int(input('Введите число №1: '))
n = int(input('Введите число №2: '))

def DegreeAandB(a, b):
    if b == 0:
        return a
    else:
        sum = DegreeAandB(a, b - 1) + 1
        return sum
        

print(DegreeAandB(num, n))