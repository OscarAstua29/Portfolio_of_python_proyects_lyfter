def select_index(my_list):#O(n^2)
    for x in range(0,len(my_list)):# O(n)
      has_made_changes = False # O(1)
      for i in range(len(my_list)-1-x):# O(n^2)
          current_index = my_list[i] # O(1)
          next_index = my_list[i+1]# O(1)

          if current_index > next_index:# O(1)
            my_list[i] = next_index# O(1)
            my_list[i+1] = current_index# O(1)
            print(current_index, next_index)# O(1)
            print(my_list)# O(1)
            has_made_changes=True# O(1)


      if not has_made_changes:# O(1)
        return# O(1)




my_list = [1,7,3,10,5]# O(1)
select_index(my_list)# O(n)
print(my_list)# O(1)




#---------------------------------------------------------------------

#print_numbers_times_2

def print_numbers_times_2(numbers_list):# O(n)
	for number in numbers_list:# O(n)
		print(number * 2)# O(1)

#---------------------------------------------------------------------

#print_10_or_less_elements

def print_10_or_less_elements(list_to_print): # O(1)
	list_len = len(list_to_print)# O(1)
	for index in range(min(list_len, 10)): # O(1)
	    print(list_to_print[index]) # O(1)


#---------------------------------------------------------------------

#generate_list_trios

def generate_list_trios(list_a, list_b, list_c):# O(n^2)
	result_list = [] # O(1)
	for element_a in list_a:# O(n)
		for element_b in list_b:# O(n^2)
			for element_c in list_c:# O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')# O(1)
				
	return result_list # O(1)