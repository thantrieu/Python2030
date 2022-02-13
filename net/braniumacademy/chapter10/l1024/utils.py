from net.braniumacademy.chapter10.l1024.model.student import Student

STUDENT_FILE_NAME = 'STUDENT.DAT'


def student_to_tuple(student: Student) -> tuple[str | str, ...]:
    """ Hàm tiện ích thực hiện chuyển đổi thông tin sinh viên thành một
        tuple chứa các phần tử biểu diễn ở string.
    """
    return tuple([student.person_id, student.full_name,
                  student.birth_date.strftime('%d/%m/%Y'),
                  student.student_id, student.email, f'{student.gpa:0.2f}',
                  student.major])


def clear_treeview(treeview):
    """ Hàm tiện ích dùng để xóa toàn bộ bản ghi trong bảng(treeview)
        trước khi hiển thị thông tin mới vào đó nhằm tránh trùng lặp các bản ghi.
    """
    for item in treeview.get_children():
        treeview.delete(item)
