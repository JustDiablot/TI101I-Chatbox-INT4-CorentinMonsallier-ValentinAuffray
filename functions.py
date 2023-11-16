import os


def files_list(directory, ext):                                                             ## Get the names of the files in the speach file and put them in a list
    files_name = []
    for filename in os.listdir(directory):                                                  # For each files in the folder
        if filename.endswith(ext):                                                          # Only if it end by '.txt'
            files_name.append(filename)                                                     # Add the name of the file into the list files_name
    return files_name                                                                       # Return the list


def get_names(files_name):                                                                  ## Get the name of each president from the list with the names of each file
    extract_name = []
    deleted_characters = ["Nomination_", "1", "2", '.txt']                                  # List with each character that we want to delete
    for _ in range(len(files_name)):                                                        # For each position in the list of the names of the files
        extract_name.append(files_name[_])                                                  # Add to a new list each string
    for i in range(len(extract_name)):                                                      # For each string in the new list
        for j in range(len(deleted_characters)):                                            # For each unwanted character
            extract_name[i] = extract_name[i].replace(deleted_characters[j], "")            # Delete the unwanted character in each string
    return extract_name                                                                     # Return the list


def add_names(extract_name):                                                                ## Combine the first name and the last name
    president_name = []
    first_names = {'Chirac' : 'Jacques',
                   'Giscard dEstaing' : 'Valéry',
                   'Hollande' : 'François',
                   'Macron' : 'Emmanuel',
                   'Mitterrand' : 'François',
                   'Sarkozy' : 'Nicolas'}
    for i in range(len(extract_name)):                                                      # For each position of the liste with the family name
        string = first_names[extract_name[i]] + ' ' + extract_name[i]                       # Make a string by adding the first name and the last name 
        president_name.append(string)                                                       # Adding these new full names to a new list
    return president_name                                                                   # Return the list


def delete_doubles(president_name):                                                         ## Delete the doubles
    list_name = set(president_name)                                                         # Convert the list to a set to delete the doubles
    return list_name                                                                        # Return the set


def create_folder():
    newpath = './cleaned' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def create_file(files_name):
    for i in range(len(files_name)):
        create_new_file = open(f'./cleaned/{files_name[i]}', 'w')
        create_new_file.close()


def copy_text(files_name):
    for i in range(len(files_name)):
        original_file = open(f'./speeches-20231109/{files_name[i]}', 'r')
        new_file = open(f'./cleaned/{files_name[i]}', 'w')
        lines = original_file.readlines()
        for line in lines:
            for character in line:
                if ord(character)>=65 and ord(character)<=90:
                    character = chr(ord(character)+32)
                print(character)
#               new_file.write(character)

  
        original_file.close()
        new_file.close()