import os


def files_list(directory, ext):
    files_name = []
    for filename in os.listdir(directory):  #for each files in the folder
        if filename.endswith(ext):          #only if it end by '.txt'
            files_name.append(filename)     #add the name of the file into the list files_name
    return files_name                       #return the list

def get_names(files_name):
    president_name = []
    deleted_characters = ["Nomination_", "1", "2", '.txt']
    for _ in range(len(files_name)):
        president_name.append(files_name[_])
    for i in range(len(president_name)):
        for j in range(len(deleted_characters)):
            president_name[i] = president_name[i].replace(deleted_characters[j], "")
    return set(president_name)