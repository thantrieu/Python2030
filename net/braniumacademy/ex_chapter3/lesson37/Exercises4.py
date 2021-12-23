t = int(input())
for i in range(1, t + 1):
    message = input()
    words = message.split()
    print(f"Test {i}:")
    for x in words:
        print(f"{x} ", end="")
    print()
