def select_index(my_list):
   for x in range(0,len(my_list)):
    has_made_changes = False

    for i in range(len(my_list)-1,x,-1):
      current_index = my_list[i]
      previous_index = my_list[i-1]

      if current_index  < previous_index:
        my_list[i] = previous_index
        my_list[i-1] = current_index
      print(current_index, previous_index)
      print(my_list)
      has_made_changes = True

    if not has_made_changes:
      return



my_list = [5,4,30,2,10]
select_index(my_list)

print(my_list)