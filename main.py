import meetup_rest_api as mra 
import requests as r
import json

response = r.get(mra._url("events"))
print (response.json())

for x in response.json():
    print(f"Event: {x['name']} with the occurs on Date: {x['local_date']}\n Link: {x['link']}")