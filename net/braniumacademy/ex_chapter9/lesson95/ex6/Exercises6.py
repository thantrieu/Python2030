import xml.etree.ElementTree as et
import urllib.request
from operator import itemgetter
from collections import OrderedDict


class Plant:
    def __init__(self, common, botanical, zone, light, price, avail):
        self.__common = common
        self.__price = price
        self.__botanical = botanical
        self.__zone = zone
        self.__light = light
        self.__availability = avail

    def __str__(self):
        return f'{self.__common:20}{self.__botanical:25}' \
               f'{self.__zone:10}{self.__light:15}' \
               f'{self.__price:10}{self.__availability:10}'

    @property
    def price(self):
        return self.__price

    @property
    def zone(self):
        return self.__zone


def parse_xml(url):
    """Hàm thực hiện bóc tách dữ liệu từ file xml và tạo
       đối tượng tương ứng trong Python. Trả về danh sách các CD.
    """
    root = et.fromstring(load_data(url))
    catalog = []
    for item in root:
        common = item[0].text
        bota = item[1].text
        zone = item[2].text
        light = item[3].text
        price = item[4].text
        avai = item[5].text
        catalog.append(Plant(common, bota, zone, light, price, avai))
    return catalog


def show_catalog(catalog):
    for item in catalog:
        print(item)


def statistics_by_zone(catalog):
    zones = {}
    for plant in catalog:
        if plant.zone in zones:
            zones[plant.zone] += 1
        else:
            zones[plant.zone] = 1
    return OrderedDict(sorted(zones.items(), key=itemgetter(0), reverse=True))


def print_statistics(dct):
    for key in dct.keys():
        print(f'{key:15}: {dct.get(key)}')


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
    url = 'https://braniumacademy.net/resources/plant_catalog.xml'
    plant_catalog = parse_xml(url)
    print('====================================')
    print('==> Danh sách các loài thực vật: ')
    show_catalog(plant_catalog)
    print('====================================')
    print('==> Danh sách các thực vật theo giá tăng dần: ')
    plant_catalog.sort(key=lambda x: x.price)
    print('====================================')
    print('==> Danh sách số lượng các loài thực vật theo zone: ')
    result = statistics_by_zone(plant_catalog)
    print_statistics(result)
