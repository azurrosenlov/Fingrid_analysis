import requests
import datetime
import json
import os

'''
Function that extracts yesterdays date, formats the datetime input and 
connects to the Fingrid API-service.
Returns the data from the API-service and the date (as the time variable).
'''
def wind_generation(): 
    variableId_elec = 124
    api_code = {'x-api-key' : 'TEy4U6sy7k4QzcDnvhmmWaxblx7FaV1b7Li5s3OM'} #This should be changed to your personal API-code that you generate from Fingrid API website
    date_elec = datetime.date.today()-datetime.timedelta(days=1)
    time_elec  = {'start_time' :str(date_elec)+'T00:00:00Z', 'end_time' : str(date_elec)+'T23:59:59Z'
    }
    response_elec = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(variableId_elec), headers = api_code, params = time_elec)
    return response_elec, date_elec

'''
Function that writes the data extracted from the API-service 
and dumps it into a new .json-file in the current directory.
'''
def wind_data_dump():
    response_elec, date_elec = wind_generation()
    file_path = '/c/Users/azur.rosenlov/Desktop/Data_Academy_Python/' #Must be Unix style file path
    file_path_elec = '{}Electricity consumption in {}.json'.format(file_path, date_elec)
    os.chdir(file_path) #Changes the directory to the specified file path
    with open(file_path_elec, 'w') as dumpfile:
        json.dump(response_elec.json(), dumpfile)
        


def main():
    wind_generation()
    wind_data_dump()


if __name__ == '__main__':
    main()