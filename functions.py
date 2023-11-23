import os


def files_list(directory, ext):                                                                                         ## Get the names of the files in the speach file and put them in a list
    files_name = []
    for filename in os.listdir(directory):                                                                              # For each files in the folder
        if filename.endswith(ext):                                                                                      # Only if it end by '.txt'
            files_name.append(filename)                                                                                 # Add the name of the file into the list files_name
    return files_name                                                                                                   # Return the list


def get_names(files_name):                                                                                              ## Get the name of each president from the list with the names of each file
    extract_name = []
    deleted_characters = ["Nomination_", "1", "2", '.txt']                                                              # List with each character that we want to delete
    for _ in range(len(files_name)):                                                                                    # For each position in the list of the names of the files
        extract_name.append(files_name[_])                                                                              # Add to a new list each string
    for i in range(len(extract_name)):                                                                                  # For each string in the new list
        for j in range(len(deleted_characters)):                                                                        # For each unwanted character
            extract_name[i] = extract_name[i].replace(deleted_characters[j], "")                                        # Delete the unwanted character in each string
    return extract_name                                                                                                 # Return the list


def add_names(extract_name):                                                                                            ## Combine the first name and the last name
    president_name = []
    first_names = {'Chirac' : 'Jacques',
                   'Giscard dEstaing' : 'Valéry',
                   'Hollande' : 'François',
                   'Macron' : 'Emmanuel',
                   'Mitterrand' : 'François',
                   'Sarkozy' : 'Nicolas'}
    for i in range(len(extract_name)):                                                                                  # For each position of the liste with the family name
        string = first_names[extract_name[i]] + ' ' + extract_name[i]                                                   # Make a string by adding the first name and the last name 
        president_name.append(string)                                                                                   # Adding these new full names to a new list
    return president_name                                                                                               # Return the list


def delete_doubles(president_name):                                                                                     ## Delete the doubles
    list_name = set(president_name)                                                                                     # Convert the list to a set to delete the doubles
    return list_name                                                                                                    # Return the set


def create_folder():                                                                                                    ## Create a new folder for the "cleaned" files
    newpath = './cleaned' 
    if not os.path.exists(newpath):                                                                                     # If the folder does not exist
        os.makedirs(newpath)                                                                                            # Create the folder


def create_file(files_name):                                                                                            ## Create the "cleaned" files in the cleaned folder
    for i in range(len(files_name)):                                                                                    # For each file in the original path
        create_new_file = open(f'./cleaned/{files_name[i]}', 'w',encoding='utf8')                                                       # Create a new file in the cleaned folder
        create_new_file.close()                                                                                         # Close the created file


def copy_text(files_name):                                                                                              ## Clean the duplicated files
    for i in range(len(files_name)):                                                                                    # For each file
        original_file = open(f'./speeches-20231109/{files_name[i]}', 'r',encoding='utf8')                                               # Open the original file
        new_file = open(f'./cleaned/{files_name[i]}', 'w',encoding='utf8')                                                              # Open the new file
        lines = original_file.readlines()                                                                               # Read all lines in a file
        for line in lines:                                                                                              # For each line of this file
            for character in line:                                                                                      # For each character of each line of each file
                if ord(character)>=65 and ord(character)<=90:                                                           # If the character is upper
                    character = chr(ord(character)+32)                                                                  # Make it lower
                elif (ord(character)>=21 and ord(character)<=47) or (ord(character)>=58 and ord(character)<=64) :       # If the character is a punctiation character
                    character = chr(32)                                                                                 # Make this character a space
                new_file.write(character)                                                                               # Write the new file with the modified characters
        original_file.close()                                                                                           # Close the original file
        new_file.close()                                                                                                # Close the new file