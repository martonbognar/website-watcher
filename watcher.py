import csv
import requests

READER = csv.reader(open('sites.csv'), delimiter=' ')

SITES = []

for entry in READER:
    SITES.append({'url': entry[0], 'period': int(entry[1])})
