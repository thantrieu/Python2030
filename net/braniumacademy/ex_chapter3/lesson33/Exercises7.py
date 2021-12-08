def reverse_string(string, pos):
    """This function print string in reverse order"""
    if pos == 0:
        print(string[pos])
    else:
        print(string[pos], end="")
        reverse_string(string, pos - 1)


t = int(input())
for i in range(1, t + 1):
    s = input()
    print(f"Test {i}: ", end="")
    reverse_string(s, len(s) - 1)
