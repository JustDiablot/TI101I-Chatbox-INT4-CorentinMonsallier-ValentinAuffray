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

def tf():
    pass