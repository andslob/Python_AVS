# 1. Последовательностью Фибоначчи называется 
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
fib_1 = input('Введите число: ')
def fibonachi(fib_1):
    if fib_1 == 1:
        return 1
    elif fib_1 == 0:
        return 0
    else:
        return fibonachi(fib_1 - 1) + fibonachi(fib_1 - 2)
print(fibonachi(fib_1))
