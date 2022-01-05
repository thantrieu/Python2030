import xml.etree.ElementTree as et
from operator import itemgetter
from collections import OrderedDict


class CD:
    def __init__(self, title, artist, country, company, price, year):
        self.__title = title
        self.__price = price
        self.__year = year
        self.__artist = artist
        self.__country = country
        self.__company = company

    def __str__(self):
        return f'{self.__title:25}{self.__artist:20}' \
               f'{self.__country:12}{self.__company:15}' \
               f'{self.__price:<6}{self.__year:6}'

    @property
    def price(self):
        return self.__price

    @property
    def country(self):
        return self.__country

    @property
    def year(self):
        return self.__year

    @property
    def artist(self):
        return self.__artist


def parse_xml(file_name):
    """Hàm thực hiện bóc tách dữ liệu từ file xml và tạo 
       đối tượng tương ứng trong Python. Trả về danh sách các CD.
    """
    tree = et.parse(file_name)
    root = tree.getroot()
    catalog = []
    for item in root:
        title = item[0].text
        artist = item[1].text
        country = item[2].text
        company = item[3].text
        price = float(item[4].text)
        year = int(item[5].text)
        catalog.append(CD(title, artist, country, company, price, year))
    return catalog


def show_catalog(catalog):
    for item in catalog:
        print(item)


def find_by_artist(catalog, artist):
    for cd in catalog:
        if cd.artist == artist:
            print(cd)


def statistics_by_country(catalog):
    countries = {}
    for cd in catalog:
        if cd.country in countries:
            countries[cd.country] += 1
        else:
            countries[cd.country] = 1
    return OrderedDict(sorted(countries.items(), key=itemgetter(1), reverse=True))


def statistics_by_year(catalog):
    years = {}
    for cd in catalog:
        if cd.year in years:
            years[cd.year] += 1
        else:
            years[cd.year] = 1
    return OrderedDict(sorted(years.items(), key=itemgetter(1)))


def print_statistics(dct):
    for key in dct.keys():
        print(f'{key:<10}: {dct.get(key)}')


if __name__ == '__main__':
    file = 'cd_catalog.xml'
    cd_catalog = parse_xml(file)
    print('====================================')
    print('==> Danh sách các CD: ')
    show_catalog(cd_catalog)
    print('====================================')
    print('==> Danh sách số lượng các CD theo quốc gia: ')
    result = statistics_by_country(cd_catalog)
    print_statistics(result)
    print('====================================')
    print('==> Danh sách số lượng các CD theo năm xuất bản: ')
    result = statistics_by_year(cd_catalog)
    print_statistics(result)
    print('====================================')
    artist_name = input('Nhập tên nghệ sĩ: ')
    print(f'==> Danh sách các CD theo tên nghệ sĩ "{artist_name}": ')
    find_by_artist(cd_catalog, artist_name)
