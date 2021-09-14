import requests
import datetime
import json

'''
Function that extracts yesterdays date, formats the datetime input and 
connects to the Fingrid API-service.
Returns the data from the API-service and the date (as the time variable).
'''
def elec_generation():
    variableId_elec = 124
    api_code = {'x-api-key' : 'TEy4U6sy7k4QzcDnvhmmWaxblx7FaV1b7Li5s3OM'}
    time = datetime.date.today()-datetime.timedelta(days=1)
    time_elec  = {'start_time' :str(time)+'T00:00:00Z', 'end_time' : str(time)+'T23:59:59Z'
    }
    response_elec = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(variableId_elec), headers = api_code, params = time_elec)
    return response_elec, time

elec_generation()   

'''
Function that writes the data extracted from the API-service 
and dumps it into a new .json-file in the current directory.
'''
def elec_data_dump():
    res, time = elec_generation()
    with open('Electricity consumption in '+str(time)+'.json', 'w') as dumpfile:
        json.dump(res.json(), dumpfile)
        
elec_data_dump()