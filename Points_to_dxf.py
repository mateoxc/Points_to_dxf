# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:11:20 2021

@author: Mateusz
"""

from dxfwrite import DXFEngine as dxf
import pandas as pd
df = pd.read_csv('punkty.txt', delimiter = "\t",header=None)

drawing = dxf.drawing('blok.dxf')



for index, row in df.iterrows():
    point = dxf.point((row[1],row[2],row[3]))
    point['layer'] = 'punkty'
    point['color'] = 7
    #point['point'] = (row[1],row[2],row[3]) # int or float
    
    text = dxf.text( row[0], (row[1], row[2]), height=0.4, rotation=0)
    text['layer'] = 'tekst'
    text['color'] = 7
    
    text2= dxf.text( row[3], (row[1]-1.2, row[2]-0.4), height=0.4, rotation=0)
    text2['layer'] = 'wysokosc'
    text2['color'] = 7
    
    drawing.add(text)
    drawing.add(text2)
    drawing.add(point)

drawing.save()