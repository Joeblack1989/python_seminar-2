# Реализуйте алгоритм перемешивания списка. Без функции suffle из модуля random.

my_list = list(range(1, 17, 2))
print(my_list)
for i in range(0,len(my_list)//2):
    temp = my_list[i]
    my_list[i] = my_list[len(my_list)-1-i]
    my_list[len(my_list)-1-i] = temp
    i += 1
print(my_list)
