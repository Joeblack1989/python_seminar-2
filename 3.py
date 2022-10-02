# Задайте список из n чисел, заполненный по формуле (1 + 1 / n) ^ n и выведите на экран их сумму.

n = int (input ('Введите число и нажмите Enter: '))
list = []
for i in range (1, n + 1):
    list.append (round((1 + 1 / i)**i, 0))
print (list)
print (sum(list))
