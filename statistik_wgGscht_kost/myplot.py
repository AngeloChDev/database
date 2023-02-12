import plotly.express as px
import sqlite3
from sup import  costo, metr2

db= sqlite3.connect('b.db')
cursor = db.cursor()
cursor.execute("SELECT QUARTIERE FROM DATA")
quartieri = cursor.fetchall()
x = costo
y = metr2
z = quartieri
fig = px.scatter_3d(x=x,y=y,z=z)
if __name__ == '__main__':
    fig.show()