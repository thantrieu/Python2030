# try:
#     result = 6 / 0
#     print(result)
# except TypeError as ex:
#     print(f'{ex}')
# except ValueError as ex:
#     print(f'{ex}')
# except ZeroDivisionError as ex:
#     print(f'{ex}')
# else:
#     print('No exception occur.')
# finally:
#     print('Cleanup...')
#
# print('Statement 1 after exception.')
# print('Statement 2 after exception.')
# print('Statement 3 after exception.')


# class GrandFatherError(Exception):
#     pass
#
#
# class FatherError(GrandFatherError):
#     pass
#
#
# class ChildError(FatherError):
#     pass
#
#
# try:
#     raise ChildError  # kích hoạt 1 ngoại lệ dẫn xuất
#
# except ChildError:
#     print('ChildError')
# except FatherError:
#     print('FatherError')
# except GrandFatherError:
#     print('GrandFatherError')
# except Exception as e:
#     print(e)


def function1():
    try:
        x = 9 / 0
    except TypeError as ex:
        print(ex)
    print('Next statement inside function1.')


def function2():
    function1()
    print('Next statement inside function2.')


def function3():
    try:
        function2()
    except ZeroDivisionError:
        print('Exception handled.')
    print('Next statement inside function3.')


function3()
print('Next statement after exception block.')

