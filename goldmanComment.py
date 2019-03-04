#https://leetcode.com/problems/remove-comments/

#Loop through array
#Loop through each element of an array ,
    # if ith element was / & i+1 was / ignore the rest of the string or basically dont writeit out
    # if ith element was / & i+1 was * set a dont-write-flag and then done write anything out untilll the slag is set to false
    # if ith element was * & i+1 was . set a dont-write-flag to false

def remComment(inpArr):
    outArr=[]
    dontWriteBulkCom = False
    dontWriteDoubSlash = False

    for line in inpArr:
        outLine=[]

        dontWriteDoubSlash = False
        i=0
        while i < len(line):
            if i < (len(line) - 1) and line[i] == '/' and line[i+1] == '/':
                dontWriteDoubSlash = True
            if i < (len(line) - 1) and line[i] == '/' and line[i+1] == '*':
                dontWriteBulkCom = True
            if i < (len(line) - 1) and line[i] == '*' and line[i+1] == '/':
                dontWriteBulkCom = False
                i=i+2
            if i < (len(line)) and dontWriteDoubSlash == False and dontWriteBulkCom == False:
                outLine.append(line[i])
            i+=1
        if (len(outLine) > 0):
          outArr.append(''.join(outLine))
    return  outArr

input=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
 "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

print(remComment(input))