from time import perf_counter

def set_matrix_zero(matrix):
    row_length=len(matrix)
    col_length=len(matrix[0])
    
    # Row wise traversal
    for row in range(row_length):
        for column in range(col_length):
            
            # if the current cell is zero
            if matrix[row][column]==0:
                
                # mark all elements of the row as zero
                for i in range(row_length):
                    if matrix[i][column]!=0:
                        matrix[i][column]=-1
                        
                # mark all the elements of the column
                for j in range(col_length):
                     if matrix[row][j]!=0:
                        matrix[row][j]=-1
                        
    for row in range(row_length):
        for column in range(col_length):
            if matrix[row][column]==-1:
                matrix[row][column]=0
    
    return matrix

# Before Conversion
print("Before Conversion")
matrix=[[1,1,1],[1,0,1],[1,1,1]]
for i in range(len(matrix)):
    print(matrix[i])

result=set_matrix_zero(matrix)

# After conversion
print("After Converstion")
for i in range(len(matrix)):
    print(matrix[i])