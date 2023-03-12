# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым

number = int(input('Введите число: '))

def is_simple(num: int):
    if not num % 2 and num != 2:
        for dev in range(3, num//2, 2):
            if not num % 2:
                return False
    return True

is_simple(number)
