def file_reader():
    splitted_data=[]
    f = open("./data_source_files/moves.txt", "r")
    data=f.read()
    data_into_list = data.split("\n")
    f.close()
    for data in  data_into_list[1:-1]:
        splitted_data.append(data.split(':'))
    return splitted_data
    
    
#print(file_reader())