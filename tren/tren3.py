my_string = '21165522351132'
my_string = list(my_string)
# my_string = list(map(int, my_string))
# print(my_string)
# 1
# my_string = list(filter(lambda x: x%2 == 0, my_string))
# print(my_string)
#
# 2
my_string = [int(x) for x in my_string if int(x)%2 == 0]
print(my_string)

# 3
# def is_odd(num: int) -> bool:
#     if num%2 == 1:
#         return True
#     else:
#         return False
# my_string = list(filter(is_odd, my_string))
# print(my_string)
