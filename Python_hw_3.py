print("Задание 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.")

a = [int(input("Введите элемент: ")) for _ in range(int(input("Введите количество элементов в списке: ")))]
print(f"{a} -> на нечётных позициях элементы ", end = '')
s = [a[i] for i in range(1, len(a), 2)]
print(*s, sep = " и ", end = ', ответ: ')
print(sum(s))

print("Задание 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")

a = [int(input("Введите элемент: ")) for _ in range(int(input("Введите количество элементов в списке: ")))]
print(f"{a} => {[a[i]*a[len(a) - i - 1] for i in range(len(a)//2 if len(a) % 2 == 0 else len(a)//2+1)]}")

print("Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.")

a = [float(input("Введите элемент: ")) for _ in range(int(input("Введите количество элементов в списке: ")))]
maxa = max([ i - int(i) for i in a if int(i) != i])
mina = min([i - int(i) for i in a if int(i) != i])
print(f"{a} => {round(maxa-mina, 2)}")

print("Задание 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")

number = int(input("Введите десятичное число: "))
str_double = ""
while number > 0:
    #print(number)
    if number % 2 == 0:
        number = number // 2
        str_double += "0"
    else:
        number = number // 2
        str_double += "1"
str_double = str_double[:: -1]
print(str_double)

print("Задание 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

def fib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return fib(index-1) + fib(index-2)


n = int(input(
    "Введите номер члена последовательности Фибоначчи: "))
lst = [fib(i) for i in range(1, n+2)]

lst = lst[::-1] + lst[1:]
lst = [-lst[i] if i % 2 == 0 and i <= len(lst)//2 else lst[i] for i in range(len(lst))]
print(lst)