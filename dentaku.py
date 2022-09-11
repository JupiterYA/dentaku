import PySimpleGUI as sg

# ウィンドウの内容を定義する
layout = [[sg.Text("ウンチーコングって知ってる？")],
          [sg.Button('はい'), sg.Button('いいえ')]]

# ウィンドウを作成する
window = sg.Window('ウソチーコング',layout)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    window.refresh()

    event, values = window.read()
    # ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == 'いいえ':
        break
    if event == 'はい':
        sg.popup('ウ　ン　チ　ー　コ　ン　グだにどとまちがえるなくそが', title='くそが') 
    if event == sg.WINDOW_CLOSED:
        sg.popup('唐揚弁当食す', title='消えなさい') 
        break
    

# 画面から削除して終了
window.close()