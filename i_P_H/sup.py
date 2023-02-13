from bs4  import BeautifulSoup
import requests
import plotly
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
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

db= sqlite3.connect('h.db')
cursor = db.cursor()
cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA(
                 ANNO TEXT ,
                 PERSONE TEXT
                )
            ''')

def tab():
    try: 
     
        for i in range(len(anno)):

            cursor.execute("INSERT INTO DATA(ANNO, PERSONE) VALUES(?,?)",(anno[i], Npersone[i]))
            db.commit()
         
    except:
        print('was a error')
    finally:
       print('Finisch')

reOrder = []
#df = pd.DataFrame({'x':anno, 'y':Npersone})
#fig = go.Figure([go.Scatter(x=df['x'], y=df['y'])])
#fig = px.line(df,x=anno,y=Npersone)
def order():
    cursor.execute("SELECT * FROM DATA ORDER BY PERSONE")
    myresult = cursor.fetchall()
    cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA2(
                 ANNO TEXT ,
                 PERSONE TEXT
                )
            ''')
    for x in myresult:
        cursor.execute("INSERT INTO DATA2 VALUES(?,?)",(x[0],x[1]))
        db.commit()
        
#def saveASnewLIST():
    
cursor.execute("SELECT PERSONE FROM DATA2 ")
myresult = cursor.fetchall()
for x in myresult:
    reOrder.append(x[0])



#df = pd.DataFrame({'anni_x':anno, 'N_P':Npersone})
fig = go.Figure([go.Scatter(x=anno, y=Npersone)])
#fig = px.line(df,x='nom_x',y='nom_y')



if __name__ == '__main__':
    #tab()
    fig.show()
    #order()
    #saveASnewLIST()
    
    
    print(anno)