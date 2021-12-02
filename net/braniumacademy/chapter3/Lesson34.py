# Tạo biểu thức lambda nhân 10 vào số a bất kỳ
# f = lambda a: a * 10
# print(f(99))
# print(f(5))

# sum = lambda a, b: a + b
# x = 5
# y = 9
# print(sum(x, y))

# a = lambda : print("Ok")
# a()

def my_function(n):
    return lambda a: a * n


doubler = my_function(2)
tripler = my_function(3)
x = 11
print(f"Before: {x}, after double value: {doubler(x)}")
print(f"Before: {x}, after triple value: {tripler(x)}")
