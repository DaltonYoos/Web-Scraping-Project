import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                   '13', '14', '15', '16', '17', '18', '19', '20', '21']

i = random.choice(chapters)

webpage = 'https://ebible.org/asv/JHN'

webpage = webpage + i + '.htm'
print(webpage)

#Professor B's Method
'''
random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
print(webpage)

'''

#webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

page_verses = soup.findAll('div',class_='main')

#print(page_verses)
#tag is /div

for verse in page_verses:
    verse_list = verse.text.split(".")

#print(verse_list)

myverse = random.choice(verse_list[:len(verse_list)-5])

#print(f"Chapter: {i} , Verse: {myverse}")

message = "Chapter: " + i + " Verse:" + myverse

print(message)

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+12283055063"

myCellPhone = "+18053584626"

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
print(textmessage.status)
