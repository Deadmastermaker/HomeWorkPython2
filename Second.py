# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.

num = int(input('Введите N: '))

my_list = []
for i in range(1, num+1):
    my_list.append(round((1+1/i)**i, 2))
print(*my_list, sep=',')
print(sum(my_list))




