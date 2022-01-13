from errors import AgeTooLowError, AgeTwoHightError

# class FullNameError(Exception):
#     """Exception raise for error in the input full name."""
#
#     def __init__(self, name, message='Full name contain invalid character'):
#         super(FullNameError, self).__init__(name, message)
#         self.__name = name
#         self.__message = message
#
#     def __str__(self):
#         return f'FullNameError: {self.__message}: {self.__name}'
#
#
# def contains_invalid_character(name):
#     for c in name:
#         if not c.isalpha() and not c == ' ':
#             return True
#     return False
#
#
# def create_full_name():
#     try:
#         full_name = input('Họ và tên: ')
#         if len(full_name) < 2 or len(full_name) > 30 or \
#                 contains_invalid_character(full_name):
#             raise FullNameError(full_name)
#         else:
#             return full_name
#     except FullNameError as e:
#         print(e)
#         return None


if __name__ == '__main__':
    try:
        age = int(input('Nhập tuổi: '))
        if age < 18:
            raise AgeTooLowError(age)
        elif age > 65:
            raise AgeTwoHightError(age)
        else:
            print('Bạn đủ điều kiện.')
    except (ValueError, AgeTooLowError, AgeTwoHightError) as e:
        print('Bạn không đủ điều kiện.')
        print(e)
