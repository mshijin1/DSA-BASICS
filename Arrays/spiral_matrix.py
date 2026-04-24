def spiral_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    res=[]
    top=0
    bottom=n-1
    left=0
    right=m-1
    
    # Iterating until the elemnets are printed
    while top<=bottom and left<=right:
        # Printing top row from left to right
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top+=1
        
        # printing right column from top to bottom
        for j in range(top, bottom+1):
            res.append(matrix[j][right])
        right-=1
        
        # printing bottom from right to left
        if top<=bottom:
            for k in range(right, left-1, -1):
                res.append(matrix[bottom][k]) 
            bottom-=1
            
        # printing the left column from bottom to top
        if left<=right:
            for l in range(bottom, top-1, -1):
                res.append(matrix[l][left])
            left+=1
            
    return res      
             

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i])
    
result=spiral_matrix(matrix)
print("Spiral matrix: ", result)
print(" ".join(map(str,result)))