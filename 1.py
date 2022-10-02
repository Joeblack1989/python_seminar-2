# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

numb = float(input ('Введите число: '))
str_numb = str(numb)
str_numb = str_numb.replace('.', '')
lst_str = list(str_numb)
lst_num = map(int, lst_str)
s = sum(lst_num)
print (s)