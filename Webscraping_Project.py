from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import keys2
from twilio.rest import Client

url = 'https://crypto.com/price'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)		

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+12283055063"

myCellPhone = "+18053584626"

table_rows = soup.findAll("tr")



for coin in table_rows[1:6]:

    #coin_row = coin.findAll('td')
    crypto = coin.findAll('p')
    price = coin.findAll('div')
    symbol = coin.findAll('span')
    #constantly changing p-value in inspect element due to volatility of crypto, especially in todays market. Div tag was consistent.


    coin_name = crypto[0].text
    coin_per_change = crypto[1].text
    coin_value = price[6].text
    coin_symbol = symbol[2].text

    
    coin_value = (coin_value.replace(",",""))
    coin_price = float(coin_value.replace("$",""))
    per_chng = float(coin_per_change.replace("%",""))

    total_per_chng = (per_chng/100)


    calculation1 = coin_price*total_per_chng
    calculation2 = coin_price-calculation1


    print("Coin Name: ",coin_name)
    print("Coin Symbol: ", coin_symbol)
    print("Coin Price: ", coin_value)
    print("Percent Change: ", per_chng,"%")
    print("Cost of Coin 24 Hours Ago:","${:,.2f}".format(calculation2))
    print()
    print()
    print()

    input()

    if coin_name == "Bitcoin" and coin_price < 40000:

        btc_mssg = "A Single Bitcoin has fallen below $40,000 USD!"
        btc_txt_mssg = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=btc_mssg)
        print(btc_txt_mssg.status)
                    



    if coin_name == "Ethereum" and coin_price < 3000:

        eth_mssg = "A Single Ethereum Coin has fallen below $3,000 USD!"
        eth_txt_mssg = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=eth_mssg)
        print(eth_txt_mssg.status)






















