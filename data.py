from config import Key,Secret
import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import pandas as pd
from datetime import timedelta,datetime
import math
import dateutil
import numpy
import parser
import matplotlib.pyplot as plt
import csv
import sys


cliente_binance = Client(Key,Secret)

info = cliente_binance.get_account()
#print(info) #toda la info de la cuenta(que cryptos tiene,etc)
all_cryptos = info['balances']

df_all_cryptos =pd.DataFrame(all_cryptos)
#print(df_all_cryptos)


df_all_cryptos.free = df_all_cryptos.free.astype(float)
billetera = df_all_cryptos[df_all_cryptos['free'] > 0]
#print(billetera)
time_res =cliente_binance.get_server_time()
ts = time_res.get('serverTime')
#print(datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d'))   #fecha actual

fecha_inicio ="1 Jul 2022"
fecha_final =datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d')


currencies = []
for item in billetera['asset']:
    currencies.append(item)
#print(currencies)
exepciones_crypto = ["USDT","LDBNB"]




for e in (exepciones_crypto):
    currencies.remove(e)

f2 = open("./Monedas/currencies.csv","w") 
df_currencies = pd.DataFrame(currencies)
df_currencies.rename(columns= {'0':'Monedas'})
df_currencies.to_csv("./Monedas/currencies.csv",index= False)
print(df_currencies.columns) 
print(df_currencies)
f2.close()

'''dict_monedas = {'Monedas':[]}
df_money = pd.DataFrame(dict_monedas)
print(df_money)
for item in currencies:
    df_money['Monedas'].append(item)
    print(df_money)'''



df_velas1 = pd.DataFrame()

for item in currencies:

    filename = '%s-data.csv' % (item)
    f1 = open("./Monedas/%s" %(filename),"w")

    velas1 = cliente_binance.get_historical_klines((item+'USDT'),Client.KLINE_INTERVAL_1DAY,fecha_inicio,fecha_final)
    velas =pd.DataFrame(velas1)    
    df_velas = velas.drop(range(2, 12), axis=1)
    df_velas.columns = ('Fecha','Precio')
    df_velas['Fecha'] = pd.to_datetime(df_velas['Fecha'],unit=('ms'))
    df_velas.to_csv('./Monedas/%s' % (filename), index =False)

    #print(df_velas)
    #f1.write("%s \n" %df_velas)
    f1.close()
    #print(df_velas)

print("Datos actualizados con exito")




















#velas = cliente_binance.get_historical_klines(currencies,Client.KLINE_INTERVAL_1DAY,"1 Jul 2022","4 Jul 2022")


#df_velas['Fecha'] = pd.to_datetime(df_velas['Fecha'],unit=('ms'))
#print(df_velas)













