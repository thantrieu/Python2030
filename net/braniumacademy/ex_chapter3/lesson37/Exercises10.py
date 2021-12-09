import re

t = int(input())


def add_space(data):
    """This function add space after punctuations"""
    data = data.replace(".", ". ")
    data = data.replace(",", ", ")
    data = data.replace(":", ": ")
    data = data.replace(";", "; ")
    data = data.replace("!", "! ")
    data = data.replace("?", "? ")
    return data


def remove_space(data):
    """This function remove all space before punctuation"""
    data = data.replace(" .", ".")
    data = data.replace(" ,", ",")
    data = data.replace(" :", ":")
    data = data.replace(" ;", ";")
    data = data.replace(" !", "!")
    data = data.replace(" ?", "?")
    data = data.strip()
    return data


def add_dot(data):
    """This function add . to the end of the sentence if it is not exist at that place"""
    size = len(data)
    if data[size - 1] != '.' and data[size - 1] != '!' and data[size - 1] != '?':
        return data + "."
    return data


for i in range(1, t + 1):
    s = input().strip()  # remove trailing and leading whitespace
    s = s.title()  # Upper first character of each word
    s = add_space(s)
    s = re.sub("\\s+", " ", s)  # replace one or more space by one space
    s = remove_space(s)
    s = add_dot(s)
    print(f"Test {i}:\n{s}")
