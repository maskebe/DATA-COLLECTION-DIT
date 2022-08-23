import json

from COURSE.MODULE5.libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory

def aggregateData():
    data = JsonFactory.main() + HtmlFactory.main() + CsvFactory.main()
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(Utils.divider())
    #print(HtmlFactory.main())
    #print(JsonFactory.main())
    #print(CsvFactory.main())
    print(aggregateData())
    print('\n')
