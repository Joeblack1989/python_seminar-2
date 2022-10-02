# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число и нажмите Enter: "))
array = []
for i in range (-n,n+1):
    array.append(i)
print (array)
file = open('file.txt','r')
pos_1 = int (file.readline())
pos_2 = int (file.readline(1))    
print (array [pos_1]*array[pos_2])