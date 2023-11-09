import functions


directory = './speeches-20231109'
files_name = functions.files_list(directory, '.txt')
print(files_name)
