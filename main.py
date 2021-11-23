import csv
import json

import requests

def main(lat: float, lng: float, radius: int):
    url = f'https://docs.openaq.org/v2/locations?limit=1000&page=1&offset=0&sort=desc&coordinates={lat}%2C{lng}&radius={radius}&order_by=lastUpdated&dumpRaw=false'
    print(url)
    res = requests.get(url)
    data = json.loads(res.content)
    fieldnames = []
    rows = data['results']
    for row in rows:
        keys = row.keys()
        for key in keys:
            if key not in fieldnames:
                fieldnames.append(key)
    with open('locations.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data['results'])


main(35.0844,-106.6504,10000)