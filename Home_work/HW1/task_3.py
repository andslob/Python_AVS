check_number = int(input('Введите номер билета:'))
a = check_number // 1000
b = check_number % 1000
if (a // 100 + (a // 10) % 10 + a % 10) == (b // 100 + (b // 10) % 10 + b % 10):
    print('YES')
else:
    print('NO')