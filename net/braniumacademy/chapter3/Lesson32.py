# def print_student_info(first, last, mid="", age=20):
#     """This function print student infomation"""
#     print(f"Full name: {first} {last} {mid}")
#     print(f"Age: {age}")
#     print("----------------------------------")
#
#
# print_student_info("Khoa", "Tran", "Van", 21)
# print_student_info("Linh", "Nguyen", "Thuy")
# print_student_info("Hoang", "Le")


# def print_words(*words):
#     i = 0
#     size = len(words)
#     while i < size:
#         print(f"{i}th parameter value: {words[i]}")
#         i += 1
#
#
# print_words("Hello", "Hi", "Good", "Learning", "Python", "Branium", "Academy")

def print_student_info(first, last, mid="", age=20):
    """This function print student infomation"""
    print(f"Full name: {first} {last} {mid}")
    print(f"Age: {age}")
    print("----------------------------------")


print_student_info(age=18, first="Nam", mid="Thanh", last="Hoang")
print_student_info(first="Ngan", last="Ly")


def print_info(**info):
    print(f"Name: {info['name']}")
    print(f"Age: {info['age']}")
    print(f"Salary: {info['salary']}")


print_info(age=20, salary=18500, name="Truong Viet Hoang")
