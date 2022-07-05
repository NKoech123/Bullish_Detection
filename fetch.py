#Trending Crypto in CoinmarketCap
import pandas as pd
import requests,pytz # $ pip install pytz
from datetime import datetime


url = "https://coinmarketcap.com/trending-cryptocurrencies/"

try:
    r = requests.get(url)
except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
    print("Error while trying to POST pid data")
df_newcoin = pd.read_html(r.text) # parse all the tables in webpages to a list
df=df_newcoin[0].drop(columns=['Last 7 Days', 'Unnamed: 10','Unnamed: 0','7d','30d']) #drop unrequired columns

df[:3]