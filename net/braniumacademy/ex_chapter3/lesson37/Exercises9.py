def is_existed(data, key, to):
    """This function check whether or not key exist in list data"""
    for index in range(0, to):
        if data[index] == key:
            return True
    return False


def create_unique_characters(data):
    """This function filter and create a list contain only one-time occurrence characters"""
    result = []
    for j in range(0, len(data)):
        # if character at j position is alphabet, and doesn't exist before
        if data[j].isalpha() and not is_existed(data, data[j], j):
            result.append(data[j])
    return result


def listed_characters(data, unique_data):
    """This function listed words and number occurent of each character"""
    print("[", end="")
    size = len(unique_data)
    for j in range(0, size):
        print(f"{unique_data[j]}: {data.count(unique_data[j])}", end="")
        if j < size - 1:
            print(", ", end="")
    print("]")


t = int(input())
for i in range(1, t + 1):
    s = input()
    print(f"Test {i}:")
    characters = create_unique_characters(s)
    listed_characters(s, characters)
