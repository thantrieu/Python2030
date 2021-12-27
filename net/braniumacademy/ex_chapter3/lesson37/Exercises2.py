def is_vowel(x):
    x_lower = x.lower()
    if x_lower == 'a' or x_lower == 'e' or x_lower == 'i' or x_lower == 'o' or x_lower == 'u':
        return True
    return False


def count_vowel(s):
    """Hàm đếm nguyên âm."""
    count = 0
    for x in s:
        if is_vowel(x):
            count += 1
    return count


def count_consonant(s):
    """Hàm đếm phụ âm"""
    count = 0
    for x in s:
        if x.isalpha() and not is_vowel(x):
            count += 1
    return count


t = int(input())
for i in range(1, t + 1):
    message = input()
    print(f"Test {i}:")
    print(count_vowel(message))
    print(count_consonant(message))
