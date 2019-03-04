
def knapSack(wtKnapsack , wtArr, val, lenVal):
    K = [[0 for x in range(wtKnapsack + 1)] for x in range(lenVal + 1)]
    print(K)
    # Build table K[][] in bottom up manner
    for i in range(lenVal + 1):
        for w in range(wtKnapsack + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wtArr[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wtArr[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][wtKnapsack ]


# Driver program to test above function
val = [1,4,5,7]
wt = [1,3,4,5]
wtKnapsack = 11
n = len(val)
print(knapSack(wtKnapsack, wt, val, n))
