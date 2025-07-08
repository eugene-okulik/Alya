result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'


# print(result_1.index(': '))
# print(result_1[20:])
a = result_1.index(': ') + 2
# print(a)
a_1 = int(result_1[a:]) + 10
print(a_1)

b = result_2.index(': ') + 2
# print(b)
b_1 = int(result_2[b:]) + 10
print(b_1)

c = result_3.index(': ') + 2
# print(c)
c_1 = int(result_3[c:]) + 10
print(c_1)
