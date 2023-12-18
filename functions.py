import os


def files_list(directory, ext):                                                                                         ## Get the names of the files in the speach file and put them in a list
    files_name = []
    for filename in os.listdir(directory):
        if filename.endswith(ext):
            files_name.append(filename)
    return files_name

def get_names(files_name):                                                                                              ## Get the name of each president from the list with the names of each file
    extract_name = []
    deleted_characters = ['Nomination_', '1', '2', '.txt']
    for i in range(len(files_name)):
        extract_name.append(files_name[i])
    for i in range(len(extract_name)):
        for j in range(len(deleted_characters)):
            extract_name[i] = extract_name[i].replace(deleted_characters[j], '')
    return extract_name


def add_names(extract_name):                                                                                            ## Combine the first name and the last name of each president
    president_name = []
    first_names = {'Chirac' : 'Jacques',
                   'Giscard dEstaing' : 'Valéry',
                   'Hollande' : 'François',
                   'Macron' : 'Emmanuel',
                   'Mitterrand' : 'François',
                   'Sarkozy' : 'Nicolas'}
    for i in range(len(extract_name)):
        string = first_names[extract_name[i]] + ' ' + extract_name[i]
        president_name.append(string)
    return president_name


def delete_doubles(president_name):                                                                                     ## Delete one name of president if there is a double --> with a set
    list_name = set(president_name)
    return list_name


def create_folder():                                                                                                    ## Create a new folder for the 'cleaned' files
    newpath = './cleaned' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def create_file(files_name):                                                                                            ## Create the 'cleaned' files in the cleaned folder
    for i in range(len(files_name)):
        create_new_file = open(f'./cleaned/{files_name[i]}', 'w',encoding='utf8')
        create_new_file.close()


def copy_text(files_name):                                                                                              ## Copies the text on each file from the speech folder to the cleaned folder witout any punctuation or special characters or capital letters
    for i in range(len(files_name)):
        original_file = open(f'./speeches-20231109/{files_name[i]}', 'r',encoding='utf8')
        new_file = open(f'./cleaned/{files_name[i]}', 'w',encoding='utf8')
        lines = original_file.readlines()
        for line in lines:
            for character in line:
                if ord(character)>=65 and ord(character)<=90:
                    character = chr(ord(character)+32)
                elif (ord(character)>=21 and ord(character)<=47) or (ord(character)>=58 and ord(character)<=64) :
                    character = chr(32)
                new_file.write(character)
        original_file.close()
        new_file.close()