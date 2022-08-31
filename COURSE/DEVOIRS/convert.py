import requests
import json
import csv


f = open('convertedcurrency.csv', 'a')

def makeCurrencyConvert(montant, source, destination):
    URL_SOURCE = f"http://www.floatrates.com/daily/{source.lower()}.json"
    r_source = requests.get(URL_SOURCE)
    result_source = json.loads(r_source.content)
    if result_source[destination.lower()]:
        rate = result_source[destination.lower()]['rate']
        convertedValue = round(montant * rate, 3)
        listeconvertedValue = [montant, source, destination, convertedValue]
        return listeconvertedValue



if __name__ == '__main__':
    writer = csv.writer(f)
    #header = ['Montant', 'Devise Initiale', 'Devise Finale', 'Montant Converti']
    #writer.writerow(header)
    montant = float(input("Entrez le montant : "))
    initial = input("Saisir une devise à convertir : ")
    final = input("Saisir une devise convertie : ")
    row = makeCurrencyConvert(montant, initial, final)
    writer.writerow(row)
    f.close()