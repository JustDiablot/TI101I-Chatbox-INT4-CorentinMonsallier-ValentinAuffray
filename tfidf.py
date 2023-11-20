import math


tf = {'mo1': 7, 'mo2': 2, 'mo3': 1, 'mo4': 3, 'mo5': 6, 'mo6': 4, 'mo7': 9, 'mo8': 5, 'mo9': 8 }

def listing(files_name, i):
    l = []
    l1 = []
    f = open(f'./speeches-20231109/{files_name[i]}', 'r')
    lines = f.readlines()
    for line in lines:  
        l = line.split()
        for i in l:
            l1.append(i)
    return set(l1)

def tf(files_name, i,  listing):
    tf = {}
    with open(f'./speeches-20231109/{files_name[i]}', 'r') as f:
        for word in listing:
            tf[word] = 0
        for word in listing:
            [word] += 1
        return tf

def idf(tf):
    idf = dict(tf)
    for i in range(len(idf)):
        tuple = idf.items()
        print(tuple[i[1]])
        '''idf[i] = math.log(1 / idf.key()[i])'''
    return idf
print(idf(tf))