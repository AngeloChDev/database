import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs


url ='https://www.macrotrends.net/cities/204341/hamburg/population'
result = rq.get(url)
x = bs(result.text, 'html.parser')
a = x.find_all('a')
print(a)