import functions
import tfidf

speeches = './speeches-20231109'
cleaned = './cleaned'
files_name = functions.files_list(speeches, '.txt')
extract_name = functions.get_names(files_name)
president_name = functions.add_names(extract_name)
list_name = functions.delete_doubles(president_name)

'''functions.create_folder()
functions.create_file(files_name)
functions.copy_text(files_name)'''


matrix = tfidf.tf_idf(cleaned, files_name)

# display the matrix in the console with the format of a table
for i in range(len(matrix)): #for each row in the matrix:
    for j in range(9): #for each column in the row
        print(matrix[i][j], end='\t')
    print('/n')





## Transposée d'une matrice
    #A = [ [3, 1, 5], [9, 8, -1], [10, 12, 2] ]
    #B = [ [8, -1, 8], [2, 1, 3], [18, 2, 32] ]
 
    #n=len(A) # nombre de lignes
    #m=len(A[0]) # nombre de colonnes
 
    #C = [[A[j][i] for j in range(n)] for i in range(m)]
 
    #print("A : ", A)
    #print("Transposée de A : ", C)