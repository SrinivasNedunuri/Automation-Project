#! /usr/bin/env python3

from PIL import Image
import os

for im in os.listdir('supplier-data/images/'):
  if '.tiff' in im:
    f,e = os.path.splitext(im)
    outfile = f+ '.jpeg'
    img = Image.open('supplier-data/images/'+im)
    out = img.resize((600,400))
    out.convert('RGB')
    out.save('supplier-data/images/'+outfile)
    print(out.size)
