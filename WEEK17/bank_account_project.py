import PySimpleGUI as sg
import data
import ui
import actions

headings = ['TYPE', 'TITLE', 'AMOUNT', 'CATEGORY']
data_list = data.import_data()
category_list = data.return_categories(data_list)
window1 = ui.main_window(data_list, headings)

while True:
    event, values = window1.read()
    print(data_list)
    print(event, values)
    data.export_data(data_list)
    
    if event == sg.WIN_CLOSED or event == 'ACCEPT':
        break

    elif event == 'ADD CATEGORY':
        add_window = ui.add_category_window()
        while True:
            add_event, add_values = add_window.read()
            if add_event == sg.WIN_CLOSED or add_event == 'CANCEL':
                add_window.close()
                break
            elif add_event == 'SAVE':
                new_category = actions.add_category(add_values, category_list)
                if new_category:
                    category_list.append(new_category)
                    add_window.close()

    elif event == 'ADD INCOME':
        if not category_list:
            ui.custom_popup('PLEASE, FIRST ADD A CATEGORY')
        else:
            add_window = ui.add_income_window(category_list)
            while True:
                data.export_data(data_list)
                add_event, add_values = add_window.read()
                if add_event == sg.WIN_CLOSED or add_event == 'CANCEL':
                    add_window.close()
                    break
                elif add_event == 'SAVE':
                    new_income = actions.add_income(add_values, data_list)
                    if new_income: 
                        data_list.append(new_income)
                        window1['-TABLE-'].update(values=data_list)
                        add_window.close()
                

    elif event == 'ADD EXPENSE':
        if not category_list:
            ui.custom_popup('PLEASE, FIRST ADD A CATEGORY')
        else:
            add_window = ui.add_expense_window(category_list)
            while True:
                data.export_data(data_list)
                add_event, add_values = add_window.read()
                if add_event == sg.WIN_CLOSED or add_event == 'CANCEL':
                    add_window.close()
                    break
                elif add_event == 'SAVE':
                    new_expense = actions.add_expense(add_values, data_list)
                    if new_expense: 
                        data_list.append(new_expense)
                        window1['-TABLE-'].update(values=data_list)
                        add_window.close()
    window1['-TABLE-'].update(values=data_list)

window1.close()