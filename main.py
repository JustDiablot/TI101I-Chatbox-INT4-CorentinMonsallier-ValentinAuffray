import functions
import tfidf

directory = './speeches-20231109'
files_name = functions.files_list(directory, '.txt')
extract_name = functions.get_names(files_name)
president_name = functions.add_names(extract_name)
list_name = functions.delete_doubles(president_name)

functions.create_folder()
functions.create_file(files_name)
functions.copy_text(files_name)

ss = tfidf.listing(files_name, 1)
tf = tfidf.tf(files_name, 1, ss)
idf = tfidf.idf(tf)
tf_idf = tfidf.tf_idf(tf, idf)
print(tf, "\n\n")
print(idf, "\n\n")
print(tf_idf)
