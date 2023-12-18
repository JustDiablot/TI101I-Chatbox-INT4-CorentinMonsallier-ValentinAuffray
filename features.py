import tfidf
import functions

speeches = './speeches-20231109'
cleaned = './cleaned'

### 1. ###
def unimportant(files_name):                                            ## Create a list where we can see all of the words that are considered unimportant
    unimportant = []
    matrix = tfidf.tf_idf(cleaned, files_name)
    for i in range(len(matrix)):
        val = 0
        for j in range(1, 9):
            val += matrix[i][j]
        if val == 0:
            unimportant.append(matrix[i][0])
    return unimportant
    

### 2. ###
def important(files_name):                                              ## Create a list where we can see all of the words that are considered the most important
    important = []
    matrix = tfidf.tf_idf(cleaned, files_name)
    temp = 0
    for i in range(len(matrix)):
        val = 0
        for j in range(1, 9):
            val += matrix[i][j]
        if val >= temp:
            temp = val
    for i in range(len(matrix)):
        val = 0
        for j in range(1, 9):
            val += matrix[i][j]
        if val == temp:
            important.append(matrix[i][0])
    return important


### 3. ###
def most_repeat(files_name, pres_name):                                 ## Get the most repeated word by a president
    word = []
    val = []
    dico = {}
    tempo = 0
    files_names = functions.get_names(files_name)
    for name in range(len(files_names)):
        if pres_name == files_names[name] :
            temp = tfidf.tf(f'{cleaned}/{files_name[name]}')
            val.append(temp)
    for dict in val:                                                    # Create a dictionnary with each word of the tf
        for key in dict:
            dico[key] = 0
    for dict in val:                                                    # Add a occurence for each word that appears in the tf
        for key in dict:
            dico[key] += dict[key]
    for key in dico:                                                    # Get the most repeated word in the dictionnary
        if dico[key] >= tempo:
            tempo = dico[key]
    for key in dico:
        if dico[key] == tempo:                                          # Add the word to the list of the most repeated words
            word.append(key)
    return word


### 4. ###
def global_research(files_name, word):                                  ## Get the name of the president who talked the most about a certain word 
    temp = []
    for file in files_name:
        tf_dict = tfidf.tf(f'{cleaned}/{file}')
        if word.lower() in tf_dict:
            temp.append(file)
    name = set(functions.add_names(functions.get_names(temp)))
    return name
def unique_research(files_name, word):                                  ## Get the name of the all of presidents who talked about a certain word 
    val = 0
    name = []
    for file in files_name:
        tf_dict = tfidf.tf(f'{cleaned}/{file}')
        if word.lower() in tf_dict:
            if tf_dict[word.lower()] > val:
                val = tf_dict[word.lower()]
                name = [file]
            elif tf_dict[word.lower()] == val:
                name.append(file)
    name = set(functions.add_names(functions.get_names(name)))
    return name


### 5. ###
def multiple_research(x, y, files_name):                                ## Look for which speech has both words
    fx = list(global_research(files_name, x))
    fy = list(global_research(files_name, y))
    for i in fx:
        if i in fy :
            return i
    return


### 6. ###
def all_in(files_name, pres_names):                                     ## Get the words that all of the presidents said, aside the unimportant words
    unimportant_word = unimportant(files_name)
    words = []
    dict = tfidf.idf(cleaned, files_name)
    for elem in dict:                                                   # For each word
        count = 0
        for name in set(pres_names):
            text = ''
            for i in files_name:
                if name in i:                                           # If the name of the president is in multiple files, make the one variable
                    file = open(f'{cleaned}/{i}', 'r', encoding='utf8')
                    text += file.read() + ''
            tf_of_text = tfidf.tf_text(text)
            if elem in tf_of_text:                                      # If the word is in one's president variable, increase the counter
                count += 1
        if count == 6 and elem not in unimportant_word:
            words.append(elem)
    return words