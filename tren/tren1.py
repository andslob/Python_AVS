import random

my_list = []
# было
# for i in range(10):
#     my_list.append(random.randint(0, 10))
# стало
my_list = [random.randint(0, 10) for _ in range(10)]