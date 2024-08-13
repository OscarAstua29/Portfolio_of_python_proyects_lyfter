import PySimpleGUI as sg

sg.change_look_and_feel('Light green 1')

def main_window(data_list, headings):
    layout = [
        [sg.Table(data_list, headings=headings, col_widths=[100, 100, 200], max_col_width=2, background_color='lightblue',
                  auto_size_columns=True, display_row_numbers=True, justification='left',
                  alternating_row_color='white', key='-TABLE-', size=(100, 30))],
        [sg.Button('ADD INCOME'), sg.Button('ADD EXPENSE'), sg.Button('ADD CATEGORY')]
    ]
    return sg.Window('MAIN WINDOW', layout, finalize=True)

def custom_popup(message, title='WARNING'):
    layout = [
        [sg.Text(message)],
        [sg.Button('ACCEPT')]
    ]
    popup_window = sg.Window(title, layout, modal=True, finalize=True)
    
    while True:
        event, _ = popup_window.read()
        if event == 'ACCEPT' or event == sg.WIN_CLOSED:
            break
    
    popup_window.close()

def add_category_window():
    layout = [
        [sg.Text('WRITE THE NAME OF THE NEW CATEGORY')],
        [sg.Input(key='-CATEGORY_INPUT-')],
        [sg.Button('SAVE'), sg.Button('CANCEL')]
    ]
    return sg.Window('ADD CATEGORY', layout, finalize=True)

def add_income_window(category_list):
    layout = [
        [sg.Text('TITLE')],
        [sg.Input(key='-TITLE_INCOME-')],
        [sg.Text('AMOUNT')],
        [sg.Input(key='-AMOUNT_INCOME-')],
        [sg.Text('CATEGORY')],
        [sg.Combo(category_list, key='-CATEGORY_INCOME-', default_value='NONE', size=(45, 3), background_color='white', text_color='black',readonly=True,)],
        [sg.Button('SAVE'), sg.Button('CANCEL')]
    ]
    return sg.Window('ADD INCOME', layout, finalize=True)

def add_expense_window(category_list):
    layout = [
        [sg.Text('TITLE')],
        [sg.Input(key='-TITLE_EXPENSE-')],
        [sg.Text('AMOUNT')],
        [sg.Input(key='-AMOUNT_EXPENSE-')],
        [sg.Text('CATEGORY')],
        [sg.Combo(category_list, key='-CATEGORY_EXPENSE-', default_value='NONE', size=(45, 3), background_color='lightblue', text_color='black', readonly =True, tooltip = 'white')],
        [sg.Button('SAVE'), sg.Button('CANCEL')]
    ]
    return sg.Window('ADD EXPENSE', layout, finalize=True)