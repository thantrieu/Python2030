import urllib.request
import xml.etree.ElementTree as et


class Food:
    def __init__(self, name, price, des, calo):
        self.__name = name
        self.__price = price
        self.__description = des
        self.__calories = calo

    def __str__(self):
        return f'Food[name={self.__name}, price={self.__price},' \
               f'description={self.__description}, calories={self.__calories}]'

    @property
    def price(self):
        return self.__price

    @property
    def calo(self):
        return self.__calories


def parse_xml(url):
    root = et.fromstring(load_data(url))
    menu = []
    for item in root:
        name = item[0].text
        price = item[1].text
        des = item[2].text
        calo = item[3].text
        menu.append(Food(name, price, des, calo))
    return menu


def show_menu(menu):
    for item in menu:
        print(item)


def load_data(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    mdata = response.read()
    data_string = str(mdata, encoding='UTF-8')
    urllib.request.urlcleanup()
    return data_string


if __name__ == '__main__':
    url = 'https://braniumacademy.net/resources/breakfast.xml'
    breakfast_menu = parse_xml(url)
    print('====================================')
    print('==> Danh sách các món ăn sáng: ')
    show_menu(breakfast_menu)
    print('====================================')
    print('==> Danh sách các món ăn theo giá tăng dần: ')
    breakfast_menu.sort(key=lambda x: x.price)
    show_menu(breakfast_menu)
    print('====================================')
    print('==> Danh sách các món ăn theo lượng calo giảm dần: ')
    breakfast_menu.sort(key=lambda x: x.calo, reverse=True)
    show_menu(breakfast_menu)
