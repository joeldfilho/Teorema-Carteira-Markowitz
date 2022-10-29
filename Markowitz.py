# Importando as bibliotecas 
import pandas as pd 
from pandas_datareader import data

df = pd.DataFrame()
df['AMZN'] = data.DataReader('AMZN', data_source='yahoo', start='1-1-2010')['Close']
df['GOOG'] = data.DataReader('GOOG', data_source='yahoo', start='1-1-2010')['Close']
df['MSFT'] = data.DataReader('MSFT', data_source='yahoo', start='1-1-2010')['Close']
df['NFLX'] = data.DataReader('NFLX', data_source='yahoo', start='1-1-2010')['Close']

df.head()