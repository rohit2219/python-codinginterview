#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, inpStr: str):
        longSubstr=""
        maxLen=0
        prevMaxlen=0
        for i in range(len(inpStr)):

            palStr1=self.lenPalinAtPoint(inpStr,i,i)
            palStr2=self.lenPalinAtPoint(inpStr,i,i+1)

            if max(maxLen,max(len(palStr1),len(palStr2))) > maxLen:
                longSubstr = palStr1 if (len(palStr1) > len(palStr2)) else palStr2
                maxLen=len(longSubstr)
        return longSubstr
    def lenPalinAtPoint(self,string,left,right):
        palin=""
        while (left > 0 and right < len(string) and string[left] == string[right] ):
            palin = str[left-1:right]
            left -= 1
            right += 1