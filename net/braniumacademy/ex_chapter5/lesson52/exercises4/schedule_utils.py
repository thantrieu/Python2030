from net.braniumacademy.ex_chapter5.lesson52.exercises4.test_schedule import TestSchedule


def create_schedule():
    sid = input('Mã lịch thi: ')
    time = input('Giờ thi dạng HH:mm: ')
    date = input('Ngày thi dạng dd/MM/yyyy: ')
    room = input('Phòng thi: ')
    subject = input('Môn thi: ')
    num_of_student = int(input('Số sinh viên thi: '))
    return TestSchedule(sid, time, date, room, subject, num_of_student)


def print_schedule(s):
    print(f'{s.sid:10}{s.time:10}{s.date:15}{s.room:12}{s.subject:20}{s.num_of_student:<10}')


def show_schedules(schedules):
    print('========================== Danh sách lịch thi ==========================')
    print(f'{"Mã LT":10}{"T.Gian":10}{"Ngày thi":15}{"Phòng thi":12}{"Môn thi":20}{"Số sinh viên":10}')
    for s in schedules:
        print_schedule(s)
