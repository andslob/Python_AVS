# функция map

my_string = '21165522351132'
my_string = list(my_string)
print(my_string)

# было
# for i in range(len(my_string)):
#     my_string[i] = int(my_string[i])
# стало ...
my_string = list(map(int, my_string))

print(my_string)
print(sum(my_string))