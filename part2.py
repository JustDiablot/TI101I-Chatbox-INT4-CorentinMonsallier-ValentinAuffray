import tfidf
import functions
import math

speeches = "./speeches-20231109"
cleaned = "./cleaned"

### 1. ###
def clean_question(question):                                                                                   ## Remove any punctuation, any capital letters or special characters from the question
    cleaned_question = ""
    for letter in question:
        if ord(letter)>=65 and ord(letter)<=90:
            cleaned_question += chr(ord(letter)+32)
        elif (ord(letter)>=21 and ord(letter)<=47) or (ord(letter)>=58 and ord(letter)<=64) :
            cleaned_question += chr(32)
        else:
            cleaned_question += letter
    return cleaned_question
def question_list(question):                                                                                    ## Split the question in a list of each word
    list_clean_question = []
    for word in clean_question(question).split():
        list_clean_question.append(word)
    return list_clean_question


### 2. ###
def words_in_corpus(question, files_name):                                                                      ## Identify the words that are in the question and in the corpus
    list_clean_question = question_list(question)
    idf_list = tfidf.idf(cleaned, files_name)
    list = []
    for i in range(len(list_clean_question)):
        if list_clean_question[i] in idf_list:
            list.append(list_clean_question[i])
    return list


### 3. ###
def vector_question(question, files_name):                                                                      ## Calculate the vector (tf-idf) of each word in the question
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
def vector_question_with_words(question, files_name):                                                           ## Calculate the vector (tf-idf) of each word in the question with the corresponding word (for identification)
    words = words_in_corpus(question, files_name)
    idf_dict = tfidf.idf(cleaned, files_name)
    vector_dict = dict(idf_dict)
    tf = tfidf.tf_list(words)
    final_vector = []
    for word in vector_dict:
        if word in tf:
            final_vector.append([word, vector_dict[word] * tf[word]])
    return final_vector


### 4. ###
def scalar_product(A, B):                                                                                       ## Calculate the scalar product of two vectors (one from the question, the other from the corpus)
    val_scalar_product = 0
    for i in range(1, len(A)):
        val_scalar_product +=  A[i]*B[i]
    return val_scalar_product
def norm_vector(vector):                                                                                        ## Calculate the norm of a vector (multiple vectors for the matrix)
    summ = 0
    for i in range(1, len(vector)):
        summ += vector[i] ** 2
    return math.sqrt(summ)
def similarity(A, B):                                                                                           ## Calculate the cosine similarity between two vectors
    cos = scalar_product(A, B)/(norm_vector(A)*norm_vector(B))
    return cos


### 5. ###
def most_relevant(question, file_path, files_name):                                                             ## Compute the text that is the closest to the question
    matrix = tfidf.tf_idf(file_path, files_name)
    index = 0
    max = 0
    for i in range(1, len(functions.files_list(file_path, ".txt"))+1):
        vecteur = []
        for elem in range(len(matrix)):
            vecteur.append(matrix[elem][i])
        cos = similarity(vecteur, vector_question(question, files_name))
        if cos > max:                                                                                           # Get the index of the most relevant text by the calculation of the cosine similarity
            max = cos
            index = i
    return functions.files_list(file_path, ".txt")[index-1]


### 6. ###
def answer(question, file_path, files_name):                                                                    ## Get first occurence of the most relevant word in the text, and find it's sentence
    vecteur_question = vector_question(question, files_name)
    vecteur_question_with_words = vector_question_with_words(question, functions.files_list(cleaned, ".txt"))
    max = 0
    for val in vecteur_question:                                                                                # Get highest tfidf value
        if val > max:
            max = val
    for i in vecteur_question_with_words:                                                                       # Get word with highest tfidf value
        if i[1] == max:
            mot = i[0]
            break
    file = open(f"{speeches}/{most_relevant(question, file_path, files_name)}", "r", encoding="utf8")   

    all_txt = file.read().split(".")                                                                            # Isolate punctuation
    for sentence in all_txt:
        if mot in sentence.lower().split():                                                                     # Split the sentence in a list of each word
            return sentence                                                                                     # Return the full sentence that contains the most relevant word


### 7. ###
def  result(question, answer):                                                                                  ## Return the answer with the beginning that changes depending on the question
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! "
    } 
    for i in question_starters:
        string = ""
        if question.startswith(i):                                                                              # If the question starts with the key, return the corresponding value
            answer = question_starters[i] + answer.lower()
            final_answer = list(answer)
            if "\n" in final_answer:                                                                            # Concatenate each leter and remove the newline
                final_answer.remove("\n")
            for i in final_answer:
                string += i
            return string
    final_answer = "je n'ai pas bien compris la question pouvez vous reformuler ?"                              # If the question doesn't start with the key, ask to reformulate the question
    return final_answer