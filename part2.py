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
def idf(file_path, files_name):
    pass



def idd(lQ, files_name):                    #identification (list question)
    for i in range(len(lQ)):
        if lQ[i] not in tfidf.idf(functions.files_list(cleaned, '.txt'), files_name):
            lQ.remove(lQ[i])
    return lQ

print(idd(question_list("BOnJouR cherS, ConcitOYEnS"), functions.files_list(cleaned, '.txt')))
