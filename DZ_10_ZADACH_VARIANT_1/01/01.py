def spiral_matrix(n,m,reverse=False):
    matrix=[[0]*m for i in range(n)]
    top=0
    bottom=n-1
    left=0
    right=m-1
    if reverse:
        number=n*m
        step=-1
    else:
        number=1
        step=1
    while top<=bottom and left<=right:
        for j in range(left,right+1):
            matrix[top][j]=number
            number+=step
        top+=1
        for i in range(top,bottom+1):
            matrix[i][right]=number
            number+=step
        right-=1
        if top<=bottom:
            for j in range(right,left-1,-1):
                matrix[bottom][j]=number
                number+=step
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=number
                number+=step
            left+=1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

print("3 x 3:")
print_matrix(spiral_matrix(3,3))

print("3 x 5:")
print_matrix(spiral_matrix(3,5))

print("4 x 2:")
print_matrix(spiral_matrix(4,2))

print("Обратная спираль 3 x 3:")
print_matrix(spiral_matrix(3,3,True))
