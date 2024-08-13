import ui

def add_category(values, category_list):
    new_category = values['-CATEGORY_INPUT-'].strip().upper()
    if new_category:
        if new_category in category_list:
            ui.custom_popup(f'Category "{new_category}" already exists!')
        else:
            category_list.append(new_category)
            ui.custom_popup(f'Category "{new_category}" added!')
            print(category_list)
    else:
        ui.custom_popup('Category name cannot be empty!')

def add_income(values, data_list):
    try:
        new_title_income = values['-TITLE_INCOME-'].strip()
        new_amount_income = float(values['-AMOUNT_INCOME-'])
        new_category_income = values['-CATEGORY_INCOME-'].strip()
    
        if not new_title_income:
            ui.custom_popup('No title, please enter a title.')
        elif new_category_income == 'NONE' or not new_category_income:
            ui.custom_popup('No category, please select a category.')
        else:
            data_list.append(['INCOME', new_title_income, new_amount_income, new_category_income])
            ui.custom_popup(f'Income "{new_title_income}" added.')
            print(data_list)
    except ValueError:
        ui.custom_popup('Invalid amount, make sure you are typing a number.')

def add_expense(values, data_list):
    try:
        new_title_expense = values['-TITLE_EXPENSE-'].strip()
        new_amount_expense = float(values['-AMOUNT_EXPENSE-'])
        new_category_expense = values['-CATEGORY_EXPENSE-'].strip()

        if not new_title_expense:
            ui.custom_popup('No title, please enter a title.')
        elif new_category_expense == 'NONE' or not new_category_expense:
            ui.custom_popup('No category, please select a category.')
        elif new_amount_expense < 0:
            ui.custom_popup('Invalid amount, make sure you are typing an amount over 0.')
        else:
            data_list.append(['EXPENSE', new_title_expense, new_amount_expense, new_category_expense])
            ui.custom_popup(f'Expense "{new_title_expense}" added.')
            print(data_list)
    except ValueError:
        ui.custom_popup('Invalid amount, make sure you are typing a number.')
