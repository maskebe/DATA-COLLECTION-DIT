from COURSE.MODULE5.libraries.csvL import CsvFactory
from COURSE.MODULE5.libraries.htmlL import HtmlFactory
from COURSE.MODULE5.libraries.jsonL import JsonFactory
from COURSE.MODULE5.libraries.currency import CurrencyScrapper
import pandas as pd
import requests
import json
from COURSE.MODULE5.libraries.utils import Utils


class GlobalDataFactory(object):

    @classmethod
    def aggregateData(cls):
        data = JsonFactory.main() + HtmlFactory.main() + CsvFactory.main()
        return data


    @classmethod
    def addCurrency(cls, data):
        liste_devise = ['Euro', 'Dollar us', 'Yen japonais']
        currencies = CurrencyScrapper.makeCurrencyList()
        #print(currencies[0]['Devise'])

        def devise(x):
            x['devise'] = liste_devise[Utils.randomizeString(liste_devise)]
            x['devise'] = str(x['devise'])
            for i in currencies:
                if i['Devise'] == x['devise']:
                    x['achat'] = i['Achat']
                    x['vente'] = i['Vente']
            return x

        data = map(devise, data)
        return list(data)

    @classmethod
    def addCountry(cls, data):
        URL = 'https://restcountries.com/v2/all'
        countries = requests.get(URL)
        countries = json.loads(countries.text[:])

        def datacountry(x):
            pays = []
            for i in countries:
                pays.append({'name': i['name'], 'flag': i['flags']['png']})
                x['country'] = pays[Utils.randomizeString(pays)]["name"]
                x['flag'] = pays[Utils.randomizeString(pays)]["flag"]
            return x

        data = map(datacountry, data)
        return list(data)