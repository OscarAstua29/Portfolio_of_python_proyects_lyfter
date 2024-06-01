def organized_string (string_to_order):
        string_list = string_to_order.split("-") 
        organized_list = sorted(string_list)
        organized_complete_string = "-".join(organized_list)
        return organized_complete_string



my_string = "python-variable-funcion-computadora-monitor"
print(organized_string(my_string)) 