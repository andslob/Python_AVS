# Даны два массива чисел. Требуется вывести те 
# элементы первого массива (в том порядке, в каком 
# они идут в первом массиве), которых нет во втором
# массиве. Пользователь вводит число N - количество 
# элементов в первом массиве, затем N чисел - 
# элементы массива. Затем число M - количество 
# элементов во втором массиве. Затем элементы 
# второго массива
from random import randint
n = int(input('Введите длину массива 1:'))
m = int(input('Введите длину массива 2:'))

list_n = [randint(0, 10) for i in range(n)]
list_m = [randint(0, 10) for i in range(m)]
print(list_n)
print(list_m)

for i in range(len(list_m)):
    count = list_n.count(list_m)
    if count > 0:
        for j in range(count):
            list_n.remove(list_m[i])
print(list_n)