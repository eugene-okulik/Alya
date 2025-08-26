temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
    ]

hot_days = list(filter(lambda temp: temp > 28, temperatures))
print('Жаркие дни:', hot_days)

max_temp = max(hot_days)
print("Самая высокая температура:", max_temp)

min_temp = min(hot_days)
print("Самая низкая температура:", min_temp)

avg_temp = sum(hot_days) / len(hot_days)
print("Средняя температура:", avg_temp)
