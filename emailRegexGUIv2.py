import PySimpleGUI as sg
import pyperclip
import re


# https://stackoverflow.com/questions/55515627/pysimplegui-call-a-function-when-pressing-button
# https://stackoverflow.com/questions/51455765/build-multiple-py-files-into-a-single-executable-file-using-pyinstaller

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find matches in the clipboard text
text = str(pyperclip.paste())

layout = [[sg.Button('Run'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Run':
        matches = []
        for groups in emailRegex.findall(text):
            matches.append(groups[0])
        # Copy results to the clipboard.
        if len(matches) > 0:
            pyperclip.copy('\n'.join(matches))
            print('Copied to the clipboard:')
            print('\n'.join(matches))
        else:
            print('No email addresses found')

window.Close()