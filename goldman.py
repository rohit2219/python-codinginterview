#1/6 2/3
#1) gcd 2)

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

def addFract(frac1,frac2):
    num1=int(frac1.split('/')[0])
    den1=int(frac1.split('/')[1])

    num2=int(frac2.split('/')[0])
    den2=int(frac2.split('/')[1])
    denGcd=gcd(den2,den1)
    resNum=num1*(denGcd/den1) + num2*(denGcd/den2)
    resDen=denGcd
    print(str(resNum/(gcd(resNum,resDen)) ) + '/' + str(resDen/gcd(resNum,resDen)))

#addFract('2/3','1/3')

#2) Find length of a string

def lenStr(x):
    count=0
    for i in x:
        count=count+1;
    return count

#print(lenStr('eee'))

# pairs of nos in an array which add up to a number

#1,2,3,4,5

#7
def smallestSubArr(inpArr,sumNum):
    winS=0
    winE=1
    resMinArr=inpArr
    for i  in range(len(inpArr)-1):
        sumWin=inpArr[winS]
        print(winS,winE,inpArr[winS],inpArr[winE])
        while winS<len(inpArr)-1:
            sumWin=sumWin+inpArr[winE]
            if sumWin > sumNum:
                print(inpArr[winS:winE+1])
                if len(inpArr[winS:winE+1]) < len(resMinArr):
                    resMinArr=inpArr[winS:winE+1]
                break
            winE=winE+1
        winS = winS + 1
        winE = winS + 1

    return len(resMinArr)
#print(smallestSubArr([1,2,3,4,5],7))

def numbersAdd(inpArr,sumNum):
    sorted(inpArr)
    print(inpArr)
    l=0
    r=len(inpArr)-1
    outList=[]
    count=0
    while l<r or count < 10:
        print(l,r)
        if inpArr[l] + inpArr[r] == sumNum:
            outList.append([inpArr[l],inpArr[r]])
            l=l+1
        elif inpArr[l] + inpArr[r] < sumNum:
            l=l+1
        else:
            r=r-1
        count=count+10

    #print('finalop',outList)
    return
##numbersAdd([1,2,3,4,5],7)

def findMedian(arr1,arr2):

    len1=len(arr1)
    len2=len(arr2)
    evenFlag=True
    if (len1+len2)%2 == 0:
        evenFlag=True
    else:
        evenFlag=False
    combArr=[]
    posArr1=0
    posArr2=0
#if even im gonna sum the mid of both , else avg the two middle
    while (posArr1 < ((len1 + 1) /2)) and posArr2 < ((len2 + 1) /2):
        if arr1[posArr1] < arr2[posArr2]:
            if posArr1 < ((len1 + 1) / 2):
                combArr.append(arr1[posArr1])
                posArr1=posArr1+1
            if posArr2 < ((len2 + 1) / 2):
                combArr.append(arr2[posArr2])
                posArr2=posArr2+1

        else:
            if posArr2 < ((len2 + 1) / 2):
                combArr.append(arr2[posArr2])
                posArr2=posArr2+1
            if posArr2 < ((len2 + 1) / 2):
                combArr.append(arr1[posArr1])
                posArr1=posArr1+1

#http://grajob.com/goldman-sachs-interviewgiven-a-string-find-its-first-non-repeating-character/
def nonRepeatChar(inpStr):
    hashStr={}
    for i in inpStr:
        if i in hashStr:
            hashStr[i]=hashStr[i] + 1
        else:
            hashStr[i]=1

    for j in inpStr:
        if  hashStr[j] == 1:
            return j

print(nonRepeatChar('GeeksforGeeks'))

# https://www.geeksforgeeks.org/trapping-rain-water/
#https://www.youtube.com/watch?v=HmBbcDiJapY
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trapRain(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water


def trapRainwrong(inpArr):
    left=0
    right=len(inpArr)-1
    curVol=0
    prevCurVol=0
    prevLsrWidth=0
    while left < right:
        if inpArr[left]==0:
            left=left+1
            continue
        if inpArr[right]==0:
            right=right-1
            continue

        lsrWidth=inpArr[left] if(inpArr[left]<inpArr[right]) else inpArr[right]
        if lsrWidth <= prevLsrWidth:
            continue

        curVol=abs(left-right)*lsrWidth
        curVol=(curVol-prevCurVol)+ prevCurVol

        if lsrWidth==inpArr[left]:
            left=left+1
        else:
            right=right-1
        prevLsrWidth=lsrWidth
        prevCurVol=curVol