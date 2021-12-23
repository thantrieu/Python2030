numbers = [1, 2, 4, 8, 7, 6, 9, 8, 0]  # Ctrl Alt L == format code
print("Odd numbers from list: ")
for x in numbers:
    if x % 2 == 0:
        continue
    print(f"{x} ", end="")
