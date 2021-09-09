# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:31:31 2021

@author: Mateusz
"""


import PySimpleGUI as sg

def make_window(theme):
    sg.theme('Dark Blue 3')
    right_click_menu_def = [[], ['Exit']]

    
    
    
    layout = [[sg.Text("Konsola")], [sg.Output(size=(60,10), font='Courier 8')],
            [sg.Button("Wybierz plik")],
            [sg.Button("Generuj blok")],
            [sg.Button("Exit")]] 
             
    return sg.Window('GUI point_to_dxf', layout, right_click_menu=right_click_menu_def)



def main():
    window = make_window(sg.theme())
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)        
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Czynnosc = ', event, ' ==============')
        
            for key in values:
                print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        elif event == "Wybierz plik":
            fname=sg.popup_get_file('Wybierz plik')
            print('Czynnosc = ', 'wybrano plik',fname)
        elif event == "Generuj blok":
            txt_dxf(fname)
            print('============ Czynnosc = ', 'wygenerowano blok', ' ==============')
        elif event == "Exit":
            window.close()
        
            

    window.close()
    exit(0)

def txt_dxf(fname):
    from dxfwrite import DXFEngine as dxf
    import pandas as pd
    df = pd.read_csv(fname, delimiter = "\t",header=None)
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
    
    
if __name__ == '__main__':
    main()