import requests
import json
import re
from bs4 import BeautifulSoup


class Formatter(object):
    @classmethod
    def to_dict(cls, data: str):
        return json.loads(data)


class HttpFetcher(object):
    @classmethod
    def fetch(cls,
              BASE_URL,
              params: dict = None,
              headers: dict = None):
        with requests.Session() as session:
            params = params or {}
            headers = headers or {}
            result = session.get(BASE_URL,
                                 params=params,
                                 headers=headers)
            result = result.text
            return result


class Scrapper(object):
    @classmethod
    def by_thousand(cls, value):
        return float(value) * 1000.0

    @classmethod
    def scrapLink(cls, URL):
        return HttpFetcher \
            .fetch(URL)

    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')

    @classmethod
    def box_products(cls, URL):
        products = []
        result = cls.souper(URL)
        box = result \
            .find_all(attrs={
                'class': 'box-text box-text-products text-center grid-style-2'})
        for item in box:
            title = item \
                .find(attrs={'class': 'title-wrapper'}) \
                .find(attrs={'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'}) \
                .string \
                .strip() \
                .capitalize()
            price = item \
                .find(attrs={'class': 'price-wrapper'}) \
                .find(attrs={'class': 'woocommerce-Price-amount amount'}) \
                .find('bdi') \
                .contents[0] \
                .strip()
            products \
                .append({
                    'title': title,
                    'price': cls.by_thousand(price),
                    'quantity': 1,
                    'currency': 'XOF'
                })
        return products


if __name__ == '__main__':
    BASE_URL = 'https://www.fabellashop.com'
    URL = f'{BASE_URL}/categorie-produit/maquillageongles/teint/'
    result = Scrapper.box_products(URL)
    print(result)
