def find_max(dict_emp):
    """Hàm tìm mức lương max trong dict."""
    max_salary = 0
    for x in dict_emp.values():
        if x > max_salary:
            max_salary = x
    return max_salary


def find_min(dict_emp):
    """Hàm tìm mức lương min trong dict."""
    min_salary = find_max(dict_emp)
    for x in dict_emp.values():
        if x < min_salary:
            min_salary = x
    return min_salary


def show_dict_items(dict_emp):
    """Hàm thực hiện hiển thị nhân viên có mức lương cao nhất và thấp nhất."""
    max_salary = find_max(dict_emp)
    min_salary = find_min(dict_emp)
    result = []
    for k in dict_emp.keys():
        if dict_emp.get(k) == max_salary:
            result.append(f'{k}: {dict_emp.get(k)}')
    if max_salary != min_salary:
        for e in dict_emp.keys():
            if dict_emp.get(e) == min_salary:
                result.append(f'{e}: {dict_emp.get(e)}')
    print('{', end='')
    for index in range(len(result)):
        print(result[index], end='')
        if index != len(result) - 1:
            print(', ', end='')
    print('}')


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    dict_of_emp = dict()
    for x in range(n):
        data = [x for x in input().split()]
        dict_of_emp[data[0]] = int(data[1])
    show_dict_items(dict_of_emp)
