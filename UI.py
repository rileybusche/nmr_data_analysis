import PySimpleGUI as sg
import os.path


# First Column
file_list_column = [
    [
        sg.Text("File Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
        )
    ]
]

# Set Layout 
layout = [
    [
        sg.Column(file_list_column)
    ]
]

window = sg.Window("File Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # File in File List
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        window["-FILE LIST-"].update(file_list)

window.close()