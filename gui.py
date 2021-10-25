import PySimpleGUI as sg
import os.path

frequencies = []


# First Column
layout = [
    [
        sg.Text("File Folder")
    ],
    [
        sg.In(size=(50,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    # Frequency
    [  
        sg.Text("Frequencies")
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(100,20), key="-FREQUENCY LIST-")
    ],
    [
        sg.In(size=(25,1), enable_events=True, key="-FREQUENCY-"),
        sg.Button(button_text="Add", enable_events=True, key="-ADD-"),
        sg.Button(button_text="Remove", enable_events=True, key="-REMOVE-"),
        sg.Button(button_text="Clear", enable_events=True, key="-CLEAR-")
    ]
]

sg.theme('dark grey 9')
window = sg.Window("File Viewer", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Adding Frequency to list
    if event == "-ADD-":
        if values["-FREQUENCY-"].strip() != "" and values["-FREQUENCY-"].strip() not in frequencies:
            frequencies.append(values["-FREQUENCY-"])
            print(frequencies)

        window["-FREQUENCY LIST-"].update(frequencies)
    # Removes freq. from list
    if event == "-REMOVE-":
        selected_frequency = values["-FREQUENCY LIST-"]
        if selected_frequency != []:
            frequencies.remove(selected_frequency[0])
            window["-FREQUENCY LIST-"].update(frequencies)
    if event == "-CLEAR-":
        frequencies = []
        window["-FREQUENCY LIST-"].update(frequencies)

window.close()