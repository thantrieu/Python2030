def show_gpa(student_ids, dict_student):
    """Hàm thực hiện hiển thị điểm sinh viên theo key
       là mã sinh viên cho trước trong list.
    """
    for y in student_ids:
        print(f'{dict_student.get(y)} ', end='')
    print()


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    dict_of_student = dict()
    for x in range(n):
        data = [x for x in input().split()]
        dict_of_student[data[0]] = data[1]
    ids = [x for x in input().split()]
    show_gpa(ids, dict_of_student)
