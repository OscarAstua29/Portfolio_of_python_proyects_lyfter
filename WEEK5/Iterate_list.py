"""index_de_acomodo = 1
index_impresion_de_primer_valor= 0
index_impresion_de_segundo_valor= 1
for index in range(0, len(second_list)):
	data_second_list = second_list[index]
	first_list.insert( index_de_acomodo, data_second_list)
	index_de_acomodo = index_de_acomodo + 2
	print (first_list[index_impresion_de_primer_valor], first_list[index_impresion_de_segundo_valor])
	index_impresion_de_primer_valor = index_impresion_de_primer_valor + 2
	index_impresion_de_segundo_valor = index_impresion_de_segundo_valor + 2
	"""


first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]


for index in range(len(second_list)):
	print(first_list[index] + " " + second_list[index])