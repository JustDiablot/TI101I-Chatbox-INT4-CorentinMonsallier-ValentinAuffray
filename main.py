import functions


directory = './speeches-20231109'
files_name = functions.files_list(directory, '.txt')
president_name = functions.get_names(files_name)
print(president_name)
