def is_existed(data, key, to):
    """This function check whether or not key exist in list data"""
    for index in range(0, to):
        if data[index] == key:
            return True
    return False


t = int(input())
for i in range(1, t + 1):
    s = input()
    words = s.split()
    print(f"Test {i}:")
    for j in range(0, len(words)):
        if is_existed(words, words[j], j) is False:
            print(f"{words[j]} ", end="")
    print()
