def summ(a, b):
    if b == 0:
        return a
    elif b > 0:
        return summ(a + 1, b - 1)
    else:
        return summ(a - 1, b + 1)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print('Результат равен:', summ(a, b))
