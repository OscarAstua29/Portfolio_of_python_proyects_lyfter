'''categories_list = []
data_list = [['EXPENSE','AGUA',1000.0,'CASA'],['EXPENSE','AGUA',1000.0,'CASA'],['EXPENSE','AGUA',1000.0,'CASA'],
['INCOME','QI',22000.0,'SALARIO']] 

for row in data_list:
    category = row[1]
    if not category in categories_list:
        categories_list.append(category)

print (categories_list)'''


import PySimpleGUI as sg

# Declarar los elementos
layout = [
    [sg.Combo(['opción1', 'opción2'], key='-CATEGORY_EXPENSE-', default_value='NONE', size=(45, 3), background_color='lightblue', text_color='black', readonly=True, tooltip='gray')],
]

# Crear la ventana
window = sg.Window("Primer programa", layout)

# Event Loop para procesar "events" y obtener los "values" de los inputs
while True:
    event, values = window.read()
    # Procesar el evento del cerrar la ventana
    if event == sg.WIN_CLOSED:
        break

window.close()
