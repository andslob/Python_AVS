path = 'tren/file.txt'
path_to_w = '../file_2.txt'
# file = open(path, 'r', encoding='UTF-8')
# data = file.read()
# # data = file.readline()
# # data = file.readlines()
# file.close()
#
# print(data)
with open(path_to_w, 'w', encoding='UTF-8') as file:
    file.write('Это новая строка')
