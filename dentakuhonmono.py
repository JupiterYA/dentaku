import PySimpleGUI as sg

layout = [ 
            [sg.Button('AC'), sg.Button('   '), sg.Button('   '), sg.Button(' / '),],
            [sg.Button(' 7 '), sg.Button(' 8 '), sg.Button(' 9 '), sg.Button(' * '),],
            [sg.Button(' 4 '), sg.Button(' 5 '), sg.Button(' 6 '), sg.Button(' - '),],
            [sg.Button(' 1 '), sg.Button(' 2 '), sg.Button(' 3 '), sg.Button(' + '),],
            [sg.Button(' 0 '), sg.Button(' . '), sg.Button('   '), sg.Button(' = '),] ]

window = sg.Window('電卓',layout)

while True:

    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

window.close()
