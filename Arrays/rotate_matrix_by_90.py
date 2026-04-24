def rotate_matrix_by_90_degree(matrix):
    m=len(matrix)
    n=len(matrix[0])
    
    for row in range(m):
        for col in range(row +1 ,m):
            matrix[row][col], matrix[col][row]= matrix[col][row], matrix[row][col]
           
    # reversing the row        
    for i in range(m):
        # Reversing the current row to simulate the clockwise rotation
        matrix[i].reverse()
            
    return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("before rotation: ")

for i in range(len(matrix)):
    print(matrix[i])
    
result=rotate_matrix_by_90_degree(matrix)

print("After rotation")
for j in range(len(result)):
    print(matrix[j])