print ("Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
a = input()
s = sum(map(lambda x: int(x) if x.isdigit() else 0, a))
print(s)

print("Задание 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.")
n = int(input())
s = [round((1 + 1/i)**i, 2) for i in range(1, n+1)]

print(f"Для n = {n} -> {s}")
print(f"Сумма {sum(s)}")

print("Задание 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int")
import random
a = [i for i in range(10)]
print(a)
c = random.randint(1, 100)
for _ in range(c):
    a1 = random.randint(0, len(a) - 1)
    a2 = random.randint(0, len(a) - 1)
    temp = a[a1]
    a[a1] = a[a2]
    a[a2] = temp
print(a)