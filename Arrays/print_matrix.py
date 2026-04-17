def print_matrix(matrix):
    n=len(matrix)
    print(n)
    
    # print(matrix[0][0])
    
    for i in range(n):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
            
            if j==len(matrix[i])-1:
                for k in range(i+1, n):
                    print(matrix[k][j], end=" ")

                if k==n-1:
                    
        break

matrix=[[1,2,3], [4,5,6], [7,8,9]]
result=print_matrix(matrix)
print(result)
