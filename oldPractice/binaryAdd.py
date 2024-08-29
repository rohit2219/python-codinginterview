def binAddHelp(num1, num2):
    sum = 0
    carry = 0
    #print('hits helper',num1, num2,type(num1),type(num2))
    if num1 == '1' and num2 == '1':
        return sum, carry+1
    elif num1 == '1' and num2 == '0':
        #print('return from helper',sum+1, carry)
        return sum+1, carry
    elif num1 == '0' and num2 == '1':
        return sum+1, carry
    elif num1 == '0' and num2 == '0':
        return sum, carry


def binAdd(bin1, bin2):
    #bin1 = bin1.split()
    #bin2 = bin2.split()
    # fill by zeroes if length of both binaries are not equal
    #if len(bin1) != len(bin2):
    #    fillzeroes(bin1, bin2)
    ctr1 = len(bin1)-1
    ctr2 = len(bin2)-1
    outStr = ''
    sum = 0
    carry = 0
    #prevCarry=0
    while ctr1 >= 0:
        #print(ctr1,ctr2)
        #print('before call:',bin1[ctr1],bin2[ctr2])
        #print('befcall    :',bin1[ctr1], bin2[ctr2], sum, carry, outStr)
        prevCarry=carry
        sum, carry = binAddHelp(bin1[ctr1], bin2[ctr2])
        if prevCarry == 1 and carry==1:
            sum=1
            carry=1
        if prevCarry == 1 and sum==1 and carry==0:
            sum=0
            carry=1

        #sum, carry = binAddHelp(str(sum), str(carry))
        outStr = str(sum) + outStr

        if ctr1 == 0 and carry == 1:
            outStr = str(carry) + outStr
        ctr1=ctr1-1
        ctr2=ctr2-1

    return outStr

print('binadd:',binAdd('11','01'))
