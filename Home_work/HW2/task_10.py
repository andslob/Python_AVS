n = int(input('Введите кол-во монет: '))
k = 0
for i in range(n):
    v = int(input('Введите сторону монеты:'))
    if v == 1:
        k += 1
print(k if k < n/2 else n-k)
