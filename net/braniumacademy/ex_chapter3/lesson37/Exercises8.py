def is_existed(data, key, to):
    """This function check whether or not key exist in list data"""
    for index in range(0, to):
        if data[index] == key:
            return True
    return False


def create_unique_words(data):
    """This function filter and create a list contain only one-time occurrence words"""
    result = []
    for j in range(0, len(data)):
        if not is_existed(data, data[j], j):
            result.append(data[j])
    return result


def listed_words(data, unique_data):
    """This function listed words and number occurent of each word"""
    for x in unique_data:
        print(f"{x}-{data.count(x)}")


t = int(input())
for i in range(1, t + 1):
    s = input()
    words = s.split()
    print(f"Test {i}:")
    u_words = create_unique_words(words)
    listed_words(words, u_words)
    print()
