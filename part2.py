import tfidf
import functions
import math

cleaned = './cleaned'

### 1. ###
def clean_question(question):                 #cleaned question (non cleaned)
    cleaned_question = ''
    for letter in question:
        if ord(letter)>=65 and ord(letter)<=90:                                                           # If the character is upper
            cleaned_question += chr(ord(letter)+32)                                                                  # Make it lower
        elif (ord(letter)>=21 and ord(letter)<=47) or (ord(letter)>=58 and ord(letter)<=64) :       # If the character is a punctiation character
            cleaned_question += chr(32)  
        else:
            cleaned_question += letter
    return cleaned_question
def question_list(question):                     #list question (cleaned question)
    list_clean_question = []
    for word in clean_question(question).split():
        list_clean_question.append(word)
    return list_clean_question


### 2. ###
def words_in_corpus(question, files_name):                    #identification (list question)
    list_clean_question = question_list(question)
    idf_list = tfidf.idf(cleaned, files_name)
    list = []
    for i in range(len(list_clean_question)):
        if list_clean_question[i] in idf_list:
            list.append(list_clean_question[i])
    return list


### 3. ###
def vector_question(question, files_name):
    words = words_in_corpus(question, files_name)
    idf_dict = tfidf.idf(cleaned, files_name)
    vector_dict = dict(idf_dict)
    tf = tfidf.tf_list(words)
    vector = []
    for word in vector_dict:
        if word in tf:
            vector_dict[word] = vector_dict[word] * tf[word]
        else:
            vector_dict[word] = 0
    for word in vector_dict:
        vector.append(vector_dict[word])
    return vector


### 4. ###
def scalar_product(A, B):
    val_scalar_product = 0
    for i in range(1, len(A)):
        val_scalar_product +=  A[i]*B[i]
    return val_scalar_product
def norm_vector(vector):
    summ = 0
    for i in range(1, len(vector)):
        summ += vector[i] ** 2
    return math.sqrt(summ)
def similarity(A, B):
    cos = scalar_product(A, B)/(norm_vector(A)*norm_vector(B))
    return cos


### 5. ###
def most_relevant(question, file_path, files_name):
    matrix = tfidf.tf_idf(file_path, files_name)
    index = 0
    max = 0
    for i in range(1, len(functions.files_list(file_path, '.txt'))+1):
        vecteur = []
        for elem in range(len(matrix)):
            vecteur.append(matrix[elem][i])
        cos = similarity(vecteur, vector_question(question, files_name))
        if cos > max:
            max = cos
            index = i
    return functions.files_list(file_path, '.txt')[index-1]
        
print(fromage("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?", cleaned, functions.files_list(cleaned, '.txt')))