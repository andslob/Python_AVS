first = int(input('Количество учеников в 1 классе: '))
second = int(input('Количество учеников во 2 классе: '))
third = int(input('Количество учеников в 3 классе: '))
table_first = (first + 1) // 2
table_second = (second + 1) // 2
table_third = (third + 1) // 2
total = table_first + table_second + table_third
print(f'Для 3 классов ({first}, {second}, {third} нужно {total} парт)')