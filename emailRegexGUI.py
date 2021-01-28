import PySimpleGUI as sg
import pyperclip
import re


# https://stackoverflow.com/questions/55515627/pysimplegui-call-a-function-when-pressing-button
https://stackoverflow.com/questions/51455765/build-multiple-py-files-into-a-single-executable-file-using-pyinstaller

layout = [[sg.Button('Run'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Run':
        # for some reason the code stops working once run
        import emailRegex
window.Close()
