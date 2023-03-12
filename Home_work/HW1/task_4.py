n = int(input('Введите размер 1 шоколадки: '))
m = int(input('Введите размер 2 шоколадки: '))
k = int(input('Введите необходимое количество долек: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')