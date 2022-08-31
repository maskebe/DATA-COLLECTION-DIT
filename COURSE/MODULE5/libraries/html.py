import json
from .utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data

    @classmethod
    def getBox(cls, data):
        box = data \
            .find(attrs={
                'id': 'box-data'})
        lines = box \
            .table \
            .tbody \
            .find_all('tr')
        factory = [
            item.find_all('td')
            for item in lines
        ]
        factory = [
            {
                'name': Utils.x(item[0].string),
                'phone': item[1].string,
                'email': item[2].string,
                'latlng': item[3].string,
                'salary': float(item[4].string),
                'age': int(item[5].string),
            }
            for item in factory
        ]
        return factory

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.getBox(data)
        return data
