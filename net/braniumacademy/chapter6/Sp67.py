import xml.etree.ElementTree as et


class Breakfast:
    def __init__(self, name, price, des, calo):
        self.__name = name
        self.__price = price
        self.__description = des
        self.__calo = calo

    def __str__(self):
        return f'Breakfast[name={self.__name}, price={self.__price}, ' \
               f'description={self.__description}, calories={self.__calo}]'


def parse_xml(file_name):
    tree = et.parse(file_name)  # Lấy cây mô tả file XML
    root = tree.getroot()       # Lấy phần tử gốc
    menu = []                   # Tạo list kết quả rỗng
    for item in root:           # Lần lượt bóc tách từng phần tử(node)
        name = item[0].text     # Trích xuất tên
        price = item[1].text
        des = item[2].text
        calo = int(item[3].text)
        menu.append(Breakfast(name, price, des, calo))
    return menu


def show_menu(menu):
    for item in menu:
        print(item)


if __name__ == '__main__':
    breakfast_menu = parse_xml('breakfast.xml')
    show_menu(breakfast_menu)
