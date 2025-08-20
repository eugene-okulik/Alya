def extract_number(s: str) -> int:
    return int(s.split(':')[-1].strip())


result_1 = "результат операции: 42"
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат работы программы: 2'
main_number = 10

print(extract_number(result_1) + main_number)
print(extract_number(result_2) + main_number)
print(extract_number(result_3) + main_number)
print(extract_number(result_4) + main_number)
