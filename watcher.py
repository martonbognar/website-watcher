import csv

from checker import Checker
from website import Website


READER = csv.reader(open('sites.csv'), delimiter=' ')

CHECKER = Checker()

for entry in READER:
    CHECKER.add_site(Website(entry[0], int(entry[1])))

CHECKER.run()
