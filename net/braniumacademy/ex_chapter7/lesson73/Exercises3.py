def print_day_of_week():
    while True:
        try:
            print('==============================')
            day = int(input('Nhập số 0-7: '))
            if day < 0 or day > 7:
                raise ValueError('Giá trị bạn nhập không hợp lệ.')
            else:
                match day:
                    case 0:
                        print('==> Chương trình kết thúc.')
                        break
                    case 1:
                        print('Monday')
                    case 2:
                        print('Tuesday')
                    case 3:
                        print('Wednesday')
                    case 4:
                        print('Thursday')
                    case 5:
                        print('Friday')
                    case 6:
                        print('Saturday')
                    case 7:
                        print('Sunday')
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    print_day_of_week()
