import matplotlib.pyplot  as plt
import plotly.graph_objects as po
import plotly.express as px
import pandas as pd
from sup import anno, Npersone, Berlin
import sqlite3

df = pd.DataFrame({'Anni':anno, 'N^ Persone':Npersone,'symbl':'.', 'Anni 3D':anno})

linearPlot = px.line(df, x='Anni',y = 'N^ Persone', symbol='symbl',title='Il mio Grafico sulla Crescita Demografica in Hamburg')

areaPlot = px.area(df,x='Anni',y = 'N^ Persone',text='symbl',title='Il mio Grafico sulla Crescita Demografica in Hamburg',log_y= True)
areaPlot.update_layout(title_x=0.5,title_y=0.95,title_font= dict(size= 30,color='red',family='Balto'),plot_bgcolor= 'rgba(0,0,0,0.75)',font=dict(size=20, color='black'))

sc = px.scatter(df,x='Anni',y = 'N^ Persone',title='Il mio Grafico sulla Crescita Demografica in Hamburg')

sc3d = px.scatter_3d(df,x='Anni',y = 'N^ Persone', z='Anni 3D',title='Il mio Grafico sulla Crescita Demografica in Hamburg')


sub, ax = plt.subplots()
ax.plot(anno, Npersone) 
ax.plot(anno, Berlin)
 
if __name__ == '__main__':
    #linearPlot.show()
    #areaPlot.show()
    #sc.show()
    plt.show()