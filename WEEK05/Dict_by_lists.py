list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

dictionary_of_lists ={}



for index in range (len(list_a)):
    llave_a = list_a[index]
    valor_b = list_b[index]
    dictionary_of_lists[llave_a]= valor_b



print(dictionary_of_lists)