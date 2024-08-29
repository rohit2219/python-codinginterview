def one(num):
    switcher = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return switcher.get(num)


def two_less_20(num):
    switcher = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    return switcher.get(num)


def ten(num):
    switcher = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    return switcher.get(num)

def convertNumToAplh(num):
    #num=str(num)

    #convert to str
    stringOfInt=lambda x:str(x)
    #find exponenntial form
    tenPowOfInt=lambda x:str(len(x))
    twoDigNumWord=lambda x:two_less_20(x) if x < 20 else (ten(x) + one(x))
    threeDigNumWord = lambda x:one(stringOfInt(x)[0]) * 'Hundred' + twoDigNumWord(stringOfInt(x)[0:2])
    wordNum=''
    if tenPowOfInt(num) == 1:
        wordNum=one(num)
    elif tenPowOfInt(num) == 2:
        wordNum =twoDigNumWord(num)
    elif tenPowOfInt(num) == 3:
        wordNum =threeDigNumWord(num)
    elif tenPowOfInt(num) == 4:
        wordNum = one(int(stringOfInt[num][0])) * 'Thousand' + threeDigNumWord(num)
    elif tenPowOfInt(num) == 5:
        wordNum = twoDigNumWord(int(stringOfInt[num][0:1])) * 'Thousand' + threeDigNumWord(int(num[1:4]))
    elif tenPowOfInt(num) == 6:
        if num == 100000:
            wordNum = 'one million'
        else:

    elif tenPowOfInt(num) == 7:

    return wordNum