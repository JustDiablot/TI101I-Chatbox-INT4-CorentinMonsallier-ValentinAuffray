import tfidf
import functions

cleaned = './cleaned'

### 1. ###
def clean_question(nc):                 #cleaned question (non cleaned)
    cQ = ''
    for letter in nc:
        if ord(letter)>=65 and ord(letter)<=90:                                                           # If the character is upper
            cQ += chr(ord(letter)+32)                                                                  # Make it lower
        elif (ord(letter)>=21 and ord(letter)<=47) or (ord(letter)>=58 and ord(letter)<=64) :       # If the character is a punctiation character
            cQ += chr(32)  
        else:
            cQ += letter
    return cQ

def question_list(nc):                     #list question (cleaned question)
    l = []
    for word in clean_question(nc).split():
        l.append(word)
    return l


### 2. ###
def idd(lQ, files_name):                    #identification (list question)
    list = []
    print
    for i in range(len(lQ)):
        if lQ[i] in tfidf.idf(cleaned, files_name):
            list.append(lQ[i])
    return list


### 3. ###
def vector(list, files_name):
    words = list
    tf = tfidf.tf_list(words)
    matrix = tfidf.tf_idf(cleaned, files_name)
    for word in matrix:                                                                     # Si mot pas dans question
        if word[0] not in tf:
            for i in range(1, len(word)):
                word[i] = 0
    vector = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]    # Transpose the matrix
    return vector


### 4. ###





#print(idd(question_list("BOnjOUR,  , mes Chers amis et cobncit concitoyens citoyens"), functions.files_list(cleaned, '.txt'))) ### Identification des mots dans tf_idf
print(vector(idd(question_list("BOnjOUR,  , mes Chers amis et cobncit concitoyens citoyens"), functions.files_list(cleaned, '.txt')), functions.files_list(cleaned, '.txt')))
#idd(question_list("BOnjOUR,  , mes Chers amis et cobncit concitoyens citoyens"), functions.files_list(cleaned, '.txt')))