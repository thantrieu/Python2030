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
    print(f'{s.id:10}{s.time:10}{s.date:15}{s.room:12}{s.subject:20}{s.num_of_student:<10}')


def show_schedules(schedules):
    print('========================== Danh sách lịch thi ==========================')
    print(f'{"Mã LT":10}{"T.Gian":10}{"Ngày thi":15}{"Phòng thi":12}{"Môn thi":20}{"Số sinh viên":10}')
    for s in schedules:
        print_schedule(s)


def get_day(date):
    return int(date.split(sep='/')[0])


def get_month(date):
    return int(date.split(sep='/')[1])


def get_year(date):
    return int(date.split(sep='/')[2])


def sort(schedules):
    schedules.sort(key=lambda x: (get_year(x.date),
                                  get_month(x.date),
                                  get_day(x.date),
                                  x.time, x.num_of_student, x.id))


def sort_reverse(schedules):
    schedules.sort(key=lambda x: (get_year(x.date),
                                  get_month(x.date),
                                  get_day(x.date),
                                  x.time, x.num_of_student, x.id),
                   reverse=True)


def find_by_date(schedules):
    result = []
    date = input('Ngày thi cần tìm dạng dd/mm/yyyy(ví dụ 22/12/2025): ')
    for s in schedules:
        if s.date == date:
            result.append(s)
    return result


def find_by_time(schedules):
    result = []
    time = input('Giờ thi cần tìm dạng HH:MM(ví dụ 10:30): ')
    for s in schedules:
        if s.time == time:
            result.append(s)
    return result


def find_by_room(schedules):
    result = []
    room = input('Phòng thi cần tìm: ')
    for s in schedules:
        if s.room == room:
            result.append(s)
    return result


def find_by_subject(schedules):
    result = []
    subject = input('Môn thi cần tìm: ')
    for s in schedules:
        if s.subject == subject:
            result.append(s)
    return result


def find_by_date_time(schedules):
    result = []
    date_time = input('Ngày thi và giờ thi cần tìm dạng dd/mm/yyyy HH:MM(ví dụ 20/12/2025 10:30): ')
    date, time = date_time.split()
    for s in schedules:
        if s.time == time and s.date == date:
            result.append(s)
    return result
