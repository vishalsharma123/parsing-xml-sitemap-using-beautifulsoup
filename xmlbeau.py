from bs4 import BeautifulSoup
import requests
import re
import urllib
import requests
import mechanize
from bs4 import BeautifulSoup
import re
import csv
from itertools import izip
myfile = open("myfile.csv",'wb')
spamwriter = csv.writer(open("myfile.csv",'wb'))
fieldnames = ['URL']
writer = csv.DictWriter(myfile, fieldnames=fieldnames)


spamwriter = csv.writer(myfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


url = "http://sitemaps.trustpilot.com/domains11_it-ch.xml"




r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)




for loc in soup.findAll("loc"):
    try:
        writer.writeheader()

        spamwriter.writerow([loc])
        print loc
    except IndexError:
        spamwriter.writerow([loc])
        print loc



myfile.close()

