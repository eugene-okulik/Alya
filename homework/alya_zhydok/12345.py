from itertools import product

statuses_dogovor = ['Страхователь', 'Не страхователь (выгодоприобретатель)', 'Не страхователь (третье лицо)']
status_nalog = ['Резидент РФ', 'Нерезидент РФ']
grazhdanstvo = ['Есть гражданство РФ', 'Нет гражданства РФ, ВНЖ/беженец', 'Нет гражданства РФ, нет ВНЖ']
danny_povt = ['Являюсь получателем', 'Не являюсь', 'Лицо без гражданства']
nalog_us = ['Да', 'Нет']
otkaz = ['Не применимо', 'Не отказывался', 'Отказывался', 'Иное']

combinations = list(product(statuses_dogovor, status_nalog, grazhdanstvo, danny_povt, nalog_us, otkaz))

# Вывод или сохранение комбинаций
for combo in combinations:
    print(combo)