per_day = int(input('Введите растояние, которое машина проезжает за день: '))
total_dist = int(input('Введите протяженность маршрута: '))

days = (total_dist + per_day - 1)//per_day

print(f'На маршрут в {total_dist} км машина потратит {days} дня')