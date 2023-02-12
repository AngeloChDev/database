from bs4  import BeautifulSoup
import requests
import sqlite3

url= "https://www.wg-gesucht.de/1-zimmer-wohnungen-in-Hamburg.55.1.1.0.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
cards = doc.find_all('div', attrs={ 'class':'middle'})
div_address = doc.find_all('div', attrs={ 'class':'col-xs-11'})
metri = doc.find_all('div', attrs={ 'class':'col-xs-3 text-right'})



db= sqlite3.connect('b.db')
cursor = db.cursor()
cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA(
                 QUARTIERE TEXT ,
                 METRI TEXT ,
                 PREZZO TEXT
                )
            ''')


addr = []
costo =[]
metr2 =[]
for address in div_address:
    span = address.find('span')
    s = span.text[150:]
    addr.append(s)
for card in cards:
    eur = card.find('b').get_text()
    costo.append(eur)
costo.remove(costo[0])
for metro in metri:
    m2 = metro.find('b').get_text()
    metr2.append(m2)  
def tab():
    try: 
     
        for i in range(len(costo)):

            cursor.execute("INSERT INTO DATA(QUARTIERE,METRI,PREZZO) VALUES(?,?,?)",(addr[i], metr2[i], costo[i]))
            db.commit()
            
    except:
        print('finisch')
if __name__ == '__main__':
    tab()