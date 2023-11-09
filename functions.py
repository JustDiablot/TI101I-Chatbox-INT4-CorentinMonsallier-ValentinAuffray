import os


def files_list(directory, ext):
    files_name = []
    for filename in os.listdir(directory):  #for each files in the folder
        if filename.endswith(ext):          #only if it end by '.txt'
            files_name.append(filename)     #add the name of the file into the list files_name
    return files_name                       #return the list

