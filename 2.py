# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

numb = int (input ('Введите число и нажмите клавишу Enter: '))
list = []
composition = 1
for i in range(numb):
    composition *= (i + 1)
    list.append (composition)
print (list)