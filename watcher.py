import csv

from checker import Checker
from website import Website


READER = csv.reader(open('sites.tsv'), delimiter='\t')
next(READER)

CHECKER = Checker()

for entry in READER:
    CHECKER.add_site(Website(url=entry[0], period=int(entry[1])))

CHECKER.run()
