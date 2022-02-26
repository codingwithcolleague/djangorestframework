import requests
import json
# data = requests.get(url="http://localhost:8000/studentdetails/")
# print(data.json())

data = {
    "name" : "Simran",
    "age" : 13,
    "country" : "Inss"
}

json_data = json.dumps(data) 
r = requests.post(url="http://localhost:8000/studentcreate/" ,data=json_data)

print(r.json())