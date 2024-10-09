import PySimpleGUI  as sg


window = sg.Window('Tree Element Test', layout, resizable=True, finalize=True)

while True:     # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    print(event, values)
window.close()