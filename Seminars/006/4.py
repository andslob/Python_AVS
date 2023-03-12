# Два различных натуральных числа n и m называются 
# дружественными, если сумма делителей числа n 
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные 
# числа. По данному числу k выведите все пары 
# дружественных чисел, каждое из которых не 
# превосходит k. Программа получает на вход одно 
# натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных 
# чисел, каждое из которых не превосходит k. Пары 
# необходимо выводить по одной в строке, разделяя 
# пробелами. Каждая пара должна быть выведена только 
# один раз (перестановка чисел новую пару не дает).

# n = 220
# m = 284

# lst_div = []
# for i in range(1, n / 2):
#     if n % 2 == 0:
#         lst_div.append(i)

# print(summ(lst_div))


def divisor(x):
    return sum([i for i in range(1,x//2+1) if x%i == 0])

x = int(input("Pls enter the upper limit: "))

for i in range(1, x):
    if divisor(divisor(i)) == i and i<divisor(i):
        print((i,divisor(i)))