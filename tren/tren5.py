my_string = 'asferrthtyjfggfd'
my_list = [i for i in range(16)]
my_string = list(my_string)
print(my_string)
print(my_list)

new_list = []
for i, item in enumerate(my_string):
    new_list.append((my_list[i], my_string[i]))
# new_list = list(zip(my_string, my_list))

print(new_list)