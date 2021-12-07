# img_viewer.py

import PySimpleGUI as sg
import os.path

image_elem = sg.Image()

tools = [[
        sg.Button('Open'),
        sg.Button('Prev'),
        sg.Button('Next'),
        sg.Button('Insert'),
        sg.Button('Delete'),
        
    ],
    [image_elem]
    ]
    



# ----- Full layout -----


window = sg.Window("Image Viewer", tools)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
