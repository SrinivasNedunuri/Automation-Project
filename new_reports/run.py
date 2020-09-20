#! /usr/bin/env python3
# uploading fruit description and image to the server.

import os
import requests

for file in os.listdir('supplier-data/descriptions'):
  img_name = file.split('.')
  img_name = img_name[0]+'.jpeg'
  with open('supplier-data/descriptions/'+file) as desc:
    lines = desc.readlines()
    list = []
    dict = {}
    for line in lines:
      lin = line.strip()
      list.append(lin)
    dict["name"] = list[0]
    dict["weight"] = list[1].split()[0]
    dict["description"] = list[2]
    dict['image_name'] = img_name
    response = requests.post('http://35.224.42.94/fruits/',data = dict)
