import tfidf
import functions

speeches = './speeches-20231109'
cleaned = './cleaned'


# Feature exercise 1
def unimportant(files_name):                                                                                            ## Get the unimportant terms
    unimportant = []
    matrix = tfidf.tf_idf(cleaned, files_name)                                                                          # Get the matrix with the tf-idf vectors
    for i in range(len(matrix)):                                                                                        # For each line
        val = 0                                                                                                         # Initialize the sum to 0
        for j in range(1, 9):                                                                                           # For each value of eaxh key
            val += matrix[i][j]                                                                                         # Add the values of the tf-idf vectors to get the sum
        if val == 0:                                                                                                    # If the sum is 0
            unimportant.append(matrix[i][0])                                                                            # Add the term to the unimportant list
    return unimportant                                                                                                  # Return the unimportant list
    

# Feature exercise 2
def important(files_name):                                                                                              ## Get the important terms of each document
    important = []
    matrix = tfidf.tf_idf(cleaned, files_name)                                                                          # Get the matrix with the tf-idf vectors
    temp = 0                                                                                                            # Initialize the temporary value to 0
    for i in range(len(matrix)):                                                                                        # For each line of the matrix
        val = 0                                                                                                         # Initialize the sum to 0
        for j in range(1, 9):                                                                                           # For each value
            val += matrix[i][j]                                                                                         # Add the values of the tf-idf vectors to get the sum
        if val >= temp:                                                                                                 # If the sum is greater than the temporary value
            temp = val                                                                                                  # Set the temporary value to the sum
    for i in range(len(matrix)):                                                                                        # For each line of the matrix
        val = 0                                                                                                         # Initialize the sum to 0
        for j in range(1, 9):                                                                                           # For each value 
            val += matrix[i][j]                                                                                         # Add the values of the tf-idf vectors to get the sum
        if val == temp:                                                                                                 # If the sum is equal to the temporary value
            important.append(matrix[i][0])                                                                              # Add the term to the important list
    return important                                                                                                    # Return the important list


# Feature exercise 3
def most_repeat(files_name, pres_name):                                                                                 ## Get the most repeated word
    word = []                                                                                                           # Initialize the word list
    val = []                                                                                                            # Initialize the val list
    dico = {}                                                                                                           # Initialize the dico dictionnary
    tempo = 0                                                                                                           # Initialize the temporary value to 0
    files_names = functions.get_names(files_name)                                                                       # Get the names of the files
    for name in range(len(files_names)):                                                                                # For each name
        if pres_name == files_names[name] :                                                                             # If the name is the same as the president name
            temp = tfidf.tf(f'{cleaned}/{files_name[name]}')                                                            # Get the tf dictionnary for the selected file
            val.append(temp)                                                                                            # Add the tf dictionnary to the val list
    for dict in val:                                                                                                    # For each dictionnary in val
        for key in dict:                                                                                                # For each key in the dictionnary
            dico[key] = 0                                                                                               # Set the value of the key to 0
    for dict in val:                                                                                                    # For each dictionnary in val
        for key in dict:                                                                                                # For each key in the dictionnary 
            dico[key] += dict[key]                                                                                      # Add the value of the key to the value of the key in dico
    for key in dico:                                                                                                    # For each key in dico
        if dico[key] >= tempo:                                                                                          # If the value of the key is greater than the temporary value
            tempo = dico[key]                                                                                           # Set the temporary value to the value of the key
    for key in dico:                                                                                                    # For each key in dico
        if dico[key]==tempo:                                                                                            # If the value of the key is equal to the temporary value
            word.append(key)                                                                                            # Add the key to the word list
    return word                                                                                                         # Return the word list


# Feature exercise 4
def global_research(files_name, word):                                                                                  ## Get the global research
    temp = []                                                                                                           # Initialize the temporary list
    for file in files_name:                                                                                             # For each file
        tf_dict = tfidf.tf(f'{cleaned}/{file}')                                                                         # Get the tf dictionnary for the selected file
        if word.lower() in tf_dict:                                                                                     # If the word is in the tf dictionnary of the selected file
            temp.append(file)                                                                                           # Add the file to the temporary list
    name = set(functions.add_names(functions.get_names(temp)))                                                          # Add the names of the files
    return name                                                                                                         # Return the name set
def unique_research(files_name, word):                                                                                  ## Get the unique research
    val = 0                                                                                                             # Initialize the temporary value to 0
    name = []                                                                                                           # Initialize the name list
    for file in files_name:                                                                                             # For each file
        tf_dict = tfidf.tf(f'{cleaned}/{file}')                                                                         # Get the tf dictionnary for the selected file
        if word.lower() in tf_dict:                                                                                     # If the word is in the tf dictionnary of the selected file
            if tf_dict[word.lower()] > val:                                                                             # If the value of the word is greater than the temporary value
                val = tf_dict[word.lower()]                                                                             # Set the temporary value to the value of the word
                name = [file]                                                                                           # Add the file to the name list
            elif tf_dict[word.lower()] == val:                                                                          # If the value of the word is equal to the temporary value
                name.append(file)                                                                                       # Add the file to the name list
    name = set(functions.add_names(functions.get_names(name)))                                                          # Add the names of the files
    return name                                                                                                         # Return the name set


# Feature exercise 5
def multiple_research(x, y, files_name):                                                                                ## Get the multiple research
    fx = list(global_research(files_name, x))                                                                           # Get the global research of the first word
    fy = list(global_research(files_name, y))                                                                           # Get the global research of the second word
    for i in fx:                                                                                                        # For each file in the global research of the first word
        if i in fy :                                                                                                    # If the file is in the global research of the second word
            return i                                                                                                    # Return the file
    return                                                                                                              # Else return nothing


# Feature exercise 6
def all_in(files_name, pres_names):
    unimportant_word = unimportant(files_name)
    words = []
    dict = tfidf.idf(cleaned, files_name)
    for elem in dict:
        print('hihihiha')
        count = 0
        for name in set(pres_names):
            print('_______')
            text = ''
            for i in files_name:
                if name in i:
                    file = open(f'{cleaned}/{i}', 'r', encoding='utf8')
                    text += file.read() + ''
            fromage = tfidf.tf_text(text)
            if elem in fromage:
                count += 1
        if count == 6 and elem not in unimportant_word:
            words.append(elem)
    return words


'''for name in range(len(pres_names)):
    text = ''
    print(name)
    for i in range(len(files_name)):
        if list(pres_names)[name] in files_name[i]:
            file = open(f'{cleaned}/{files_name[i]}', 'r', encoding='utf8')
            text += file.read() + ' '
    fromage = tfidf.tf_text(text)
    print(fromage)
    if word[0] in fromage:
        count += 1
if count == 6 and word not in unimportant(files_name):
    words.append(word)
return words'''