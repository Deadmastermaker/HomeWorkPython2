# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Число: '))

sum = 0
for dig in str(num):
    if dig != ".":
        sum += int(dig)
print(sum)





