from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url1 = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url1, headers=headers)		

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

tablecells = soup.findAll("div",attrs={"class":"table-cell"})

'''
highvalue = float(tablecells[5].text)
lowvalue = float(tablecells[6].text)

value = (highvalue - lowvalue)
perchange = (value / lowvalue) * 100

print("Number:" ,tablecells[0].text)
print("Company Name: ", tablecells[1].text)
print("% Chance In 1 Day:", tablecells[3].text)
print("High: ", tablecells[5].text)
print("Low:", tablecells[6].text)

name = 1
high = 5
low = 6
'''
count = 1

for x in range(5):
    
    name = tablecells[count].text
    change = tablecells[count+2].text
    high = float(tablecells[count+4].text)
    low = float(tablecells[count+5].text)

    calc_change = round(((high - low)/low) * 100, 2)

    print(name)
    print(f"Change in %:' {change}")
    print(f"High: {high}")
    print(f"Low: {low}")
    print(f"Calculated Change: {calc_change}")
    print()
    print()

    count += 11
