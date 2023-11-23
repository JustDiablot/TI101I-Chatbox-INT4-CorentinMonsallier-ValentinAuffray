import math


def listing(files_name, i):
    l = []
    l1 = []
    f = open(f'./cleaned/{files_name[i]}', 'r',encoding='utf8')
    lines = f.readlines()
    for line in lines:  
        l = line.split()
        for i in l:
            l1.append(i)
    return l1

def tf(files_name, i,  listing):
    tf = {}
    print(files_name[i])
    with open(f'./cleaned/{files_name[i]}', 'r',encoding='utf8') as f:
    
        for word in set(listing):
            tf[word] = 0
        for word in listing:
            tf[word] += 1
        return tf

def idf(tf):
    idf = dict(tf)
    for key in idf.keys():
        idf[key] = 1 / math.log(idf[key], 10)
    return idf

def tf_idf(tf, idf):
    tf_idf = dict(tf)
    for key in tf_idf.keys():
        tf_idf[key] = tf[key] * idf[key]
    return tf_idf