from bs4  import BeautifulSoup
import requests
import plotly.express as px
import pandas as pd
import sqlite3

anno = []
Npersone = []

url= "https://www.macrotrends.net/cities/204341/hamburg/population"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
tab = doc.find('div', attrs={ 'class':'col-xs-6'})
tbod = tab.find('tbody')
rows = tbod.findAll('tr', recursive= True)
for tr in rows:
   td1 = tr.find('td')
   td2 = td1.find_next()
   td1v = td1.get_text()
   tdv = td2.get_text()
   anno.append(td1v)
   Npersone.append(tdv)

anno.reverse()
Npersone.reverse()

fig = px.line(x=anno,y=Npersone)
fig.show()

db= sqlite3.connect('h.db')
cursor = db.cursor()
cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA(
                 persone TEXT ,
                 anni TEXT
                )
            ''')

def tab():
    try: 
     
        for i in range(len(anno)):

            cursor.execute("INSERT INTO DATA(persone, anni) VALUES(?,?)",(anno[i], Npersone[i]))
            db.commit()
         
    except:
        print('was a error')
    finally:
       print('Finisch')

if __name__ == '__main__':
    #tab()
    fig.show()