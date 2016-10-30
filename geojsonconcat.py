import requests
import json

#Open "database" which is a shitty file with everything saved to disk
#If db.json doesn't exist can just save the json_url data to disk first time
with open('db.geojson') as data_file:    
    db = json.load(data_file)

print "Starting DB size: %d"%len(db['features'])

#Get data (example: crime data from Halifax)
json_url = r"https://opendata.arcgis.com/datasets/f6921c5b12e64d17b5cd173cafb23677_0.geojson"
r = requests.get(json_url)

#Merge lists - skip any the same
new_data_list = r.json()['features']
db['features'].extend(x for x in new_data_list if x not in db['features'])

#Update so github adds different colors/icons
for x in db['features']:
    #if not hasattr(x, 'marker-symbol'):
    if True:
        if x['properties']['RUCR_EXT_D'] == 'BREAK AND ENTER':
            x['properties']['marker-symbol'] = 'castle'
        elif x['properties']['RUCR_EXT_D'] == 'THEFT OF VEHICLE':
            x['properties']['marker-symbol'] = 'car'
        elif x['properties']['RUCR_EXT_D'] == 'THEFT FROM VEHICLE':
            x['properties']['marker-symbol'] = 'grocery-11.svg'
        elif x['properties']['RUCR_EXT_D'] == 'ASSAULT':
            x['properties']['marker-symbol'] = 'baseball-15.svg'
        elif x['properties']['RUCR_EXT_D'] == 'ROBBERY':
            x['properties']['marker-symbol'] = 'bank-11.svg'

print "Ending DB size: %d"%len(db['features'])

#Save database back to disk
with open('db.geojson', 'w') as outfile:
    json.dump(db, outfile)

