import datetime

my_time = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')

full_month_name = python_date.strftime('%B')
print('Полное название месяца:', full_month_name)

formatted_date = python_date.strftime('%d.%m.%Y, %H:%M')
print('Отформатированная дата:', formatted_date)
