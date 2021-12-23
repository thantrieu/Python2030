# a = int(input("Enter a number: "))
# if a % 2 == 0:
#     print(f"{a} is even number.")
# else:
#     print(f"{a} is odd number.")
#
# print(f"{a} is even number.") if a % 2 == 0 else print(f"{a} is odd number.")

a = int(input("Enter an interger number: "))
b = int(input("Enter other interger number: "))
if a < b:
    print(f"{a} is less than {b}")
elif a == b:
    print(f"{a} equals to {b}")
else:
    print(f"{a} is greater than {b}")
