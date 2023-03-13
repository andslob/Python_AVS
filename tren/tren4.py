my_string = 'asferrthtyjfggfd'
my_string = list(my_string)
print(my_string)
# 1
for i in range(len(my_string)):
    print(f'{i}. {my_string[i]}')
# 2
# for i, item in enumerate(my_string, 1):
#     print(f'{i}. {item}')