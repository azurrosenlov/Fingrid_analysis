import pandas as pd
import datetime
import csv
import os

#time = datetime.date.today()-datetime.timedelta(days=1) #Extracting the date for the day before the current day
def reader(): #Reading in the .json-files created by Wind_generation.py and Electricity_consumption.py
    dates = datetime.date.today()-datetime.timedelta(days=1) #Extracting the date for the day before the current day
    file_path = 'C:/Users/azur.rosenlov/Desktop/Data_Academy_Python/' #File path must be written as Unix style
    os.chdir(file_path)
    wind_prod = pd.read_json('{}Wind generation in {}.json'.format(file_path, dates))
    elec_cons = pd.read_json('{}Electricity consumption in {}.json'.format(file_path, dates))
    #wind_prod = pd.read_json('C:/Users/azur.rosenlov/airflow/dags/Wind generation in {}.json'.format(str(dates)))
    #elec_cons = pd.read_json('C:/Users/azur.rosenlov/airflow/dags/Electricity consumption in {}.json'.format(str(dates)))    
    return wind_prod, elec_cons

def sum_calc(): #Extracting the amount of energy produced and consumed
    wind_prod, elec_cons = reader()
    wind_tot = wind_prod['value'].sum() #Summed up energy produced by wind
    elec_tot = elec_cons['value'].sum() #Summed up energy consumed in total by Finland
    return wind_tot, elec_tot

def percent_share(): #Calculating the percentage and formating the result
    wind_tot, elec_tot = sum_calc()
    share_elec = wind_tot/elec_tot #Calculating the share
    result_format = '{:.0%}'.format(share_elec) #Formating the share into a percentage
    return result_format

def csv_writer():
    time = datetime.date.today()-datetime.timedelta(days=1) #Extracting the date for the day before the current day
    dict_result = {'Date' : str(time), 'Percentage': percent_share()} #Storing the date and percentage as a dict
    dict_keys = list(dict_result) #Creating a list of the dict keys for insertion into .csv-file as headers

    #Writing the results to a .csv-file
    #with open('mnt/c/Users/azur.rosenlov/Desktop/Data_Academy_Python/Fingrid_results.csv', 'a', encoding='UTF8') as f:
    with open('Fingrid_results.csv', 'a', encoding='UTF8') as f:
        out = csv.DictWriter(f, fieldnames= dict_keys)
        if f.tell() == 0: #Adds headers if the file does not exist yet
            out.writeheader()
        
        out.writerow(dict_result) #Writes the result as a row in .csv-file

def main():
    reader() #Calling the reader-function
    sum_calc() #Calling the sum_calc-function
    percent_share() #Calling percent_share function, returning the percent share, formatted
    csv_writer() #Calling csv_writer function, writing to csv-file

if __name__ == '__main__':
    main()

