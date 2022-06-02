import json
import os
from datetime import date

nama_objek_2="saya"
nama_objek_3="07.20"
today = date.today()
d1 = today.strftime("%d-%b-%Y")
# Data to be written
dictionary =[{
    "name" : nama_objek_2,
    "jam" : nama_objek_3
}]
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 2)
# Writing to sample.json
with open("Database/"+d1+".json", "w") as outfile:
    outfile.write(json_object)