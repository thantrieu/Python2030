message = "Hello"
print(message)

for x in message:
    print(f"{x} ", end="")
print()

for i in range(0, len(message), 1):
    print(f"{message[i]} ", end="")
print()

for i in range(-len(message), 0, 1):
    print(f"{message[i]} ", end="")
print()

print(message[0: 3])
print(message[: 3])
print(message[3:])
print(message[3: len(message)])
print(message[:])

print(r"Welcome\nto\nBranium\nAcademy")
print('D:/Hello/Some Folder/labla')

string = "             WecOme to BrAnium acAdemy              "
number = "-32214545"
print(string.swapcase())
print(f"After remove leading and trailing space: '{string.strip()}'")
print(string.zfill(40))
print(number.zfill(20))
