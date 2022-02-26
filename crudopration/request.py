
from email import header
import re
import requests
geturl = "http://localhost:8000/getallStudent/"
header = {"content-Type" : "application/json" }

# data = requests.get(url=geturl,headers=header)
# print(data.json())

# data = {
#     "name" : "rsahul",
#     "age" : 34,
#     "country" : "In"
# }

# import json
# jsondata = json.dumps(data)
# all = requests.post(url=geturl,headers=header,data=jsondata)

# print(all.json())


data = {
    "id": 11,
    "name" : "Raj Spark SS",
   
}

import json
jsondata = json.dumps(data)
all = requests.put(url=geturl,headers=header,data=jsondata)

print(all.json())


# data = {
#     "id": 1,
#     "name" : "Raj Spark",
   
# }

# import json
# jsondata = json.dumps(data)
# all = requests.delete(url=geturl,data=jsondata)

# print(all.json())