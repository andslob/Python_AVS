# Дан список чисел. Посчитайте, сколько в нем пар 
# элементов, равных друг другу. Считается, что любые 
# два элемента, равные друг другу образуют одну пару, 
# которую необходимо посчитать. Вводится список 
# чисел. Все числа списка находятся на разных строках.
import random
length_mass_1 = int(input('Input length of list: '))
random_mass_1 = [random.randint(1, 10) for _ in range(length_mass_1)]
count = 0
for i in random_mass_1:
    random_mass_1.count(i) > 1
    count += 1
print((count // 2))
print(random_mass_1)
