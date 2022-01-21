import urllib.request
import xml.etree.ElementTree as ET


def write_xml_file(data, file_name):
    with open(file_name, 'w', encoding='UTF-8') as xml_writer:
        xml_writer.write(data)


class Breakfast:
    def __init__(self, name, price, des, calo):
        self.__name = name
        self.__price = price
        self.__description = des
        self.__calories = calo

    def __str__(self):
        return f'Breakfast[name={self.__name}, price={self.__price},' \
               f'description={self.__description}, calories={self.__calories}]'


def parse_xml(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    # print('Result code: ' + str(url.getcode()))
    data = response.read()
    data_string = str(data, encoding='UTF-8')
    data_string = data_string.replace('\n', '')
    root = ET.fromstring(data_string)
    menu = []
    for item in root:
        name = item[0].text
        price = item[1].text
        des = item[2].text
        calo = item[3].text
        menu.append(Breakfast(name, price, des, calo))
    return menu


def show_menu(menu):
    for item in menu:
        print(item)


if __name__ == '__main__':
    file = 'https://braniumacademy.net/breakfast.xml'
    breakfast_menu = parse_xml(file)
    show_menu(breakfast_menu)
