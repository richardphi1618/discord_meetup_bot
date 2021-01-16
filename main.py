import meetup_rest_api as mra 
import requests as r
import json

response = r.get(mra._url("events"))
print (response.json())
