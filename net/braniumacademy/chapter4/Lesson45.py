dict_a = {'one': 1, 'two': 2, 'three': 3}
dict_b = dict(one=1, two=2, three=3)
dict_c = dict({'one': 1, 'two': 2, 'three': 3})
dict_d = dict([('one', 1), ('two', 2), ('three', 3)])
dict_e = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
dict_f = dict({'two': 2, 'one': 1}, three=3)
print(dict_a)
print(dict_f)
print(dict_f == dict_e == dict_d == dict_c == dict_b == dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

# Thêm mới phần tử vào dict
dict_a["five"] = 5
dict_a["four"] = 4
print(dict_a)
del dict_a['four']
print(dict_a)
del dict_a
