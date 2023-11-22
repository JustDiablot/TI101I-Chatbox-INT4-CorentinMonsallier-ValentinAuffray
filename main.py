import functions
import tfidf

tf = {'mo1': 7, 'mo2': 2, 'mo3': 1, 'mo4': 3, 'mo5': 6, 'mo6': 4, 'mo7': 9, 'mo8': 5, 'mo9': 0.1 }

directory = './speeches-20231109'
files_name = functions.files_list(directory, '.txt')
extract_name = functions.get_names(files_name)
president_name = functions.add_names(extract_name)
list_name = functions.delete_doubles(president_name)
print(list_name)

functions.create_folder()
functions.create_file(files_name)
functions.copy_text(files_name)

ss = tfidf.listing(files_name, 1)
tf = tfidf.tf(files_name, 1, ss)
idf = tfidf.idf(tf)