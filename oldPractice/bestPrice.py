#https://www.programcreek.com/2014/03/leetcode-candy-java/

def candyDistribute(ratingArr,totCandy):
    # 1) sort the arr
    # 2) go ascending in array , starting with one candy , increase the number of candies to each children with ratings
        # in step 2 also keep a copy of children with highest rating in one aray
    #3) the rest of the candy distribute it equally among the rest of children and the remainder should be again assigned
    # in descending order
    ratingArr.sort();
    noChild=len(ratingArr)
    candyArr=[]
    numCandy=1
    candyGiven=0
    prevRating=ratingArr[0]
    if ratingArr.sum() > totCandy:
        return

    for i in range(noChild-1):
        currRating = ratingArr[i]
        if currRating > prevRating:
            numCandy = numCandy + 1
        candyArr[i]=numCandy
        candyGiven=candyGiven+numCandy
        prevRating=ratingArr[i]

    remainingCandy=totCandy - candyGiven
    candyToEachChild=int(remainingCandy/noChild)
    remCandyFinal=remainingCandy%noChild

    for j in reversed(range(noChild-1)):
        if (remCandyFinal > 0):
            candyArr[j] = candyArr[j] + candyToEachChild + 1
            remCandyFinal = remCandyFinal - 1
        else:
            candyArr[j] = candyArr[j] + candyToEachChild
