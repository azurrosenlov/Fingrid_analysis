import numpy as np 
import pandas as pd
import datetime
#import json
import csv

time = datetime.date.today()-datetime.timedelta(days=1)
def reader():
    wind_prod = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Wind generation in {}.json'.format(str(time)))
    elec_cons = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Electricity consumption in {}.json'.format(str(time)))
    return wind_prod, elec_cons

reader() 

def sum_calc():
    wind_prod, elec_cons = reader()
    wind_tot = wind_prod['value'].sum()
    elec_tot = elec_cons['value'].sum()
    return wind_tot, elec_tot

sum_calc()

def percent_share():
    wind_tot, elec_tot = sum_calc()
    share_elec = wind_tot/elec_tot
    result_format = '{:.0%}'.format(share_elec)
    return result_format

dict_result = {'Date' : str(time), 'Percentage': percent_share()}
dict_keys = list(dict_result)

#with open('Daily share wind generation and power consumption', 'a') as f:
#    f.write(json.dumps(dict_result))

with open('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Fingrid_csv', 'a', encoding='UTF8') as f:
    out = csv.DictWriter(f, fieldnames= dict_keys)
    out.writeheader()
    out.writerow(dict_result)
