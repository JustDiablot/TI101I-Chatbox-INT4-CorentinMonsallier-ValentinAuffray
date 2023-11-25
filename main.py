import functions
import tfidf

speeches = './speeches-20231109'
cleaned = './cleaned'
files_name = functions.files_list(speeches, '.txt')
extract_name = functions.get_names(files_name)
president_name = functions.add_names(extract_name)
list_name = functions.delete_doubles(president_name)

functions.create_folder()
functions.create_file(files_name)
functions.copy_text(files_name)

print(tfidf.idf(cleaned))