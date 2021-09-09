import numpy as np 
import pandas as pd

def reader():
    wind_prod = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Wind generation in 2021-09-07.json')
    elec_cons = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Electricity consumption in 2021-09-07.json')
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

print('The share of the total electricity consumption that can come from wind generated electricity is: ' + str(percent_share()))
