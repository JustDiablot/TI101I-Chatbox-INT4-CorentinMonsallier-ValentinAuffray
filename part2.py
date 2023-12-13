import tfidf
import functions

cleaned = './cleaned'
def cleanQ(nc):                 #cleaned question (non cleaned)
    cQ = []
    for letter in nc:
        if ord(letter)>=65 and ord(letter)<=90:                                                           # If the character is upper
            letter = chr(ord(letter)+32)                                                                  # Make it lower
        elif (ord(letter)>=21 and ord(letter)<=47) or (ord(letter)>=58 and ord(letter)<=64) :       # If the character is a punctiation character
            letter = chr(32)                                                                                 # Make this character a space
        cQ.append(letter)
    return cQ

def lQ(nc):                     #list question (cleaned question)
    l = []
    for word in cleanQ(nc).split():
        l.append(word)
    return set(l)

def idd(lQ):                    #identification (list question)
    for i in len(lQ):
        if lQ[i] not in tfidf.idf(functions.files_list(cleaned, '.txt')):
            lQ.remove(lQ[i])