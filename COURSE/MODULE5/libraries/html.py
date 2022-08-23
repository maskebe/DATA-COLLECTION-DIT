from bs4 import BeautifulSoup
import request
import json
from COURSE.MODULE5.libraries.utils import Utils
#from bs4 import BeautifulSoup



BASE_URL = r'C:\masterIA\data_collection\repos\repos\KUASSI\DATA-COLLECTION-DIT\COURSE\DATABASES\data-zIybdmYZoV4QSwgZkFtaB.html'


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
    def getBoxData(cls):
        data = cls.openFile()
        data = data \
            .find_all(attrs={
            'id': 'box-data'})
        if data:
            table = data[0].table
            return table
        return None

    @classmethod
    def makeDataList(cls):
        data = cls.getBoxData()
        if data:
            tr = data.find_all('tr')
            th = data.find_all('th')
            factory = [
                          item.find_all('td')
                          for item in tr
                      ][1:]
            factory = [
                {
                    th[0].string.strip().lower(): x.string.strip(),
                    th[1].string.strip().lower(): y.string.strip(),
                    th[2].string.strip().lower(): z.string.strip(),
                    th[3].string.strip().lower(): t.string.strip(),
                    th[4].string.strip().lower(): float(u.string.strip().replace(',', '.')),
                    th[5].string.strip().lower(): float(w.string.strip().replace(',', '.')),
                }
                for (x, y, z, t, u, w) in factory
            ]
            return factory

    @classmethod
    def naming(cls, data):
        def name(x):
            x['name'] = x['name'].split(' ')
            last_name = x['name'][-1].upper()
            first_name = x['name'][0].capitalize()
            x['name'] = ' '.join([first_name, last_name])
            return x

        data = map(name, data)
        return list(data)

    @classmethod
    def main(cls):
        data = cls.makeDataList()
        data = cls.naming(data)
        return data