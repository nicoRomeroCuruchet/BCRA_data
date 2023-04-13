import requests
import pandas as pd

class BcraApi:
    
    def __init__(self, api_key):
        self.base_url = 'https://api.estadisticasbcra.com/'
        self.api_key  =  api_key
        self.headers  = {'Authorization': 'Bearer ' + api_key}

    def __parser__(self, df, column_name):

        df.rename(columns={'d': 'Date', 'v': column_name}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
        df.sort_values('Date', ascending=False, inplace=True)
        return df

    def __request__(self, url, name):
        
        response = requests.get(url, headers=self.headers)
        return self.__parser__(pd.DataFrame(response.json()), name)

    def get_series(self, metric):

        url = self.base_url + str(metric).strip()
        return self.__request__(url, str(metric).strip())
    
