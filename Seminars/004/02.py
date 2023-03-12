string = """Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных 
слов содержится в этом тексте."""

listString = string.lower().split()

print(string)
print(listString)

catalog = {}

for word in listString:
    catalog[word] = catalog.get(word, 0) + 1

count = 0
for _ in catalog:
    count += 1
print(count)

key = catalog.keys()
print(len(key))

print(len(listString))