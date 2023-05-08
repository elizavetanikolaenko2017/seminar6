"""
 Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
 """

list=[9,0,3,-2,1,10,2,-5,7]
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)