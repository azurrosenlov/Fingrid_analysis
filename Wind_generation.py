import requests
import datetime
import json

def wind_generation():
    variableId_wind = 75
    api_code = {'x-api-key' : 'TEy4U6sy7k4QzcDnvhmmWaxblx7FaV1b7Li5s3OM'}
    time = datetime.date.today()-datetime.timedelta(days=1)
    time_wind  = {'start_time' :str(time)+'T00:00:00Z', 'end_time' : str(time)+'T23:59:59Z'
    }
    response_wind = requests.get('https://api.fingrid.fi/v1/variable/{}/events/json'.format(variableId_wind), headers = api_code, params = time_wind)
    return response_wind, time

wind_generation()   

def wind_data_dump():
    res, time = wind_generation()
    with open('Wind generation in '+str(time)+'.json', 'w') as dumpfile:
        json.dump(res.json(), dumpfile)
        
wind_data_dump()