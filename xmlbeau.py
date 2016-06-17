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


url = "" #insert xml_sitemap link/url




r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)




for loc in soup.findAll("loc"):# you can also add other parameters
    try:
        writer.writeheader()

        spamwriter.writerow([loc]) #simple way to genrate CSV
        print loc
    except IndexError:
        spamwriter.writerow([loc])
        print loc



myfile.close()
#note:- this script just only for learning purpose and i am not submitted my complete code,this is just a segment of my script.

