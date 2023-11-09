import os


def files_list(directory, ext):             ## Get the names of the files in the speach file and put them in a list
    files_name = []
    for filename in os.listdir(directory):  # For each files in the folder
        if filename.endswith(ext):          # Only if it end by '.txt'
            files_name.append(filename)     # Add the name of the file into the list files_name
    return files_name                       # Return the list


def get_names(files_name):                                                                  ## Get the name of each president from the list with the names of each file
    president_name = []
    deleted_characters = ["Nomination_", "1", "2", '.txt']                                  # List with each character that we want to delete
    for _ in range(len(files_name)):                                                        # For each position in the list of the names of the files
        president_name.append(files_name[_])                                                # Add to a new list each string
    for i in range(len(president_name)):                                                    # For each string in the new list
        for j in range(len(deleted_characters)):                                            # For each unwanted character
            president_name[i] = president_name[i].replace(deleted_characters[j], "")        # Delete the unwanted character in each string
    return set(president_name)                                                              # Retern the set