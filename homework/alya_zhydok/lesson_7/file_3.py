result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат работы программы: 2'


# print(result_1.index(': '))
# print(result_1[20:])
a = result_1.index(': ') + 2
a_1 = int(result_1[a:])

b = result_2.index(': ') + 2
b_1 = int(result_2[b:])

c = result_3.index(': ') + 2
c_1 = int(result_3[c:])

d = result_4.index(': ') + 2
d_1 = int(result_4[c:])


def calc(numb):
    print(numb + 10)


calc(a_1)
calc(b_1)
calc(c_1)
calc(d_1)

