def select_index(my_list):
    for x in range(0,len(my_list)):
      has_made_changes=False
      for i in range(len(my_list)-1-x):
          current_index = my_list[i]
          next_index = my_list[i+1]

          if current_index > next_index:
            my_list[i] = next_index
            my_list[i+1] = current_index
            print(current_index, next_index)
            print(my_list)
            has_made_changes=True

      if not has_made_changes:
        return



my_list = [1,7,3,10,5]
select_index(my_list)

print(my_list)