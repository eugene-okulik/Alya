import os
import re
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(base_path))
#print(homework_path)
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)

# Регулярное выражение для поиска дат с миллисекундами
date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d+)? )')

# Список для хранения дат
dates = []

# Читаем файл
with open(eugene_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Находим все даты по шаблону
matches = date_pattern.findall(content)

# Обрабатываем найденные даты
for match in matches:
    # Удаляем лишние пробелы
    date_str = match.strip()
    # Преобразуем строку в объект datetime (если нужно)
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        # Если миллисекунды отсутствуют
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    dates.append(dt)

# Теперь список дат
if len(dates) >= 3:
    date1, date2, date3 = dates[0], dates[1], dates[2]
    print("Первая дата на неделю позже:", date1 + timedelta(weeks=1))
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    day_of_week = days[dt.weekday()]
    print(f"День недели: {day_of_week}")
    today = datetime.now()
    delta = today - dt
    print(f"Дней назад: {delta.days}")
