import datetime , time, calendar, os
import meetup_rest_api as mra 
import requests as r
import json

#request events from Meetup REST API
response = r.get(mra._url("events"))
new_list = response.json()
#print (response.json())

#file storage handling
curpath = os.path.abspath(os.curdir)
filename = "eventList.json"
filepath = os.path.join(curpath, filename)
print (f"Trying to open: {filepath}")

if(os.path.exists(f"{filepath}")):
    print("oh boy here we go again....")
    with open(filepath) as f:
        old_list = json.load(f)
else :
    print("well where'd you leave it ya dingus?")
    old_list= open(f"{filepath}","w+")

#compare old and new list
if new_list != old_list:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for x in response.json():
        print(f"\nEvent: {x['name']} @Date: {x['local_date']} @Time: {x['local_time']}\n ")
        print(f"Status: {x['status']}\n")
        print(f"Link: {x['link']}\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("No New Updates")

#overwrite old list with new
with open(f'{filename}', 'w') as f:
    json.dump(new_list, f)


