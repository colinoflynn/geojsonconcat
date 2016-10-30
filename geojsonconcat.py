import requests
import json

#Open "database" which is a shitty file with everything saved to disk
with open('db.json') as data_file:    
    db = json.load(data_file)

print "Starting DB size: %d"%len(db['features'])

#Get data (example: crime data from Halifax)
json_url = r"https://opendata.arcgis.com/datasets/f6921c5b12e64d17b5cd173cafb23677_0.geojson"
r = requests.get(json_url)

#Merge lists - skip any the same
new_data_list = r.json()['features']
db['features'].extend(x for x in new_data_list if x not in db['features'])

print "Ending DB size: %d"%len(db['features'])

#Save database back to disk
with open('db.json', 'w') as outfile:
    json.dump(db, outfile)

