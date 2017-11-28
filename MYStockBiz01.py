# Malaysian Stock Biz Scrapping Ver 1

# Import libraries
import urllib2
from bs4 import BeautifulSoup
import requests

NoofStocks = 2;
# Define length of array
w, h = 2, NoofStocks;
stocks = [[0 for x in range(w)] for y in range(h)]
url = [0 for y in range(h)]
quote = [0 for y in range(h)]
# Stock name and code
stocks = [['COMFORT','2127'],
        ['GPACKET','0082']]

def getStockPrice(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  quote = soup.find(id="MainContent_lbQuoteLast")
  quote = quote.text
  return quote
  print quote

#number of stocks counter
count = 0
Max = len(stocks)
# Specift url

while (count < Max):
    url[count] = 'http://www.malaysiastock.biz/Corporate-Infomation.aspx?securityCode=%s' %(stocks[count][1])
    print url[count]
    quote[count] = getStockPrice(url[count])
    count = count + 1

if count == Max:
    print 'Latest Price Import Complete'

# query the website and return the html to the variable 'page'

#count_url = 0

#while (count_url < Max):

# Print it out just to check
print url
print quote
print stocks
