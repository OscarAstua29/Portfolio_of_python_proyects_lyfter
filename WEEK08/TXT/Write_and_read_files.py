def read_file_line_by_line(songs_file, copy_file):
    list_to_order=[]
    with open (songs_file) as file:
        for line in file.readlines():
                list_to_order.append(line)
        list_to_order.sort()
        with open(copy_file, "a") as file:
           for index in list_to_order:
            file.write(index)



read_file_line_by_line("1.txt","2.txt")