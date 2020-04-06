#! /usr/bin/env python3

import requests
import os
url = 'http://localhost/upload/'
for im in os.listdir('supplier-data/images'):
  if '.jpeg' in im:
    with open('supplier-data/images/'+im,'rb') as opened:
      r = requests.post(url, files = {'file':opened})
