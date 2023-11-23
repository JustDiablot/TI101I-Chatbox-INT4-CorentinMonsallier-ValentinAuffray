import math


def listing(files_name, i):
    l = []
    l1 = []
    f = open(f'./speeches-20231109/{files_name[i]}', 'r',encoding='utf8')
    lines = f.readlines()
    for line in lines:  
        l = line.split()
        for i in l:
            l1.append(i)
    return set(l1)

"""def tf(files_name, i,  listing):
    tf = {}
    with open(f'./speeches-20231109/{files_name[i]}', 'r',encoding='utf8') as f:
        for word in listing:
            tf[word] = 0
        for lines in f.readlines():
            for line in lines:
                for word in line:
                    tf[word] += 1
        return tf
"""
def idf(tf):
    idf = dict(tf)
    for key in idf.keys():
        val = idf[key]
        idf[key] = math.log(1 / val, 10)
    return idf
