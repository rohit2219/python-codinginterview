def callRefValue(passValueStr,passValueList):
    passValueStr='hello'
    passValueList.append(3)
    print(passValueStr,passValueList)
    return

valueStr='rohit'
valueList=[1,2]
print('--1',valueStr,valueList)
print(callRefValue(valueStr,valueList))
print('--2',valueStr,valueList)