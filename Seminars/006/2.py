# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая в данном массиве определит 
# количество элементов, у которых два соседних и, 
# при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов
# в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
# 1
# from random import randint
# n = int(input("Pls enter the length of the first array: "))
# lst = [randint(0,10) for i in range(n)]
# print(lst)
# counter = 0
# for i in range(len(lst)):
#     curr = lst[i]
#     prev = lst[(i-1)%len(lst)]
#     nxt = lst[(i+1)%len(lst)]
#     if (curr>prev) and (curr>nxt):
#         counter += 1

# print(counter)

# 2

import random

n = int(input())
arr = list(random.randint(0, 100) for _ in range(n))
print(arr)
count = 0
for i in range(len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i]>arr[i+1]:
        count += 1
if arr[-1] > arr[0] and arr[-1] > arr[-2]:
    count +=1
print(count)