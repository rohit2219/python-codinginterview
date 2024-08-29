
def maxCost(matrix,row,col):
    print('inside fn',row,col)
    if row < 0 or col < 0:
        return -99999
    if row==0 and col ==0:
        return matrix[row][col]
    else:
        return matrix[row][col] + max(maxCost(matrix,row,col-1),maxCost(matrix,row-1,col))

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(maxCost(cost, 1, 2))