import json

from COURSE.MODULE5.libraries.utils import Utils
from libraries.csvL import CsvFactory
from libraries.jsonL import JsonFactory
from libraries.htmlL import HtmlFactory
from todatabase import saveToDatabase
from libraries.globalData import GlobalDataFactory

data = JsonFactory.main() + HtmlFactory.main() + CsvFactory.main()



if __name__ == '__main__':
    print(Utils.divider())
    #print(HtmlFactory.main())
    #print(JsonFactory.main())
    #print(CsvFactory.main())
    #print(liste[Utils.randomizeString(liste)])
    #saveToDatabase(GlobalDataFactory.addCountry(GlobalDataFactory.addCurrency(data)))
    print(GlobalDataFactory.addCountry(GlobalDataFactory.addCurrency(data)))
    print('\n')
