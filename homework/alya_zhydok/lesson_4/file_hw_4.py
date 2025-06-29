my_dict = {}

my_tuple = (1, 3, 5.55, True, 'text1')
# print(my_tuple)
print(my_tuple[-1])

my_list = [2, 4, 6.88, False, 'text2']
# print(my_list)
my_list.append('addition')
my_list.pop(1)
# print(my_list)

my_dict_add = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
# print(my_dict_add)
my_dict_add['i am a tuple'] = 'value6'
del my_dict_add['key5']
# print(my_dict_add)

my_set = {11, 33, 55.55, None, 'text3'}
# print(my_set)
my_set.add(111)
my_set.pop()
# print(my_set)

my_dict = {'tuple': my_tuple, 'list': my_list, 'dict': my_dict_add, 'set': my_set}
print(my_dict)
