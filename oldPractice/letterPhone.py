#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
numLetrMap={
    2:['a','b','c'],
    3:['d','e','f'],
    4:['g','h','i'],
    5:['jkl'],
    6:['mno'],
    7:['pqrs'],
    8:['tuv'],
    9:['wxyz'],

}

def combStringLetr(singLetter,strLetter):
    combList=[]
    for i in strLetter:
        combList.append(singLetter+i)
    return  combList

def combTwoDigits(dig1,dig2):
    retcombTwoDIgits=[]
    for i in numLetrMap[dig1]:
        for j in numLetrMap[dig2]:
            retcombTwoDIgits.append(i+j)
    return retcombTwoDIgits


#def
#def combLtr(inpNum):
print(combTwoDigits(2,3))
