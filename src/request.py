import requests
from src.priv_api import API_KEY

# Station ID numbers
ashfield_id = 486
kogarah_id = 487
seven_hills_id = 488
manly_vale_id = 489

# Mapping station names from input to id
station_dict = {
    'ashfield': ashfield_id,
    'kogarah': kogarah_id,
    'seven hills': seven_hills_id,
    'manly vale': manly_vale_id,
}

BASE_URL = 'https://api.transport.nsw.gov.au/v1'


def get_station_occupancy_data(station_lowercase):
    data = {
        'facility': station_dict[station_lowercase]
    }

    header = {'Authorization' : API_KEY}
    url_endpoint = f'{BASE_URL}/carpark'

    r = requests.get(url_endpoint, headers=header, params=data)
    data = (r.json())

    total_spots = int(data["spots"])
    curr_occupancy = int(data["occupancy"]["total"])
    available_spots = total_spots - curr_occupancy

    if (available_spots <= 0):
        status = 'FULL'
    elif available_spots/total_spots <= 0.1:
        status = 'There are parking spaces but almost at capacity'
    else:
        status = 'There are parking spaces'

    ret_dict = {
        'station_name': station_lowercase,
        'total_spots': total_spots,
        'curr_occupancy': curr_occupancy,
        'available_spots': available_spots,
        'status': status,
    }

    return ret_dict
    

