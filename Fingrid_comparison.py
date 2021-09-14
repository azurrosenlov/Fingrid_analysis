import numpy as np 
import pandas as pd
import datetime
import csv

time = datetime.date.today()-datetime.timedelta(days=1) #Extracting the date for the day before the current day
def reader(): #Reading in the .json-files created by Wind_generation.py and Electricity_consumption.py
    wind_prod = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Wind generation in {}.json'.format(str(time)))
    elec_cons = pd.read_json('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Electricity consumption in {}.json'.format(str(time)))
    return wind_prod, elec_cons

reader() #Calling the reader()-function

def sum_calc(): #Extracting the amount of energy produced and consumed
    wind_prod, elec_cons = reader()
    wind_tot = wind_prod['value'].sum() #Summed up energy produced by wind
    elec_tot = elec_cons['value'].sum() #Summed up energy consumed in total y Finland
    return wind_tot, elec_tot

sum_calc() #Calling the sum_calc()-function

def percent_share(): #Calculating the percentage and formating the result
    wind_tot, elec_tot = sum_calc()
    share_elec = wind_tot/elec_tot #Calculating the share
    result_format = '{:.0%}'.format(share_elec) #Formating the share into a percentage
    return result_format

dict_result = {'Date' : str(time), 'Percentage': percent_share()} #Storing the date and percentage as a dict
dict_keys = list(dict_result) #Creating a list of the dict keys for insertion into .csv-file as headers

#Writing the results to a .csv-file
with open('C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/Fingrid_results.csv', 'a', encoding='UTF8') as f:
    out = csv.DictWriter(f, fieldnames= dict_keys)
    if f.tell() == 0: #Adds headers if the file does not exist yet
        out.writeheader()
    
    out.writerow(dict_result) #Writes the result as a row in .csv-file
