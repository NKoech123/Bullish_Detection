'''
Author : Nicholas Koech
'''
import pandas as pd
import requests,pytz # $ pip install pytz
from datetime import datetime

class Pipeline:

    '''method to extract data in a dataframe format'''
    def extract_data(self , url):

        try:
            r = requests.get (url)
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
            print("Error while trying to POST pid data")

        df_extract = pd.read_html(r.text)[0]# parse all the tables in webpages to a list

        return df_extract

    '''df argument in method below is dataframe returned from extract_data method'''
    def clean_data (self,df):

        #drop unrequired columns
        df.drop(columns=['Last 7 Days', 'Unnamed: 10','Unnamed: 0','7d','30d']) 

        #Remove dollar signs
        df['Price']=df['Price'].str.replace('$','',regex=True)
        df['Market Cap']=df['Market Cap'].str.replace('$','',regex=True)   
        df['Volume(24h)']=df['Volume(24h)'].str.replace('$','',regex=True)

        #Remove % in 25h column
        df['24h']=df['24h'].str.replace('%','',regex=True)   
        
        #Price: Convert from String to Float
        price_column_num=2
        for count,price in enumerate(df.Price):

            try:
                df.iloc[count,price_column_num]=float(price)

            except ValueError:
                df.iloc[count,price_column_num]='Nan'    #remove these rows instead of replacing with Nan

        #Market Cap: Convert to Float.  
        mkcap_column_num=4
        for row_num,mkcap_Value in enumerate(df['Market Cap']):
            if type(mkcap_Value)==str and len(mkcap_Value)>2:
                mkcap_Value=mkcap_Value.replace(',','')
                df.iloc[row_num,mkcap_column_num]=float(mkcap_Value)

        #24h Column: Convert to Float.  
        hour_column_num=3
        for row_num,hour_Value in enumerate(df['24h']):
            if type(hour_Value)==str:
                df.iloc[row_num,hour_column_num]=float(hour_Value)


        #Include time column utc/Los_Angeles tz
        df['date_time']=datetime.now(pytz.timezone("America/Los_Angeles"))

        return df

    '''method to get the columns we need for further processing.Argument is cleaned dataframe'''
    def get_meaningful_data(self,df):

        pass

class TestCases:
    pass








        





