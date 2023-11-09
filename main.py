import functions


directory = './speeches-20231109'
files_name = functions.files_list(directory, '.txt')
extract_name = functions.get_names(files_name)
president_name = functions.add_names(extract_name)
list_name = functions.delete_doubles(president_name)
print(list_name)