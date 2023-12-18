import math
import functions #


def tf(file_path):                                                                                                      ## Look for the frequency of each word in a text
    file = open(file_path, 'r', encoding='utf-8')                                                                       # Opens a speech
    tf = {}
    list = []
    lines = file.readlines()                                                                                            # Read all lines in a file
    for line in lines:                                                                                                  # For each line of this file
        for i in line.split():                                                                                          # For each word of each line
            list.append(i)                                                                                              # Add it to a list
    for word in list:                                                                                                   # For each word of the list
        if word not in tf:                                                                                              # If the word is not in the tf dictionnary
            tf[word] = 1                                                                                                # Add it with a value of 1
        else:                                                                                                           # If the word is already in the dictionnary
            tf[word] += 1                                                                                               # Add to the value of the count 1
    return tf                                                                                                           # Return the tf dictionary

def tf_text(text):
    tf = {}
    list = []                                                                                               # For each line of this file
    for i in text.split():                                                                                          # For each word of each line
        list.append(i)                                                                                              # Add it to a list
    for word in list:                                                                                                   # For each word of the list
        if word not in tf:                                                                                              # If the word is not in the tf dictionnary
            tf[word] = 1                                                                                                # Add it with a value of 1
        else:                                                                                                           # If the word is already in the dictionnary
            tf[word] += 1                                                                                               # Add to the value of the count 1
    return tf                                                                                                           # Return the tf dictionary


def tf_list(list):
    tf = {}
    for word in list:
        if word not in tf:
            tf[word] = 1
        else:
            tf[word] += 1
    return tf


def idf(file_path, files_name):                                                                                         ## Get the importance of each term
    idf = {}                                                                                                 # If the list is empty
    for file in files_name:                                                                                             # For each file of the cleaned folder
        for key in tf(f'{file_path}/{file}').keys():                                                                    # For each key of the tf function of each file)
            if key not in idf:                                                                                          # If the key is not in the idf dictionary
                idf[key] = 1                                                                                            # Put the count to one
            else:                                                                                                       # If the key is already in the dictionnary
                idf[key] += 1                                                                                           # Add to the value of the the count 1
    for key in idf.keys():                                                                                              # For each word of the list
        idf[key] = math.log(len(files_name) / idf[key])                                                                 # Compute the logarithm of the inverse of the proportion of documents in the corpus that contain that word
    return idf     


def tf_idf(file_path, files_name):                                                                                      ## Create a matrix with the tf-idf vectors
    tf_idf = []
    idf_dict = idf(file_path, files_name)                                                                               # Get the idf dictionnary
    for key in idf_dict:                                                                                                # For each key
        temp = []
        temp.append(key)                                                                                                # Add the key to the list of the list
        for file in files_name:                                                                                         # For each file
            tf_dict = tf(f'{file_path}/{file}')                                                                         # Get the tf dictionnary for the selected file
            if key in tf_dict.keys():                                                                                   # If the idf key is in the tf dictionnary of the selected file
                val = idf_dict[key] * tf_dict[key]                                                                      # Compute the tf-idf vector
            elif key not in tf_dict.keys():                                                                             # If the idf key is not in the tf dictionnary of the selected file
                val = 0                                                                                                 # Set the tf-idf vector to 0
            temp.append(round(val, 2))                                                                                  # Add the tf-idf vector to the temporary list with a rounded vector
        tf_idf.append(temp)                                                                                             # Add the temporary list to the matrix
    return tf_idf