try:
    x = 2 / 0
except TypeError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
else:
    print('No exception occur.')
finally:
    print('Finally block excute.')
print('Next statement after exception block.')
# division by zero
# Finally block excute.
# Next statement after exception block.

try:
    x = 9 / 3
except TypeError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
else:
    print('No exception occur.')
print('Next statement after exception block.')
# No exception occur.
# Next statement after exception block.

try:
    x = 2 / 0
    print('No exception occur.')
finally:
    print('Finally block excute.')
print('Next statement after exception block.')
# Traceback (most recent call last):
#   File "C:\Users\trieu\PycharmProjects\LeanPython
#   \net\braniumacademy\chapter7\Lesson72.py", line 27, in <module>
#     x = 2 / 0
# ZeroDivisionError: division by zero
# Finally block excute.


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
# except ChildError:
#     print('ChildError')
# except FatherError:
#     print('FatherError')
# except GrandFatherError:
#     print('GrandFatherError')


