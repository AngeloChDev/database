from bs4  import BeautifulSoup
import requests
import sqlite3

url= "https://www.wg-gesucht.de/1-zimmer-wohnungen-in-Hamburg.55.1.1.0.html"
result = requests.get(url)                                                     ####  CONNECT THE URL
doc = BeautifulSoup(result.text, "html.parser")                                ### EXSTRACT HTML CODE
cards = doc.find_all('div', attrs={ 'class':'middle'})                         ### SEARCH DATA 
div_address = doc.find_all('div', attrs={ 'class':'col-xs-11'})                
metri = doc.find_all('div', attrs={ 'class':'col-xs-3 text-right'})
db= sqlite3.connect('sq2.db')                                                  ## CONNECT TO THE DATABASE 
cursor = db.cursor()
cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA(
                 QUARTIERE TEXT ,
                 METRI TEXT ,
                 PREZZO TEXT
                )
            ''')                                                             ## CREATE TABLE
                                                                            ##CREATE TABLE
addr = []                                                                   ### CREATE LIST WHERE INSERT DATA
costo =[]
metr2 =[]
for address in div_address:                                                 ### TAKE THE VALUE
    span = address.find('span')
    s = span.text[150:]
    cursor.execute("INSERT INTO DATA(QUARTIERE) VALUES(?)",(s,))
    addr.append(s)
for card in cards:                                                               ### TAKE THE VALUE
    eur = card.find('b').get_text()
    
    valore = str(eur).split('ab')[0] 
    costo.append(valore)
    cursor.execute("INSERT INTO DATA(PREZZO) VALUES(?)",(valore,))
    print(valore)
for metro in metri:                                                                  ### TAKE THE VALUE
    m2 = metro.find('b').get_text()
    metr2.append(m2)
    cursor.execute("INSERT INTO DATA(METRI) VALUES(?)",(m2,))
#cursor.execute("INSERT INTO DATA(QUARTIERE,METRI,PREZZO) VALUES(?,?,?)",(s,))          ## INSERT VALUES IN TABLE
db.commit()    
x=1
  