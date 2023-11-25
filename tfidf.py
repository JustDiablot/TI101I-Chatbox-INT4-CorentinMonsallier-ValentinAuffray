import math
import os

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


def idf(file_path):                                                                                                      ## Get the importance of each term
    idf = {}
    for file in os.listdir(file_path):
        for key in tf(f'{file_path}/{file}').keys():
            if key not in idf:
                idf[key] = 1
            else:
                idf[key] += 1                                                                                           # Add to the value of the the count
    for key in idf.keys():                                                                                              # For each word of the list
        idf[key] = math.log(8 / idf[key])                                                                               # Compute the logarithm of the inverse of the proportion of documents in the corpus that contain that word
    return(idf)                                                                                                         # Return the tdf dictionnary


def tf_idf(directory):
    pass