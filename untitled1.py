# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:47:28 2021

@author: user
"""

import easyocr
import PIL
import re
import pandas as pd
from PIL import ImageDraw
from geotext import GeoText
from datetime import datetime
from collections import defaultdict
import numpy as np

reader = easyocr.Reader(['en'])

im = PIL.Image.open(r'D:\otimised_poc_ocr\images\Final_simple9.jpg')

invoice_dict = defaultdict(list)

text = reader.readtext(im,detail=0, paragraph=True)
text1=str(text)

text4=str(text)
text4=re.sub(r'[^0-9a-zA-Z._-]'," ",text4)
text4=text4.replace(' . ','.').replace('38 ','38.').replace('Tin','TIN').replace('28 . ','28.').replace('28 ','28.')

corpus=r'BOX\s{4}(\d{3}.\d+\s)|TIN\s{4}(\d{2}.\d+\s)|KGM\s{4}(\d+.\d+\s)|MR\d+\s{4}(\d+.\d+)'
text4=re.findall(corpus,text4)

unit_price = []

for i in text4:
   i=str(i)
   i=re.sub(r'[^0-9.]',' ',i)
   i=i.strip()
   unit_price.append(i)