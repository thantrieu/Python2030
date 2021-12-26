from net.braniumacademy.ex_chapter5.lesson52.exercises4 import schedule_utils

schedules = []

option = "===================== TÙY CHỌN =====================\n" \
         "1. Thêm mới lịch thi vào danh sách.\n" \
         "2. Hiển thị danh sách lịch thi ra màn hình.\n" \
         "3. Sắp xếp danh sách lịch thi theo ngày tăng dần.\n" \
         "4. Sắp xếp danh sách lịch thi theo ngày giảm dần.\n" \
         "5. Tìm lịch thi theo ngày thi.\n" \
         "6. Tìm lịch thi theo giờ thi.\n" \
         "7. Tìm lịch thi theo phòng thi.\n" \
         "8. Tìm lịch thi theo môn thi.\n" \
         "9. Tìm lịch thi theo ngày thi và giờ thi.\n" \
         "Bạn chọn? "
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("=== Chương trình kết thúc ===")
            break
        case 1:
            new_schedule = schedule_utils.create_schedule()
            schedules.append(new_schedule)
        case 2:
            if len(schedules) > 0:
                schedule_utils.show_schedules(schedules)
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 3:
            if len(schedules) > 0:
                schedule_utils.sort(schedules)
                schedule_utils.show_schedules(schedules)
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 4:
            if len(schedules) > 0:
                schedule_utils.sort_reverse(schedules)
                schedule_utils.show_schedules(schedules)
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 5:
            if len(schedules) > 0:
                result = schedule_utils.find_by_date(schedules)
                if len(result) > 0:
                    print('=== Danh sách kết quả tìm kiếm ===')
                    schedule_utils.show_schedules(result)
                else:
                    print("=== Không tìm thấy kết quả nào ===")
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 6:
            if len(schedules) > 0:
                result = schedule_utils.find_by_time(schedules)
                if len(result) > 0:
                    print('=== Danh sách kết quả tìm kiếm ===')
                    schedule_utils.show_schedules(result)
                else:
                    print("=== Không tìm thấy kết quả nào ===")
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 7:
            if len(schedules) > 0:
                result = schedule_utils.find_by_room(schedules)
                if len(result) > 0:
                    print('=== Danh sách kết quả tìm kiếm ===')
                    schedule_utils.show_schedules(result)
                else:
                    print("=== Không tìm thấy kết quả nào ===")
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 8:
            if len(schedules) > 0:
                result = schedule_utils.find_by_subject(schedules)
                if len(result) > 0:
                    print('=== Danh sách kết quả tìm kiếm ===')
                    schedule_utils.show_schedules(result)
                else:
                    print("=== Không tìm thấy kết quả nào ===")
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case 9:
            if len(schedules) > 0:
                result = schedule_utils.find_by_date_time(schedules)
                if len(result) > 0:
                    print('=== Danh sách kết quả tìm kiếm ===')
                    schedule_utils.show_schedules(result)
                else:
                    print("=== Không tìm thấy kết quả nào ===")
            else:
                print('=== Danh sách lịch thi rỗng ===')
        case _:
            print('=== Sai chức năng. Vui lòng kiểm tra lại ===')
