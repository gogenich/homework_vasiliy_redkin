time_sec = int(input('введите время в секундах: '))
time_hour = time_sec // 3600
time_sec = time_sec % 3600
time_min = time_sec // 60
time_sec = time_sec % 60
print(f'{time_hour:02}:{time_min:02}:{time_sec:02}')



