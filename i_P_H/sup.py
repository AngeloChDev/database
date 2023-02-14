from bs4  import BeautifulSoup
import requests
import sqlite3
# CREA CONTENITORI E VARIABILI
anno = []
Npersone = []
reOrder = []
Berlin = []
url= "https://www.macrotrends.net/cities/204341/hamburg/population"

#CONNESSIONE ALL URL ED ESTRAZIONE DATI
with requests.get(url) as result:
    try:
        doc = BeautifulSoup(result.text, "html.parser")
        tab = doc.find('div', attrs={ 'class':'col-xs-6'})
        tbod = tab.find('tbody')
        rows = tbod.findAll('tr', recursive= True)
        for tr in rows:
            td1 = tr.find('td')
            td2 = td1.find_next()
            td1v = td1.get_text()
            tdv = td2.get_text()
            x = int(td1v)
            yy = tdv.replace(',','')
            y= int(yy)
            anno.append(x)
            Npersone.append(y)
        anno.reverse()
        Npersone.reverse()

    except:
        print('ERROR on this load Url')
    finally:
        print('Dati estratti')
with requests.get('https://www.macrotrends.net/cities/204296/berlin/population') as result:
    try:
        doc = BeautifulSoup(result.text, "html.parser")
        tab = doc.find('div', attrs={ 'class':'col-xs-6'})
        tbod = tab.find('tbody')
        rows = tbod.findAll('tr', recursive= True)
        for tr in rows:
            td1 = tr.find('td')
            td2 = td1.find_next()    
            tdv = td2.get_text()
            yy = tdv.replace(',','')
            y= int(yy)
            Berlin.append(y)
        
        Berlin.reverse()

    except:
        print('error loading berlin data')
    finally:
        print(Berlin)
# CONNESSIONE AL DATABASE CREAZIONE TABELLE
with sqlite3.connect('d.db') as db:
    cursor = db.cursor()
    try:    
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS DATA(
                        ANNO INT ,
                        PERSONE INT,
                        BERLIN INT
                        )
                    ''')
    except:
        print('La tabella non puo essere creata')
    finally:
        print('Tabella creata con successo')
# SCRITTURA TABELLE
# ORDINE ANNI
def tab():
    try: 
     
        for i in range(len(anno)):

            cursor.execute("INSERT INTO DATA(ANNO, PERSONE, BERLIN) VALUES(?,?,?)",(anno[i], Npersone[i],Berlin[i]))
            db.commit()
         
    except:
        print('was a error')
    finally:
       print('tb1 tabella creata ordinata per anni')
# OPDINE POPOLAZIONE
def order():
    cursor.execute("SELECT * FROM DATA ORDER BY PERSONE")
    myresult = cursor.fetchall()
    cursor.execute('''
             CREATE TABLE IF NOT EXISTS DATA2(
                 ANNO INT ,
                 PERSONE INT,
                 BERLIN INT
                )
            ''')
    for x in myresult:
        cursor.execute("INSERT INTO DATA2 VALUES(?,?,?)",(x[0],x[1],x[2]))
        db.commit()
    print('tb2 creata tabella ordinata per quantita')   

def List_ReOrder():
    with sqlite3.connect('d.db') as db:
        cursor = db.cursor()
        try:  
            cursor.execute("SELECT PERSONE FROM DATA2 ") 
            myresult = cursor.fetchall()
            for x in myresult:
                reOrder.append(x[0])
        except:
            print('ERROR LIST REORDERING')
        finally:
            print('La lista ordinata per numero popolazione creata')
######
        
if __name__ == '__main__':
    tab()
    order()
    List_ReOrder()